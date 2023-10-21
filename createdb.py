from app import app, db

# Importe seus modelos para que o SQLAlchemy saiba sobre eles
from app.models import Team, Pokemon

# Crie o contexto de aplicação Flask
with app.app_context():
    # Crie o banco de dados com base nos modelos
    db.create_all()
