import pandas as pd


class CarregadorDados:
    """
    Classe para carregar dados 

    Atributos:

        caminho (str): caminho do arquivo que contém os dados
        delimitador (str): delimitador usado no arquivo de dados
        dataset (object) : dataframe com os dados
    """

    def __init__(self, caminho, delimitador=','):
        """
        Inicializa a classe DadosLoader

        Args:
            caminho (str): caminho do arquivo que contém os dados
            delimitador (str): delimitador usado no arquivo de dados
        """
        self.caminho = caminho
        self.delimitador = delimitador
        self.dataset = self.carregar_dados()
        
        
    def carregar_dados(self):
        """
        Carrega os dados em um dataframe.

        """
        try:
           return pd.read_csv(self.caminho, delimiter=self.delimitador)
        except Exception as e:
            raise Exception(f"Erro ao processar os dados: {e}")
        