from app import app, db

# Importa os modelos Team e Pokemon para que o SQLAlchemy saiba sobre eles
from app.models import Team, Pokemon

# Cria o contexto de aplicação Flask
with app.app_context():
    # Cria o banco de dados com base nos modelos Team e Pokemon
    db.create_all()