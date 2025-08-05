# config.py
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

# Agora podemos acessar com os.getenv("VARIAVEL")
class Config:
    # Treinamento
    EPOCAS = int(os.getenv("EPOCAS", 500))
    TAXA_APRENDIZADO = float(os.getenv("TAXA_APRENDIZADO", 0.001))
    TAMANHO_DADOS = int(os.getenv("TAMANHO_DADOS", 100))
    RUIDO = float(os.getenv("RUIDO", 1.0))

    # Controle
    PLOTAR_GRAFICO = os.getenv("PLOTAR_GRAFICO", "true").lower() == "true"
    VERBOSE = os.getenv("VERBOSE", "true").lower() == "true"
    SEED = int(os.getenv("SEED", 42))

    # Caminhos
    MODELO_SAVE_PATH = os.getenv("MODELO_SAVE_PATH", "modelo_salvo.pkl")