# Dentro do arquivo routes.py
from app import app, db
from flask import Flask, jsonify, request
from app.models import Pokemon, Team

# Lista fictícia de times de Pokémon
teams_data = []

@app.route('/api/teams', methods=['GET'])
def get_teams():
    serialized_teams = []
    for index, team_data in enumerate(teams_data):
        team = Team(team_data['username'], team_data['pokemons'])  # Usar a lista direta de Pokémon

        serialized_pokemons = []
        for pokemon in team.pokemons:
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
    team = Team(team_data['username'], team_data['pokemons'])  # Usar a lista direta de Pokémon

    serialized_pokemons = []
    for pokemon in team.pokemons:
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

@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    username = data.get('username')  # Altere 'owner' para 'username' para corresponder ao seu modelo
    pokemons_data = data.get('pokemons')

    if not username or not pokemons_data:
        return jsonify({"error": "Campos obrigatórios em falta"}), 400

    pokemons = []
    for pokemon_data in pokemons_data:
        name = pokemon_data.get('name')
        id = pokemon_data.get('id')
        height = pokemon_data.get('height')
        weight = pokemon_data.get('weight')

        if not name or not id or not height or not weight:
            return jsonify({"error": "Campos de Pokémon em falta"}), 400

        # Crie instâncias de Pokemon com os campos corretos
        pokemon = Pokemon(name=name, id=id, height=height, weight=weight)
        pokemons.append(pokemon)

    # Agora crie a instância de Team com os campos corretos
    team = Team(username=username, pokemons=pokemons)

    # Armazene o time fictício em 'teams_data' (você pode usar um banco de dados em vez disso)
    teams_data.append({"username": username, "pokemons": pokemons})

    # Retorne uma mensagem de validação e a ID única (o índice na lista é uma abordagem simples)
    team_id = len(teams_data) 
    return jsonify({"message": "Time criado com sucesso", "team_id": team_id}), 201