class Pokemon:
    def __init__(self, name, id, height, weight):
        self.name = name
        self.id = id
        self.height = height
        self.weight = weight
    
    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "height": self.height,
            "weight": self.weight
        }

class Team:
    def __init__(self, username, pokemons):
        self.username = username
        self.pokemons = pokemons
