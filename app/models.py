from app import db

# Definição da classe Team
class Team(db.Model):
    # Coluna de identificação
    id = db.Column(db.Integer, primary_key=True)
    # Coluna para o nome de usuário
    username = db.Column(db.String(50), nullable=False)
    # Relação com a tabela Pokemon
    pokemons = db.relationship('Pokemon', back_populates='team')

    # Construtor da classe
    def __init__(self, username, pokemons):
        self.username = username
        self.pokemons = pokemons

    # Método para converter o objeto em um dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "pokemons": [pokemon.to_dict() for pokemon in self.pokemons]
        }

# Definição da classe Pokemon
class Pokemon(db.Model):
    # Coluna para o ID 
    id = db.Column(db.Integer, primary_key=True)
    # Coluna para o nome do Pokémon
    name = db.Column(db.String(50), nullable=False)
    # Coluna para a altura do Pokémon
    height = db.Column(db.Integer, nullable=False)
    # Coluna para o peso do Pokémon
    weight = db.Column(db.Integer, nullable=False)
    # Coluna de chave estrangeira para relacionamento com a classe Team
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    # Relação com a classe Team
    team = db.relationship('Team', back_populates='pokemons')

    # Construtor da classe
    def __init__(self, id, name, height, weight):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight

    # Método para converter o objeto em um dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight
        }