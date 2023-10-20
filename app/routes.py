# Dentro do arquivo routes.py
from app import app
from flask import Flask,jsonify, request
from app.models import Pokemon, Team

# Lista fictícia de times de Pokémon
teams_data = []

@app.route('/api/teams', methods=['GET'])
def get_teams():
    serialized_teams = []
    for index, team_data in enumerate(teams_data):
        pokemons = [Pokemon(p['name'], p['id'], p['height'], p['weight']) for p in team_data['pokemons']]
        team = Team(team_data['username'], pokemons)

        serialized_pokemons = []
        for pokemon in pokemons:
            serialized_pokemons.append({
                "id": pokemon.id,
                "name": pokemon.name,
                "weight": pokemon.weight,
                "height": pokemon.height
            })

        serialized_team = {
            "owner": team_data['username'],
            "pokemons": serialized_pokemons
        }

        serialized_teams.append(serialized_team)

    return jsonify(serialized_teams)


@app.route('/api/teams/<int:id>', methods=['GET'])
def get_team_by_id(id):
    if id < 0 or id >= len(teams_data):
        return jsonify({"error": "Time não encontrado"}), 404
    team_data = teams_data[id]
    pokemons = [Pokemon(p['name'], p['id'], p['height'], p['weight']) for p in team_data['pokemons']]
    team = Team(team_data['username'], pokemons)

    serialized_pokemons = []
    for pokemon in pokemons:
        serialized_pokemons.append({
            "id": pokemon.id,
            "name": pokemon.name,
            "weight": pokemon.weight,
            "height": pokemon.height
        })

    serialized_team = {
        "owner": team_data['username'],
        "pokemons": serialized_pokemons
    }

    return jsonify(serialized_team)



# Rota POST /api/teams
@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    username = data.get('username')
    pokemons = data.get('pokemons')

    if not username or not pokemons:
        return jsonify({"error": "Campos obrigatórios em falta"}), 400

    # Lógica para solicitar dados da pokeapi.co para cada Pokémon na lista
    # Armazenar dados dos Pokémon em uma lista chamada 'pokemon_data'
    pokemon_data = []  # Substitua por dados reais da pokeapi.co

    if 'error' in pokemon_data:
        return jsonify({"error": "Erro ao buscar informações dos Pokémons"}), 500

    # Armazene o time fictício em 'teams_data' (você pode usar um banco de dados em vez disso)
    teams_data.append({"username": username, "pokemons": pokemons})

    # Retorne uma mensagem de validação e a ID única (o índice na lista é uma abordagem simples)
    team_id = len(teams_data) - 1
    return jsonify({"message": "Time criado com sucesso", "team_id": team_id}), 201
