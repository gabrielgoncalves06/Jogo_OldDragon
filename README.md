Gerador de Personagens Old Dragon (Projeto Flask)
Este é um projeto web desenvolvido em Python com o framework Flask. A aplicação permite criar fichas de personagem para o RPG Old Dragon, seguindo as regras do livro para geração de atributos, seleção de raças e classes.

🚀 Principais Recursos e Últimas Atualizações
O sistema foi atualizado para incluir persistência de dados. Agora, cada personagem criado é salvo automaticamente de duas formas diferentes:

Salvamento em Arquivo JSON:

Cada personagem é salvo como um arquivo .json individual, contendo todos os seus dados (atributos, raça, classe, etc.).

Localização: Os arquivos JSON são armazenados na pasta /saves/, localizada na raiz do projeto.

Conexão com Banco de Dados MongoDB:

O projeto também salva os dados principais de cada personagem em um banco de dados NoSQL (MongoDB).

A lógica de conexão e inserção está no arquivo jogo/gerenciadobd.py.

📂 Estrutura do Projeto
A arquitetura do projeto segue uma organização modular, separando a lógica de negócio (Model) das rotas da aplicação (Controller).

Python_oldDragon/
├── jogo/                  # Pacote principal da aplicação
│   ├── __init__.py
│   ├── app.py             # Controller: Rotas Flask e lógica da aplicação
│   ├── gerenciadobd.py    # Lógica de conexão com o MongoDB
│   ├── gerenciador_save.py  # Lógica para salvar em JSON
│   │
│   ├── model/             # Model: Contém as regras de negócio
│   │   ├── componentes/
│   │   │   ├── dado.py
│   │   │   └── gerador_atributos.py
│   │   │
│   │   ├── racas/
│   │   │   ├── anao.py
│   │   │   ├── elfo.py
│   │   │   └── humano.py
│   │   │
│   │   └── classes_personagem/
│   │       ├── guerreiro.py
│   │       ├── mago.py
│   │       ├── ladrao.py
│   │       └── personagem.py
│   │
│   ├── static/            # Arquivos estáticos (CSS, Imagens)
│   │   └── style.css
│   │
│   └── templates/         # Views: Arquivos HTML (Jinja2)
│       ├── index.html
│       ├── distribuir.html
│       └── resultado.html
│
├── saves/                 # <-- DESTINO DOS SAVES EM JSON
│   └── (personagens.json são criados aqui)
│
├── venv/                  # Ambiente virtual do Python
└── requirements.txt       # Lista de dependências (Flask, PyMongo)
🛠️ Como Executar o Projeto
Clone o repositório:

Bash

git clone [URL_DO_SEU_REPOSITORIO]
cd Python_oldDragon
Crie e ative um ambiente virtual:

PowerShell

# Criar o ambiente
python -m venv venv
# Ativar o ambiente (Windows PowerShell)
.\venv\Scripts\Activate
Instale as dependências: (Certifique-se de ter o arquivo requirements.txt atualizado)

Bash

pip install -r requirements.txt
Se não tiver o arquivo, instale manualmente:

Bash

pip install flask pymongo
Configure o MongoDB:

Abra o arquivo jogo/gerenciadobd.py.

Insira sua string de conexão do MongoDB (local ou do Atlas) na variável MONGO_URI.

Inicie o servidor Flask: (No terminal PowerShell, a partir da pasta Python_oldDragon)

PowerShell

# Define o arquivo da aplicação
$env:FLASK_APP = "jogo.app"
# Inicia o servidor em modo de desenvolvimento
flask run
Abra seu navegador e acesse http://127.0.0.1:5000.
