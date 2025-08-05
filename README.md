# 🧠 Meu Primeiro Projeto de IA do Zero  
**Regressão Linear Implementada 100% do Zero com Configuração via `.env`**

> **Autor:** Alves  
> **Tecnologia:** Python puro + `.env` + `pickle` + `matplotlib` (opcional)  
> **Objetivo:** Criar uma IA real do zero, sem depender de modelos prontos como ChatGPT, LLaMA ou frameworks como TensorFlow/PyTorch.  
> \#IA_do_Zero \#MachineLearning \#FromScratch

---

## 🎯 O Que Este Projeto Faz?

Este projeto implementa um **modelo de regressão linear completamente do zero**, com:

- ✅ Cálculo manual de **gradientes** e **função de perda (MSE)**
- ✅ **Treinamento via gradiente descendente**
- ✅ Configuração via arquivo `.env`
- ✅ Ambiente virtual isolado (`venv`)
- ✅ Serialização do modelo com `pickle`
- ✅ Geração automática de gráficos (salvos como PNG)

🎯 O modelo aprende sozinho a relação `y ≈ 2x + 1` a partir de dados sintéticos — **sem nenhuma ajuda explícita**.

---

## 🏗️ Arquitetura do Projeto

´´
projeto_ia_alves/
├── .env # 🔧 Configurações externas
├── main.py # 🚀 Ponto de entrada: gera dados, treina, salva
├── config.py # ⚙️ Carrega variáveis do .env
├── model.py # 🧠 Implementação do modelo (neurônio, treino, predição)
├── requirements.txt # 📦 Dependências
├── modelo_salvo.pkl # 💾 Modelo treinado (salvo com pickle)
├── resultado_modelo.png # 📊 Gráfico gerado automaticamente
└── README.md # 📖 Este arquivo
´´