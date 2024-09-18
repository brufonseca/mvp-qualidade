from sklearn.model_selection import train_test_split, StratifiedKFold
import pickle
import numpy as np


class PreProcessador:

    """
    Classe para realizar o pré-processamento dos dados

    Atributos:
        X (pd.DataFrame): dados de entrada.
        y (pd.Series): dados de saída
        tamanho_conjunto (float): proporção dos dados
        semente (int): semente para a randomização
        std_scaler (object): Scaler para normalização dos dados
        min_max_scaler (object): Scaler para padronização dos dados 
    """

    def __init__(self, tamanho_conjunto=0.2, semente=11):
        """
        Inicializa a classe PreProcessador 

        Args:
            tamanho_conjunto (float): proporção dos dados
            semente (int): semente para a randomização
        """
        self.X = None
        self.y = None
        self.tamanho_conjunto = tamanho_conjunto
        self.semente = semente

    def preparar_dados_formulario(self, form):
        X = np.array([
            form.gill_size,
            form.gill_color,
            form.stalk_root,
            form.ring_type,
            form.spore_print_color,
            form.odor,
            form.population,
            form.bruises,
            form.stalk_surface_above_ring
        ])

        X = X.reshape(1, -1)
        self.X = X




