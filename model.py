# model.py
import random
import pickle

class RegressaoLinear:
    def __init__(self):
        self.w = random.uniform(-1, 1)
        self.b = random.uniform(-1, 1)
        self.historico_loss = []

    def forward(self, x):
        """Faz a previsão: y = w*x + b"""
        return self.w * x + self.b

    def calcular_mse(self, dados):
        erro_total = 0.0
        for x, y_real in dados:
            y_pred = self.forward(x)
            erro_total += (y_real - y_pred) ** 2
        return erro_total / len(dados)

    def gradiente_descendente(self, dados, taxa_aprendizado):
        m = len(dados)
        grad_w = 0.0
        grad_b = 0.0

        for x, y_real in dados:
            y_pred = self.forward(x)
            erro = y_real - y_pred

            grad_w += -2 * x * erro / m
            grad_b += -2 * erro / m

        self.w -= taxa_aprendizado * grad_w
        self.b -= taxa_aprendizado * grad_b

    def treinar(self, dados, epocas, taxa_aprendizado, verbose=True):
        if verbose:
            print(f"[INFO] Iniciando treinamento... w0={self.w:.3f}, b0={self.b:.3f}")

        for i in range(epocas):
            loss = self.calcular_mse(dados)
            self.historico_loss.append(loss)

            if verbose and i % 50 == 0:
                print(f"Época {i:3d} | Loss: {loss:.4f} | w: {self.w:.3f}, b: {self.b:.3f}")

            self.gradiente_descendente(dados, taxa_aprendizado)

        if verbose:
            print(f"[SUCESSO] Treinamento concluído!")
            print(f"✅ Modelo: y = {self.w:.3f}x + {self.b:.3f}")

    def salvar(self, caminho):
        """Salva o modelo com pickle"""
        modelo_data = {
            'w': self.w,
            'b': self.b,
            'historico_loss': self.historico_loss
        }
        with open(caminho, 'wb') as f:
            pickle.dump(modelo_data, f)
        print(f"[SAVE] Modelo salvo em {caminho}")

    def carregar(self, caminho):
        """Carrega o modelo salvo"""
        with open(caminho, 'rb') as f:
            modelo_data = pickle.load(f)
        self.w = modelo_data['w']
        self.b = modelo_data['b']
        self.historico_loss = modelo_data['historico_loss']
        print(f"[LOAD] Modelo carregado de {caminho}")