from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote

from model import Session, Cogumelo, PreProcessador, ModeloML
from logger import logger

from schemas.cogumelo import (
    CogumeloSchema, CogumeloViewSchema, CogumeloListaSchema,
    CogumeloRemocaoSchema, CogumeloBuscaSchema,
    retorna_cogumelo, retorna_lista_cogumelos
)

from schemas.error import ErrorSchema
from flask_cors import CORS

info = Info(title="Classificação de cogumelos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cogumelo_tag = Tag(
    name="Cogumelos", description="Adição, visualização e remoção e predição de cogumelos comestíveis ou venenosos")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentacao.
    """
    return redirect('/openapi')

@app.get('/listar_cogumelos', tags=[cogumelo_tag],
         responses={"200": CogumeloListaSchema, "404": ErrorSchema})
def get_cogumelos():
    """Retorna todos os registros de cogumelos presentes no bd
     Args:
       none
        
    Returns:
        list: lista de cogumelos cadastrados no bd

    """
    logger.debug("Buscando entradas de cogumelos ")
    # criando conexao com o bd
    session = Session()
    # fazendo a busca
    cogumelos = session.query(Cogumelo).all()

    if not cogumelos:
        # se nao ha registros cadastrados
        return {"cogumelos": []}, 200
    else:
        logger.debug("%s cogumelos encontrados", len(cogumelos))
        # retorna a representacao de um registro
        return retorna_lista_cogumelos(cogumelos), 200

@app.get('/buscar_cogumelo', tags=[cogumelo_tag],
         responses={"200": CogumeloSchema, "404": ErrorSchema})
def get_cogumelo(query: CogumeloBuscaSchema):
    """Faz a busca de um cogumelo a partir do nome informado

    Args:
        nome (str): nome do cogumelo
        
    Returns:
        dict: representação do cogumelo e categoria associada
    """
    cogumelo_nome = query.name
    logger.debug("Buscando cogumelo para o nome %s ", cogumelo_nome)
    # criando conexao com o bd
    session = Session()
    # fazendo a busca
    cogumelo = session.query(Cogumelo).filter(
        Cogumelo.name == cogumelo_nome).first()

    if not cogumelo:
        # se o registro nao foi encontrado
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
    """Deleta um cogumelo a partir do nome informado

    Retorna uma mensagem de confirmacao da remocao.
    """
    cogumelo_nome = unquote(query.name)
    logger.debug("Deletando cogumelo %s", cogumelo_nome)
    # criando conexao com o bd
    session = Session()
    # fazendo a remocao
    
    cogumelo =  session.query(Cogumelo).filter(
        Cogumelo.name == cogumelo_nome).first()

    if cogumelo:
        # retorna a representacao da mensagem de confirmacao
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
def realizar_predicao(body:CogumeloSchema):
    """Adiciona um novo cogumelo
    Retorna uma representação dos cogumelos e classificações associadas
    
    Args:
        name (string) : Nome identificador do cogumelo
        odor (int): Odor do cogumelo.
        gill_size (int): Tamanho das lâminas do cogumelo.
        gill_color (int): Cor das lâminas do cogumelo.
        stalk_root (int): Raiz do caule do cogumelo.
        stalk_shape (int): Formato do caule do cogumelo.
        ring_type (int): Tipo de anéis no caule.
        spore_print_color (int): Cor da impressão das esporas.
        population (int): População do cogumelo no habitat.
        outcome (int, optional): Classe do cogumelo (se comestível ou venenoso).

    Returns:
        dict: representação do paciente e diagnóstico associado
    
    """
    
    # Recuperando os dados do formulário
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
    
    #Preparando os dados para o modelo
    pp = PreProcessador()
    pp.preparar_dados_formulario(body)
    X_entrada = pp.X
    
    caminho_modelo = "./ML/models/dt_mushroom_classifier.pkl"
    
    modelo = ModeloML(caminho_modelo)
    
    predicoes = modelo.realizar_predicoes(X_entrada)
    
    outcome = int(predicoes[0])
    
    cogumelo = Cogumelo(name,  gill_size, gill_color, stalk_root, ring_type, spore_print_color,
                 odor, population, bruises, stalk_surface_above_ring,
                 outcome)
    
    logger.debug(f"Adicionando cogumelo: '{cogumelo.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se cogumelo já existe na base
        if session.query(Cogumelo).filter(Cogumelo.name == body.name).first():
            error_msg = "Cogumelo já existente na base :/"
            logger.warning(f"Erro ao adicionar cogumelo '{cogumelo.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando cogumelo
        session.add(cogumelo)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado cogumelo: '{cogumelo.name}'")
        return retorna_cogumelo(cogumelo), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo cogumelo :/"
        logger.warning(f"Erro ao adicionar cogumelo '{cogumelo.name}', {error_msg}")
        return {"message": error_msg}, 400
    
