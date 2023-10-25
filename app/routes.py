from app import app, db
from flask import Flask, jsonify, request
from flask_json import FlaskJSON
from app.models import Pokemon, Team
import requests

# Função para buscar informações sobre um Pokémon na pokeapi.co
def get_pokemon_info(pokemon_name, offset=0, limit=10):
    # URL base da pokeapi.co
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    # Monta a URL completa para buscar informações do Pokémon com paginação
    url = f"{base_url}{pokemon_name}/?offset={offset}&limit={limit}"

    try:
        # Cria uma uma sessão em cada interação, permitindo que a conexão seja mantida aberta
        # Faz uma solicitação GET para a pokeapi.co
        session = requests.Session()
        response = session.get(url)

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
    
@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    username = data.get('user')
    pokemon_names = data.get('team')

    if not username or not pokemon_names:
        return jsonify({"error": "Campos obrigatórios em falta"}), 400

    pokemons = []
    for name in pokemon_names:
        # Busca o Pokémon pelo nome no banco de dados
        existing_pokemon = Pokemon.query.filter_by(name=name).first()

        if existing_pokemon:
            # Se o Pokémon já existe, apenas o associe à equipe
            pokemons.append(existing_pokemon)
        else:
            # Obtenha as informações do Pokémon a partir da pokeapi.co
            pokemon_info = get_pokemon_info(name)

            if 'error' in pokemon_info:
                return jsonify(pokemon_info), 400

            # Preencha os campos do Pokémon com as informações obtidas
            pokemon_id = pokemon_info['id']
            height = pokemon_info['height']
            weight = pokemon_info['weight']

            # Crie uma nova instância de Pokemon e adicione ao banco de dados
            new_pokemon = Pokemon(name=name, height=height, weight=weight, id=pokemon_id)
            db.session.add(new_pokemon)
            pokemons.append(new_pokemon)

    team = Team(username=username, pokemons=pokemons)
    db.session.add(team)
    db.session.commit()

    # Retorna uma mensagem de validação e a ID única (o índice na lista é uma abordagem simples)
    return jsonify({"message": "Time criado com sucesso", "team_id": team.id}), 201

@app.route('/api/teams', methods=['GET'])
def get_teams():
    # Consulta todos os times no banco de dados
    teams = Team.query.all()
    
    # Dicionário para armazenar times serializados com índices
    serialized_teams_with_index = {}

    # Inicialize o índice
    index = 1

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

        # Associe o time serializado ao índice no dicionário
        serialized_teams_with_index[index] = serialized_team

        # Incrementar o índice
        index += 1

    # Retorna o dicionário com os times serializados com índices como uma resposta JSON usando jsonify
    return jsonify(serialized_teams_with_index)

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

    # Retorna o time serializado como uma resposta JSON usando jsonify
    return jsonify(serialized_team)