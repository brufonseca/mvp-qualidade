from datetime import date
from typing import List
from pydantic import BaseModel

from model.cogumelo import Cogumelo


class CogumeloSchema(BaseModel):
    """    
    Define como exibir uma instancia de cogumelo
    """

    name: str = "Cogumelo 1"
    odor: int = 5
    gill_size: int = 0
    gill_color: int = 1
    stalk_shape: int = 0
    stalk_root: int = 3
    ring_type: int = 1
    spore_print_color: int = 7
    population: int = 0
    habitat: int = 0


class CogumeloViewSchema(BaseModel):
    """ 
    Define como um cogumelo sera retornado
    """
    id: int = 1
    name: str = "Cogumelo 1"
    odor: int = 5
    gill_size: int = 0
    gill_color: int = 1
    stalk_shape: int = 0
    stalk_root: int = 3
    ring_type: int = 1
    spore_print_color: int = 7
    population: int = 0
    habitat: int = 0


class CogumeloListaSchema(BaseModel):
    """
    Define como retornar uma lista de cogumelos
    """
    cogumelos: List[CogumeloSchema]


class CogumeloBuscaSchema(BaseModel):
    """
    Define como representar uma busca. A busca sera feita pelo nome do cogumelo
    """
    name: str = "Cogumelo 1"


class CogumeloRemocaoSchema(BaseModel):
    """ 
    Define a estrutura do retorno de uma requisicao de remocao
    """

    mensagem: str


def retorna_lista_cogumelos(cogumelos: List[Cogumelo]):
    """ Retorna uma lista de cogumelos seguindo o schema definido em
        CogumeloViewSchema.
    """
    lista_cogumelos = []
    for cogumelo in cogumelos:
        lista_cogumelos.append({
            "id": cogumelo.id,
            "name": cogumelo.name,
            "odor": cogumelo.odor,
            "gill_size": cogumelo.gill_size,
            "gill_color": cogumelo.gill_color,
            "stalk_shape": cogumelo.stalk_shape,
            "stalk_root": cogumelo.stalk_root,
            "ring_type": cogumelo.ring_type,
            "spore_print_color": cogumelo.spore_print_color,
            "population": cogumelo.population,
            "habitat": cogumelo.habitat,
            "outcome": cogumelo.outcome
        })
    return {
        "cogumelos": lista_cogumelos
    }


def retorna_cogumelo(cogumelo: Cogumelo):
    """ Retorna uma representacao de cogumelo
    """
    return {
        "id": cogumelo.id,
        "name": cogumelo.name,
        "odor": cogumelo.odor,
        "gill_size": cogumelo.gill_size,
        "gill_color": cogumelo.gill_color,
        "stalk_shape": cogumelo.stalk_shape,
        "stalk_root": cogumelo.stalk_root,
        "ring_type": cogumelo.ring_type,
        "spore_print_color": cogumelo.spore_print_color,
        "population": cogumelo.population,
        "habitat": cogumelo.habitat,
        "outcome": cogumelo.outcome
    }
