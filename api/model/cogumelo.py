from sqlalchemy import Column, Integer, String, DateTime
from  model import Base
from datetime import datetime
from typing import Union

class Cogumelo(Base):
    
    """
    Classe para cogumelos

    Atributos:
        id (int): Identificador único para cada registro.
        name (string) : Nome identificador do cogumelo
        odor (int): Odor do cogumelo.
        gill_size (int): Tamanho das lâminas do cogumelo.
        gill_color (int): Cor das lâminas do cogumelo.
        stalk_shape (int): Formato do caule do cogumelo.
        stalk_root (int): Raiz do caule do cogumelo.
        ring_type (int): Tipo de anéis no caule.
        spore_print_color (int): Cor da impressão das esporas.
        population (int): População do cogumelo no habitat.
        habitat (int): Habitat do cogumelo.
        outcome (int, optional): Classe do cogumelo (se comestível ou venenoso).
        data_insercao (datetime): Data e hora de inserção dos dados.
    """
    
    __tablename__ = 'cogumelo'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("Name", String(50))
    odor = Column("Odor",Integer)
    gill_size = Column("GillSize",Integer)
    gill_color = Column("GillColor",Integer)
    stalk_shape = Column("StalkShape",Integer)
    stalk_root = Column("StalkRoot",Integer)
    ring_type = Column("RingNumber",Integer)
    spore_print_color = Column("SporePrintColor",Integer)
    population = Column("Population",Integer)
    habitat = Column("Habitat",Integer)
    outcome = Column("Class",Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    
    
    def __init__(self, name: str, odor: int, 
                 gill_size: int, gill_color: int,
                 stalk_shape: int, stalk_root: int, 
                 ring_type: int, spore_print_color: int, population: int, habitat: int,
                 outcome: int = None,  data_insercao:Union[DateTime, None] = None):
        """
        Inicializa uma instância da classe Cogumelo

        Args:
            name (string) : Nome identificador do cogumelo
            odor (int): Odor do cogumelo.
            gill_size (int): Tamanho das lâminas do cogumelo.
            gill_color (int): Cor das lâminas do cogumelo.
            stalk_shape (int): Forma do caule do cogumelo.
            stalk_root (int): Raiz do caule do cogumelo.
            ring_type (int): Tipo de anéis no caule.
            spore_print_color (int): Cor da impressão das esporas.
            population (int): População do cogumelo no habitat.
            habitat (int): Habitat do cogumelo.
            outcome (int, optional): Classe do cogumelo (se comestível ou venenoso).
        """
        self.name = name
        self.odor = odor
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_shape = stalk_shape
        self.stalk_root = stalk_root
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        self.population = population
        self.habitat = habitat
        self.outcome = outcome
        
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
    
    
    