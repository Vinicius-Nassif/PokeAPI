from app import db
from collections import OrderedDict

# Definição da classe TeamPokemonAssociation para a tabela de associação entre equipes e Pokémon
class TeamPokemonAssociation(db.Model):
    __tablename__ = 'team_pokemon_association'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))

    def __init__(self, team_id, pokemon_id):
        self.team_id = team_id
        self.pokemon_id = pokemon_id
 
# Definição da classe Team
class Team(db.Model):
    # Coluna de identificação
    id = db.Column(db.Integer, primary_key=True)
    # Coluna para o nome de usuário
    username = db.Column(db.String(50), nullable=False)
    # Relação com a tabela team_pokemon_association
    pokemons = db.relationship('Pokemon', secondary=TeamPokemonAssociation.__tablename__, back_populates='teams')

    # Construtor da classe
    def __init__(self, username, pokemons):
        self.username = username
        self.pokemons = pokemons

    # Método para converter o objeto em um dicionário
    def to_dict(self):
        return OrderedDict({
            "id": self.id,
            "username": self.username,
            "pokemons": [pokemon.to_dict() for pokemon in self.pokemons]
        })

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
    # Relação com a classe Team e tabela team_pokemon_association
    teams = db.relationship('Team', secondary=TeamPokemonAssociation.__tablename__, back_populates='pokemons')

    # Construtor da classe
    def __init__(self, id, name, height, weight):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight

    # Método para converter o objeto em um dicionário
    def to_dict(self):
        return OrderedDict({
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight
        })
    