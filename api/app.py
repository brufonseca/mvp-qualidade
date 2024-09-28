from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from model import Session, Cogumelo, ModeloML
from logger import logger
import numpy as np

from schemas.cogumelo import (
    CogumeloSchema, CogumeloViewSchema, CogumeloListaSchema,
    CogumeloRemocaoSchema, CogumeloBuscaSchema,
    retorna_cogumelo, retorna_lista_cogumelos
)

from schemas.error import ErrorSchema
from flask_cors import CORS

# Informações da API
info = Info(title="Classificação de cogumelos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para a documentação
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cogumelo_tag = Tag(
    name="Cogumelos", description="Adição, visualização e remoção e predição de cogumelos comestíveis ou venenosos")


@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/listar_cogumelos', tags=[cogumelo_tag],
         responses={"200": CogumeloListaSchema, "404": ErrorSchema})
def get_cogumelos():
    """
    Retorna todos os registros de cogumelos presentes no banco de dados.

    Returns:
        list: Lista de cogumelos cadastrados no banco de dados.
    """
    logger.debug("Buscando entradas de cogumelos ")
    session = Session()
    cogumelos = session.query(Cogumelo).all()

    if not cogumelos:
        return {"cogumelos": []}, 200
    else:
        logger.debug("%s cogumelos encontrados", len(cogumelos))
        return retorna_lista_cogumelos(cogumelos), 200


@app.get('/buscar_cogumelo', tags=[cogumelo_tag],
         responses={"200": CogumeloSchema, "404": ErrorSchema})
def get_cogumelo(query: CogumeloBuscaSchema):
    """
    Faz a busca de um cogumelo a partir do nome informado.

    Args:
        query (CogumeloBuscaSchema): Nome do cogumelo.

    Returns:
        dict: Representação do cogumelo encontrado.
    """
    cogumelo_nome = query.name
    logger.debug("Buscando cogumelo para o nome %s ", cogumelo_nome)
    # criando conexao com o bd
    session = Session()
    # fazendo a busca
    cogumelo = session.query(Cogumelo).filter(
        Cogumelo.name == cogumelo_nome).first()

    if not cogumelo:
        error_msg = "Cogumelo não encontrado na base :/"
        logger.warning(
            "Erro ao buscar cogumelo %s , %s", cogumelo_nome, error_msg)
        return {"message": error_msg}, 404
    logger.debug("Cogumelo econtrado : %s", {cogumelo.name})
    # retorna a entrada encontrada
    return retorna_cogumelo(cogumelo), 200


@app.delete('/deletar_cogumelo', tags=[cogumelo_tag],
            responses={"200": CogumeloRemocaoSchema, "404": ErrorSchema})
def del_cogumelo(query: CogumeloBuscaSchema):
    """
    Deleta um cogumelo a partir do nome informado.

    Args:
        query (CogumeloBuscaSchema): Nome do cogumelo a ser deletado.

    Returns:
        dict: Mensagem de confirmação da remoção.
    """
    cogumelo_nome = unquote(query.name)
    logger.debug("Deletando cogumelo %s", cogumelo_nome)
    session = Session()

    cogumelo = session.query(Cogumelo).filter(
        Cogumelo.name == cogumelo_nome).first()

    if cogumelo:
        session.delete(cogumelo)
        session.commit()
        logger.debug("Deletado cogumelo %s", cogumelo_nome)
        return {"message": "Cogumelo removido", "nome": cogumelo_nome}

    error_msg = "Cogumelo não encontrada na base :/"
    logger.warning("Erro ao deletar cogumelo %s %s",
                   cogumelo_nome, error_msg)
    return {"message": error_msg}, 404


@app.post('/inserir_predicao', tags=[cogumelo_tag],
          responses={"200": CogumeloViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def realizar_predicao(body: CogumeloSchema):
    """
    Adiciona um novo cogumelo e realiza a predição.

    Args:
        body (CogumeloSchema): Dados do cogumelo a ser inserido.

    Returns:
        dict: Representação do cogumelo e predição realizada (comestível ou venenoso).
    """

    name = body.name
    gill_size = body.gill_size
    gill_color = body.gill_color
    stalk_root = body.stalk_root
    ring_type = body.ring_type
    spore_print_color = body.spore_print_color
    odor = body.odor
    population = body.population
    bruises = body.bruises
    stalk_surface_above_ring = body.stalk_surface_above_ring

    # Preparando os dados para o modelo
    X = np.array([
        body.gill_size,
        body.gill_color,
        body.stalk_root,
        body.ring_type,
        body.spore_print_color,
        body.odor,
        body.population,
        body.bruises,
        body.stalk_surface_above_ring
    ])

    X_entrada = X.reshape(1, -1)
    
    # Carregando o modelo
    caminho_modelo = "./ML/models/dt_mushroom_classifier.pkl"
    modelo = ModeloML(caminho_modelo)
    predicoes = modelo.realizar_predicoes(X_entrada)
    outcome = int(predicoes[0])
    cogumelo = Cogumelo(name,  gill_size, gill_color, stalk_root, ring_type, spore_print_color,
                        odor, population, bruises, stalk_surface_above_ring,
                        outcome)

    logger.debug(f"Adicionando cogumelo: '{cogumelo.name}'")

    try:
        session = Session()

        if session.query(Cogumelo).filter(Cogumelo.name == body.name).first():
            error_msg = "Cogumelo já existente na base :/"
            logger.warning(f"Erro ao adicionar cogumelo '{cogumelo.name}', {error_msg}")
            return {"message": error_msg}, 409

        session.add(cogumelo)
        session.commit()
        logger.debug(f"Adicionado cogumelo: '{cogumelo.name}'")
        return retorna_cogumelo(cogumelo), 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo cogumelo :/"
        logger.warning(f"Erro ao adicionar cogumelo '{cogumelo.name}', {error_msg}")
        return {"message": error_msg}, 400
