# main.py
import random
import matplotlib.pyplot as plt
from config import Config
from model import RegressaoLinear

def gerar_dados(n, ruido):
    dados = []
    for _ in range(n):
        x = random.uniform(-10, 10)
        y = 2 * x + 1 + random.uniform(-ruido, ruido)
        dados.append((x, y))
    return dados

def plotar_resultados(dados, modelo):
    xs = [x for x, y in dados]
    ys = [y for x, y in dados]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(xs, ys, alpha=0.6, label="Dados")
    plt.plot(xs, [modelo.forward(x) for x in xs], 'r-', label=f"y = {modelo.w:.2f}x + {modelo.b:.2f}")
    plt.title("Modelo Aprendido")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.plot(modelo.historico_loss, 'b-', label="Loss (MSE)")
    plt.title("Evolução do Erro")
    plt.xlabel("Épocas")
    plt.ylabel("Loss")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Definir seed para reprodutibilidade
    random.seed(Config.SEED)

    # Gerar dados
    print(f"[GERAR] Gerando {Config.TAMANHO_DADOS} pontos com ruído ±{Config.RUIDO}")
    dados = gerar_dados(Config.TAMANHO_DADOS, Config.RUIDO)

    # Criar e treinar modelo
    modelo = RegressaoLinear()
    modelo.treinar(dados, Config.EPOCAS, Config.TAXA_APRENDIZADO, verbose=Config.VERBOSE)

    # Salvar modelo
    modelo.salvar(Config.MODELO_SAVE_PATH)

    # Plotar se habilitado
    if Config.PLOTAR_GRAFICO:
        try:
            plotar_resultados(dados, modelo)
        except Exception as e:
            print(f"[ERRO] Falha ao plotar: {e}")