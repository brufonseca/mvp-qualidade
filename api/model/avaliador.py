from sklearn.metrics import accuracy_score

class AvaliadorModelo:
    """
    Classe para avaliar o desempenho de um modelo de machine learning.

    Atributos:
        modelo (object): Uma instância de uma classe de modelo que possui um método `predict`.
        X_teste (pd.DataFrame ou np.array): Dados de entrada para teste.
        y_teste (pd.Series ou np.array): Rótulos verdadeiros correspondentes aos dados de teste.
    """ 
    
    def __init__(self, modelo, X_teste, y_teste):
        """
        Inicializa a classe AvaliadorModelo com o modelo, dados de teste e rótulos verdadeiros.

        Args:
            modelo (object): Uma instância do modelo a ser avaliado.
            X_teste (pd.DataFrame ou np.array): Dados de entrada para teste.
            y_teste (pd.Series ou np.array): Rótulos verdadeiros correspondentes aos dados de teste.
        """
        self.modelo = modelo
        self.X_teste = X_teste
        self.y_teste = y_teste
        
    def calcular_acuracia(self):
        """
        Calcula a acurácia do modelo com base nos dados de teste e rótulos verdadeiros.

        Returns:
            float: A acurácia do modelo, que é a proporção de previsões corretas.
        
        Raises:
            ValueError: Se os dados de teste e os rótulos não forem fornecidos.
        """

        if self.X_teste is None or self.y_teste is None:
            raise ValueError("Dados de teste e rótulos devem ser fornecidos.")
        
        # Fazer previsões com o modelo
        previsoes = self.modelo.realizar_predicoes(self.X_teste)
        
        # Calcular a acurácia
        acuracia = accuracy_score(self.y_teste, previsoes)
        return acuracia