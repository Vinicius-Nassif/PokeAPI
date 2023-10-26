from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Criação de uma instância Flask
app = Flask(__name__)
# Configura a aplicação com as configurações definidas em Config
app.config.from_object(Config)
# Inicializa o objeto SQLAlchemy associado à aplicação
db = SQLAlchemy()

# Importa as rotas da aplicação a partir do módulo app
from app import routes