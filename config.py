import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'times.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:
    SECRET_KEY = 'chave_secreta_aqui'