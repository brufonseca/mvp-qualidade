from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

class PreProcessador:
    
    """
    Classe para realizar o pré-processamento de dados para machine learning.

    Atributos:
        X (pd.DataFrame): Dados de entrada.
        y (pd.Series): Rótulos de saída correspondentes aos dados de entrada.
        tamanho_conjunto (float): Proporção dos dados a serem usados para teste.
        semente (int): Semente para a randomização (para reprodução dos resultados).
        scaler (object): Scaler para normalização/padronização dos dados (StandardScaler ou MinMaxScaler).
    """
    
    def __init__(self, X, y, tamanho_conjunto=0.2, semente=42):
        """
        Inicializa a classe PreProcessador com os dados, proporção de teste e estado aleatório.

        Args:
            X (pd.DataFrame ou np.array): Dados de entrada.
            y (pd.Series ou np.array): Rótulos de saída.
            tamanho_conjunto (float): Proporção dos dados a serem usados para teste.
            semente (int): Semente para a randomização.
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
            tuple: Dados de treino e teste, bem como rótulos correspondentes.
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
            StratifiedKFold: Objeto StratifiedKFold configurado.
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
        Retorna o scaler utilizado para normalização/padronização.

        Returns:
            object: Scaler utilizado (StandardScaler ou MinMaxScaler).
        
        Raises:
            ValueError: Se o scaler ainda não tiver sido definido.
        """
        self.std_scaler = StandardScaler()
        self.min_max_scaler = MinMaxScaler()
