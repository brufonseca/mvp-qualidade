from sklearn.metrics import accuracy_score

class AvaliadorModelo:
    """
    Classe para avaliar o desempenho de um modelo de machine learning.

    Atributos:
        modelo (object): instância de ModeloML
        X_teste (pd.DataFrame): Dados de entrada
        y_teste (pd.Series): Dados de saida
    """ 
    
    def __init__(self, modelo, X_teste, y_teste):
        """
        Inicializa a classe AvaliadorModelo

        Args:
            modelo (object):  instância de ModeloML
            X_teste (pd.DataFrame): Dados de entrada
            y_teste (pd.Series): Dados de saida
        """
        self.modelo = modelo
        self.X_teste = X_teste
        self.y_teste = y_teste
        
    def calcular_acuracia(self):
        """
        Calcula a acurácia do modelo

        Returns:
            float: acurácia do modelo
        
        """

        if self.X_teste is None or self.y_teste is None:
            raise ValueError("Dados não fornecidos")
        
        predicoes = self.modelo.realizar_predicoes(self.X_teste)
        
        acuracia = accuracy_score(self.y_teste, predicoes)
        return acuracia