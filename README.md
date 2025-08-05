🧠 Meu Primeiro Projeto de IA do Zero
Uma regressão linear implementada 100% do zero, com configuração via .env e execução local

Por: Alves
Tecnologia: Python puro + .env + pickle + matplotlib (opcional)
Objetivo: Criar uma IA real, do zero, sem modelos prontos como ChatGPT ou LLaMA. 

🎯 O Que Este Projeto Faz?
Este projeto implementa um modelo de regressão linear do zero, ou seja:

Não usa scikit-learn, PyTorch ou TensorFlow
Calcula gradientes manualmente
Aprende a partir de dados
Salva e carrega o modelo treinado
É totalmente configurável via .env
Roda localmente em qualquer máquina com Python
🎯 O modelo descobre sozinho a fórmula y ≈ 2x + 1 apenas observando exemplos — como uma IA deveria fazer.

🧱 Arquitetura do Projeto


1
2
3
4
5
6
7
8
9
projeto_ia_alves/
├── .env                   # 🔧 Configurações externas (taxa de aprendizado, épocas, etc)
├── main.py                # 🚀 Ponto de entrada: gera dados, treina e salva o modelo
├── config.py              # ⚙️ Carrega variáveis do .env
├── model.py               # 🧠 Rede neural minimalista: forward, loss, gradiente, treino
├── requirements.txt       # 📦 Dependências do projeto
├── modelo_salvo.pkl       # 💾 Modelo treinado (salvo com pickle)
├── resultado_modelo.png   # 📊 Gráfico do resultado (gerado automaticamente)
└── README.md              # 📖 Este arquivo
🔧 Configurações (via .env)
Tudo é controlado pelo arquivo .env — sem precisar editar o código.

env


1
2
3
4
5
6
7
8
9
10
11
12
13
# Configurações do modelo
EPOCAS=500
TAXA_APRENDIZADO=0.001
TAMANHO_DADOS=100
RUIDO=1.0

# Controle de execução
PLOTAR_GRAFICO=true
VERBOSE=true
SEED=42

# Caminhos
MODELO_SAVE_PATH=modelo_salvo.pkl
✅ Altere aqui para testar diferentes cenários sem tocar no código. 

📦 Dependências
Este projeto usa apenas duas bibliotecas externas:

python-dotenv
Ler o arquivo
.env
matplotlib
Gerar gráficos (opcional)

💡 O núcleo da IA (model.py) é feito em Python puro, sem dependências. 

🚀 Como Executar (Linux)
1. Clone ou crie a pasta do projeto
bash


1
2
cd ~/Documentos
mkdir Desnvovimento_IA && cd Desnvovimento_IA
2. Crie e ative o ambiente virtual
bash


1
2
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências
bash


1
2
pip install --upgrade pip
pip install -r requirements.txt
4. Rode o projeto
bash


1
python main.py
🖥️ Saída Esperada


1
2
3
4
5
6
7
8
9
10
[GERAR] Gerando 100 pontos com ruído ±1.0
[INFO] Iniciando treinamento... w0=0.938, b0=0.853
Época   0 | Loss: 43.7282 | w: 0.938, b: 0.853
Época  50 | Loss: 0.3251 | w: 1.986, b: 0.860
...
Época 450 | Loss: 0.3034 | w: 2.006, b: 0.907
[SUCESSO] Treinamento concluído!
✅ Modelo: y = 2.006x + 0.910
[SAVE] Modelo salvo em modelo_salvo.pkl
[PLOT] Gráfico salvo como 'resultado_modelo.png'
✅ O modelo aprendeu y ≈ 2x + 1
✅ O modelo foi salvo
✅ O gráfico foi gerado como imagem 

📈 Resultado Visual
Após a execução, você verá:

resultado_modelo.png:
Gráfico 1: Dados reais vs. reta aprendida
Gráfico 2: Queda do erro (MSE) ao longo do tempo
📌 Útil para validar que o modelo está aprendendo de verdade. 

💾 Como Salvar e Carregar o Modelo
O modelo é salvo automaticamente com pickle:

python


1
modelo.salvar("modelo_salvo.pkl")
Para carregar depois:

python


1
2
modelo.carregar("modelo_salvo.pkl")
y_previsto = modelo.forward(5)  # Ex: prever y quando x = 5
✅ Ideal para usar o modelo treinado sem precisar treinar de novo. 

🛡️ Boas Práticas Adotadas
Ambiente virtual (
venv
)
Isola dependências
.env
com
python-dotenv
Configuração externa e segura
requirements.txt
Reprodutibilidade
Código modular (
model.py
,
config.py
)
Fácil de entender e evoluir
Gráficos salvos como PNG
Funciona mesmo sem interface gráfica
Seed fixa
Resultados reprodutíveis

🚧 Possíveis Erros e Soluções
ModuleNotFoundError: No module named 'dotenv'
Execute:
pip install python-dotenv
dentro do
venv
matplotlib
não mostra gráficos
O script já salva como PNG — abra o arquivo
resultado_modelo.png
Erro de compilação com
matplotlib
Use:
pip install --only-binary=all matplotlib
Python não encontrado
Instale com:
sudo apt install python3 python3-pip
(Linux)

🚀 Próximos Passos (Ideias para Evoluir)
Este projeto é a base perfeita para construir algo ainda maior. Sugestões:

🔁 Criar uma CLI: python main.py prever 5
🧠 Evoluir para uma rede neural do zero (XOR)
📄 Gerar relatórios em CSV com histórico de treino
🖱️ Interface gráfica simples com tkinter
📦 Gerar um executável com pyinstaller
🌐 Adicionar suporte a dados reais (ex: CSV do Titanic)
📚 Fundamentos Aprendidos
Este projeto ensina os pilares da IA moderna:

📐 Álgebra linear e cálculo (gradientes)
📉 Função de perda (MSE)
🔄 Gradiente descendente
🔁 Treinamento iterativo
💾 Serialização de modelos
🧪 Validação visual e numérica
✅ Tudo isso sem caixas pretas — você controla cada linha. 

🙌 Agradecimentos
Este projeto foi desenvolvido com base em estudos, prática e mentoria consistente.
Você, Alves, está no caminho certo: construindo IA do zero, com entendimento total.

📄 Licença
Este projeto é de código aberto e pode ser usado livremente para estudo, modificação e evolução.
Não há licença restritiva — apenas o compromisso com o aprendizado.# IA_do_Zero
