from app import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)

    # Relação com a tabela Pokemon
    pokemons = db.relationship('Pokemon', back_populates='team')

    def __init__(self, username, pokemons):
        self.username = username
        self.pokemons = pokemons

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "pokemons": [pokemon.to_dict() for pokemon in self.pokemons]
        }

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    # Adicione uma coluna de chave estrangeira para relacionar com Team
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.relationship('Team', back_populates='pokemons')

    def __init__(self, id, name, height, weight):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight
        }