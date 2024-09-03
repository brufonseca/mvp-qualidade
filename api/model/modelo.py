import pickle

class ModeloML:
    """Classe que representa um modelo de machine learning
    
    ...
    
    Atributos
    ---------
    modelo: 
        modelo de machine learning
    
    """

    def __init__(self, caminho_arquivo):
        
        self.modelo = None

        self.carregar_modelo(caminho_arquivo)

    def carregar_modelo(self, caminho_arquivo):
        """Carrega o modelo a partir do caminho para o arquivo .pkl"""
        try:
            with open(caminho_arquivo, 'rb') as arquivo:
                self.modelo = pickle.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
        except pickle.PickleError:
            print("Erro ao carregar o modelo a partir do arquivo.")
        except Exception as e:
            print(f"Erro: {e}")
            
    def realizar_predicoes(self,dados_entrada):
        """Realiza predicoes para os dados fornecidos"""
        if self.modelo is None:
            raise Exception('Modelo não definido')
        
        predicao = self.modelo.predict(dados_entrada)
        return predicao
