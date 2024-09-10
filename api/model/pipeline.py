import pickle


class Pipeline:
    """
    Classe para carregar um pipeline a partir de um arquivo .pkl.

    Atributos:
        caminho_arquivo (str): Caminho para o arquivo .pkl que contém o pipeline.
        pipeline : objeto pipeline carregado a do arquivo

    """


    def __init__(self, caminho_arquivo):
        
        """
        Inicializa a classe Pipeline

        Args:
            caminho_arquivo (str): Caminho para o arquivo .pkl que contém o pipeline.
        """
        
        self.caminho_arquivo = caminho_arquivo
        self.pipeline = None
    
    def carregar_pipeline(self):
        """
        Carrega o pipeline a partir do arquivo .pkl.

        """
        
        try:
            with open(self.caminho_arquivo, 'rb') as file:
                self.pipeline = pickle.load(file)
        except FileNotFoundError as e:
            print(f"Erro: O arquivo '{self.caminho_arquivo}' não foi encontrado.")
            raise e
        except IOError as e:
            print(f"Erro ao ler o arquivo '{self.caminho_arquivo}'.")
            raise e
        except Exception as e:
            print(f"Erro ao carregar o arquivo '{self.filepath}'.")
            raise e
    