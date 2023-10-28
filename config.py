import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    database_file = os.path.join(basedir, 'times.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{database_file}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    