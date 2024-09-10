import pickle

class ModeloML:
    """
    Classe que representa um modelo de machine learning
    
    Atributos:
    modelo (object):  modelo de machine learning
    
    """
    def __init__(self, caminho_arquivo):
        """
        Inicializa a classe ModeloML
        
        Args:
        caminho_arquivo (str):  caminho para o arquivo do modelo
        
        """
        self.modelo = None

        self.carregar_modelo(caminho_arquivo)

    def carregar_modelo(self):
        """
        Carrega o modelo a partir de um arquivo .pkl
        
        Returns:
            object: modelo 
        
        """
        try:
            with open(self.caminho_arquivo, 'rb') as arquivo:
                self.modelo = pickle.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {self.caminho_arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar o modelo a partir do arquivo.: {e}")
            
    def realizar_predicoes(self,dados_entrada):
        """
        Realiza predições para os dados fornecidos
        
        Returns:
            object: predicoes realizadas 
        
        """
        if self.modelo is None:
            raise Exception('Modelo não definido')
        
        predicao = self.modelo.predict(dados_entrada)
        return predicao
