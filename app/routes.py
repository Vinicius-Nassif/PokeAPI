from app import app, db
from flask import Flask, jsonify, request
from app.models import Pokemon, Team

# Rota para obter todos os times
@app.route('/api/teams', methods=['GET'])
def get_teams():
    # Lista para armazenar times serializados
    serialized_teams = []
    # Consulta todos os times no banco de dados
    teams = Team.query.all()

    for team in teams:
        # Lista para armazenar Pokémon serializados
        serialized_pokemons = []
        for pokemon in team.pokemons:
            # Serializa os dados do Pokémon
            serialized_pokemons.append({
                "id": pokemon.id,
                "name": pokemon.name,
                "weight": pokemon.weight,
                "height": pokemon.height
            })

        # Serializa os dados do time
        serialized_team = {
            "owner": team.username,
            "pokemons": serialized_pokemons
        }

        # Adiciona o time serializado à lista
        serialized_teams.append(serialized_team)

    # Retorna os times serializados como uma resposta JSON
    return jsonify(serialized_teams)

# Rota para obter um time por ID
@app.route('/api/teams/<int:id>', methods=['GET'])
def get_team_by_id(id):
    team = Team.query.get(id)

    if not team:
        return jsonify({"error": "Time não encontrado"}), 404

    # Lista para armazenar Pokémon serializados
    serialized_pokemons = []
    for pokemon in team.pokemons:
        # Serializa os dados do Pokémon
        serialized_pokemons.append({
            "id": pokemon.id,
            "name": pokemon.name,
            "weight": pokemon.weight,
            "height": pokemon.height
        })

    # Serializa os dados do time
    serialized_team = {
        "owner": team.username,
        "pokemons": serialized_pokemons
    }

    # Retorna o time serializado como uma resposta JSON
    return jsonify(serialized_team)

# Rota para criar um novo time
@app.route('/api/teams', methods=['POST'])
def create_team():
    # Obtém os dados da solicitação em formato JSON
    data = request.get_json()
    # Extrai o nome de usuário e os dados dos Pokémon da solicitação
    username = data.get('username')  # Altere 'owner' para 'username' para corresponder ao seu modelo
    pokemons_data = data.get('pokemons')

    # Verifica se os campos obrigatórios estão presentes
    if not username or not pokemons_data:
        return jsonify({"error": "Campos obrigatórios em falta"}), 400

    # Lista para armazenar instâncias de Pokémon
    pokemons = []
    for pokemon_data in pokemons_data:
        # Extrai os campos do Pokémon
        name = pokemon_data.get('name')
        height = pokemon_data.get('height')
        weight = pokemon_data.get('weight')

        # Verifica se os campos do Pokémon estão presentes
        if not name or not height or not weight:
            return jsonify({"error": "Campos de Pokémon em falta"}), 400

        # Cria instâncias de Pokemon com os campos corretos
        pokemon = Pokemon(name=name, height=height, weight=weight)
        pokemons.append(pokemon)

    # Cria uma instância de Team com os campos corretos
    team = Team(username=username, pokemons=pokemons)

    # Adiciona o time à sessão
    db.session.add(team)
    db.session.commit()

    # Retorna uma mensagem de validação e a ID única (o índice na lista é uma abordagem simples)
    return jsonify({"message": "Time criado com sucesso", "team_id": team.id}), 201
