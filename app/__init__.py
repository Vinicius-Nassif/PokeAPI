from flask import Flask
from config import Config, SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy

# Criação de uma instância Flask
app = Flask(__name__)
# Configura a aplicação com as configurações definidas em Config
app.config.from_object(Config)
# Configura a URI do banco de dados a partir do arquivo de configuração
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# Inicializa o objeto SQLAlchemy associado à aplicação
db = SQLAlchemy(app)

# Importa as rotas da aplicação a partir do módulo app
from app import routes