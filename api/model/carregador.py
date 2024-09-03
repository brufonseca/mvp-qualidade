import pandas as pd


class CarregadorDados:
    """
    Classe para carregar dados de uma URL e colocá-los em um DataFrame.

    ...

    Atributos
    ---------

        caminho (str): O caminho do arquivo local ou a URL para os dados.
        delimitador (str): O delimitador usado no arquivo de dados (padrão é ',').
    """

    def __init__(self, caminho, delimitador=','):
        """
        Inicializa a classe DadosLoader com a origem dos dados, o caminho e o delimitador.

        Args:
            caminho (str): O caminho para os dados.
            delimitador (str): O delimitador usado no arquivo de dados (padrão é ',').
        """
        self.caminho = caminho
        self.delimitador = delimitador
        self.dataset = None
        
    def carregar_dados(self):
        """
        Carrega os dados da URL e os coloca em um DataFrame.

        Utiliza a biblioteca requests para baixar os dados e pandas para criar o DataFrame.
        Se a URL não for acessível ou os dados não puderem ser processados, será gerado um erro.

        Raises:
            Exception: Se ocorrer um erro ao baixar ou processar os dados.
        """
        try:
            self.dataset = pd.read_csv(self.caminho, delimiter=self.delimitador)
        except Exception as e:
            raise Exception(f"Erro ao processar os dados: {e}")
        