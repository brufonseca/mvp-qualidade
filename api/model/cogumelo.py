from sqlalchemy import Column, Integer, String, DateTime
from model import Base
from datetime import datetime
from typing import Union


class Cogumelo(Base):

    """
    Classe que representa um cogumelo

    Atributos:
        id (int): Identificador único para cada registro.
        name (str) : Nome identificador do cogumelo
        gill_size (int): Tamanho das lamelas do cogumelo.
        gill_color (int): Cor das lamelas.
        stalk_root (int): Tipo de raiz do caule.
        ring_type (int): Tipo de anel presente no caule.
        spore_print_color (int): Cor do esporo do cogumelo.
        odor (int): Odor característico do cogumelo.
        population (int): População onde o cogumelo é encontrado.
        bruises (int): Indica se o cogumelo apresenta hematomas.
        stalk_surface_above_ring (int): Superfície do caule acima do anel.
        outcome (int, optional): Classe do cogumelo .
        data_insercao (datetime): Data e hora da inserção do registro no banco de dados.
    """

    __tablename__ = 'cogumelo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    gill_size = Column(Integer)
    gill_color = Column(Integer)
    stalk_root = Column(Integer)
    ring_type = Column(Integer)
    spore_print_color = Column(Integer)
    odor = Column(Integer)
    population = Column(Integer)
    bruises = Column(Integer)
    stalk_surface_above_ring = Column(Integer)
    outcome = Column(Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, name,  gill_size, gill_color, stalk_root, ring_type, spore_print_color,
                 odor, population, bruises, stalk_surface_above_ring,
                 outcome: int = None,  data_insercao: Union[DateTime, None] = None):
        """
        Inicializa uma instância da classe Cogumelo

        Args:
            name (str) : Nome identificador do cogumelo
            gill_size (int): Tamanho das lamelas do cogumelo.
            gill_color (int): Cor das lamelas.
            stalk_root (int): Tipo de raiz do caule.
            ring_type (int): Tipo de anel presente no caule.
            spore_print_color (int): Cor do esporo do cogumelo.
            odor (int): Odor característico do cogumelo.
            population (int): População onde o cogumelo é encontrado.
            bruises (int): Indica se o cogumelo apresenta hematomas.
            stalk_surface_above_ring (int): Superfície do caule acima do anel.
            outcome (int): Classe do cogumelo.
            data_insercao (datetime): Data e hora da inserção do registro no banco de dados.
        """
        self.name = name
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_root = stalk_root
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        self.odor = odor
        self.population = population
        self.bruises = bruises
        self.stalk_surface_above_ring = stalk_surface_above_ring
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
