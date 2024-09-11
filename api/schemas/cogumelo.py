from datetime import date
from typing import List
from pydantic import BaseModel

from model.cogumelo import Cogumelo


class CogumeloSchema(BaseModel):
    """    
    Define como exibir uma instancia de cogumelo
    """
    
    name: str = "Cogumelo 1"
    gill_size: int = 0
    gill_color: int = 6
    stalk_root: int = 0
    ring_type: int = 4
    spore_print_color: int = 4
    odor: int = 5
    population: int = 1
    bruises: int = 0
    stalk_surface_above_ring: int = 2

class CogumeloViewSchema(BaseModel):
    """ 
    Define como um cogumelo sera retornado
    """
    id: int = 1
    name: str = "Cogumelo 1"
    gill_size: int = 0
    gill_color: int = 6
    stalk_root: int = 0
    ring_type: int = 4
    spore_print_color: int = 4
    odor: int = 5
    population: int = 1
    bruises: int = 0
    stalk_surface_above_ring: int = 2
    outcome: int = None
    


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
            "gill_size": cogumelo.gill_size,
            "gill_color": cogumelo.gill_color,
            "stalk_root": cogumelo.stalk_root,
            "ring_type": cogumelo.ring_type,
            "spore_print_color": cogumelo.spore_print_color,
            "odor": cogumelo.odor,
            "population": cogumelo.population,
            "bruises": cogumelo.bruises,
            "stalk_surface_above_ring": cogumelo.stalk_surface_above_ring,
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
        "gill_size": cogumelo.gill_size,
        "gill_color": cogumelo.gill_color,
        "stalk_root": cogumelo.stalk_root,
        "ring_type": cogumelo.ring_type,
        "spore_print_color": cogumelo.spore_print_color,
        "odor": cogumelo.odor,
        "population": cogumelo.population,
        "bruises": cogumelo.bruises,
        "stalk_surface_above_ring": cogumelo.stalk_surface_above_ring,
        "outcome": cogumelo.outcome
    }
