from model import *

# To run: pytest -v test_modelos.py

caminho_dados = "./ML/data/test_dataset_mushroom.csv"

carregador = CarregadorDados(caminho_dados) 

dataset = carregador.dataset
X = dataset.drop(['class'], axis=1)
y = dataset["class"]

def test_modelo_dt():
    caminho_modelo_dt = "./ML/models/dt_mushroom_classifier.pkl"
    modelo_dt = ModeloML(caminho_modelo_dt) 
    avaliador_dt = AvaliadorModelo(modelo_dt,X,y)
    
    acuracia_dt = avaliador_dt.calcular_acuracia()
    
    assert acuracia_dt == 1.00
    
def test_modelo_lr():
    caminho_modelo_lr = "./ML/models/lr_mushroom_classifier.pkl"
    modelo_lr = ModeloML(caminho_modelo_lr) 
    avaliador_lr = AvaliadorModelo(modelo_lr,X,y)
    
    acuracia_lr = avaliador_lr.calcular_acuracia()
    
    assert acuracia_lr < 1.00
    
def test_modelo_rf():
    caminho_modelo_rf = "./ML/models/rf_mushroom_classifier.pkl"
    modelo_rf = ModeloML(caminho_modelo_rf) 
    avaliador_rf = AvaliadorModelo(modelo_rf,X,y)
    
    acuracia_rf = avaliador_rf.calcular_acuracia()
    
    assert acuracia_rf == 1.00









