from app import app, db
from flask import Flask, jsonify, request
from app.models import Pokemon, Team
import requests

# Função para buscar informações sobre um Pokémon na pokeapi.co
def get_pokemon_info(pokemon_name):
    # URL base da pokeapi.co
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    # Monta a URL completa para buscar informações do Pokémon
    url = f"{base_url}{pokemon_name}/"

    try:
        # Faz uma solicitação GET para a pokeapi.co
        response = requests.get(url)

        if response.status_code == 200:
            # Converte os dados da resposta em JSON
            data = response.json()

            # Verifica se os campos necessários estão presentes
            if 'id' in data and 'height' in data and 'weight' in data:
                pokemon_id = data['id']
                height = data['height']
                weight = data['weight']
                return {"id": pokemon_id, "name": pokemon_name, "height": height, "weight": weight}
            else:
                return {"error": "Dados incompletos na resposta da pokeapi.co"}, 400
        elif response.status_code == 404:
            return {"error": f"Não foi possível encontrar informações para o Pokémon {pokemon_name}"}, 404
        elif response.status_code == 429:
            return {"error": "Limite de solicitações atingido. Tente novamente mais tarde."}, 429
        else:
            return {"error": "Erro desconhecido na solicitação à pokeapi.co"}, 500
    except requests.exceptions.RequestException as e:
        return {"error": "Erro na solicitação à pokeapi.co. Verifique sua conexão de rede."}, 500
    
# Rota para criar um novo time
@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    username = data.get('username')
    pokemons_data = data.get('pokemons')

    if not username or not pokemons_data:
        return jsonify({"error": "Campos obrigatórios em falta"}), 400

    pokemons = []
    for pokemon_data in pokemons_data:
        name = pokemon_data.get('name')

        # Chama a função get_pokemon_info para obter informações do Pokémon
        pokemon_info = get_pokemon_info(name)

        if 'error' in pokemon_info:
            return jsonify(pokemon_info), 400

        # Preenche os campos do Pokémon com as informações obtidas
        pokemon_id = pokemon_info['id']
        height = pokemon_info['height']
        weight = pokemon_info['weight']

        # Cria uma instância de Pokemon com os campos corretos
        new_pokemon = Pokemon(name=name, height=height, weight=weight, id=pokemon_id)
        pokemons.append(new_pokemon)

    team = Team(username=username, pokemons=pokemons)
    db.session.add(team)
    db.session.commit()

    # Retorna uma mensagem de validação e a ID única (o índice na lista é uma abordagem simples)
    return jsonify({"message": "Time criado com sucesso", "team_id": team.id}), 201

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