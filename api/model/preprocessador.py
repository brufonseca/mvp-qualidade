from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pickle

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
    
    def __init__(self, X, y, tamanho_conjunto=0.2, semente=42):
        """
        Inicializa a classe PreProcessador 

        Args:
            X (pd.DataFrame): dados de entrada.
            y (pd.Series): dados de saída
            tamanho_conjunto (float): proporção dos dados
            semente (int): semente para a randomização
        """
        self.X = X
        self.y = y
        self.tamanho_conjunto = tamanho_conjunto
        self.semente = semente
        self.std_scaler = None
        self.min_max_scaler = None
        
    def separar_dados(self):
        """
        Separa os dados em conjuntos de treino e teste.

        Returns:
            tuple: Dados de treino e teste
        """
        X_treino, X_teste, y_treino, y_teste = train_test_split(
            self.X, self.y, test_size=self.tamanho_conjunto, random_state=self.semente, stratify=self.y
        )
        return X_treino, X_teste, y_treino, y_teste
    
    def validao_cruzada_estratificada(self, n_splits=5):
        """
        Cria objetos para validação cruzada estratificada.

        Args:
            n_splits (int): Número de dobras para a validação cruzada.

        Returns:
            StratifiedKFold: Objeto StratifiedKFold
        """
        return StratifiedKFold(n_splits=n_splits, shuffle=True, semente=self.semente)
    
    def normalizar_padronizar(self, metodo = 'padronizar'):
        """
        Normaliza ou padroniza os dados de entrada.

        """
        
        if metodo == 'padronizar':
            scaler = self.std_scaler
        elif metodo == 'normalizar':
            scaler = self.min_max_scaler
        

        self.X = scaler.fit_transform(self.X)
    
    def definir_scalers(self):
        """
        Define os scalers para normalização/padronização.

        """
        #self.std_scaler = pickle.load(open('./ML/scalers/std_scaler_mushroom.pkl', 'rb'))
        self.min_max_scaler = pickle.load(open('./ML/scalers/minmax_scaler_mushroom.pkl', 'rb'))
