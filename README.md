# API de Equipes de Pokémon
Este projeto é uma API de criação e gerenciamento de equipes de Pokémon. Você pode criar equipes fornecendo uma lista de Pokémon e um nome de usuário. Além disso, é possível listar todas as equipes registradas e buscar uma equipe específica por sua ID única. A API é desenvolvida em Flask e utiliza a ```pokeapi.co``` para obter informações sobre os Pokémon.

## Estrutura do Projeto
O projeto está organizado da seguinte forma:
```
project_folder/
    app/
        __init__.py
        models.py
        routes.py
    venv/
    config.py
    run.py
    times.db
```
- **app**: Pasta que contém os arquivos relacionados à sua aplicação Flask.
- **venv**: Pasta que contém o ambiente virtual.
- **config.py**: Arquivo de configuração da aplicação.
- **run.py**: Arquivo para iniciar a aplicação.
- **times.db**: Arquivo de banco de dados

## Módulos
### `__init__.py`

O arquivo `__init__.py` inicializa a aplicação Flask e configura o banco de dados.

### `models.py`

O arquivo models.py define os modelos de dados da aplicação. Aqui estão as principais classes:

#### Team: Representa uma equipe de Pokémon. Possui as seguintes propriedades:

- id: Identificação única da equipe.
- username: Nome do usuário que criou a equipe.
- pokemons: Relação com os Pokémon na equipe.

#### Pokemon: Representa um Pokémon. Possui as seguintes propriedades:

- id: Identificação única do Pokémon.
- name: Nome do Pokémon.
- height: Altura do Pokémon.
- weight: Peso do Pokémon.

### `routes.py`
O arquivo routes.py define as rotas da API e contém a lógica de negócios para criar equipes, listar equipes e buscar equipes por ID. Aqui estão as rotas principais:

- **POST /api/teams**: Cria uma nova equipe de Pokémon. O usuário fornece um nome de usuário e uma lista de nomes de Pokémon.
- **GET /api/teams**: Lista todas as equipes registradas.
- **GET /api/teams/{id}**: Busca uma equipe de Pokémon por ID.

A rota de criação de equipe valida os nomes de Pokémon e busca informações sobre eles na ```pokeapi.co```. Em seguida, armazena os dados no banco de dados.

## Configuração
O arquivo `config.py` contém as configurações da aplicação, como a chave secreta e a URI do banco de dados. 
### Ambiente Virutal de Desenvolvimento
Para desenvolver e executar este projeto, é altamente recomendável configurar um ambiente virtual de desenvolvimento. Isso ajuda a isolar as dependências do projeto e evita conflitos com outras bibliotecas Python em seu sistema. Siga estas etapas para configurar:

1. Instale o Virtualenv (caso ainda não tenha):
```
pip install virtualenv
```
2. Crie um Diretório para o Ambiente Virtual:
```
mkdir venv
```
3. Crie um diretório em seu projeto para armazenar o ambiente virtual. 
```
virutalenv venv
``` 
4. Ative o Ambiente Virtual:

Antes de trabalhar em seu projeto, é necessário ativar o ambiente virtual. Isso isolará as bibliotecas instaladas dentro do ambiente virtual. Use o comando apropriado de acordo com seu sistema operacional:

No Windows:

``` bash
venv\Scripts\activate
```
No macOS e Linux:

```bash
source venv/bin/activate
```
Quando o ambiente virtual estiver ativado, você verá o nome do ambiente virtual no prompt de comando, o que indica que você está trabalhando dentro dele.

5. Instale as Dependências do Projeto:

Com o ambiente virtual ativado, navegue até o diretório do seu projeto (onde o arquivo requirements.txt está localizado) e instale as dependências do projeto com o seguinte comando:

```bash
pip install -r requirements.txt
```
Isso instalará todas as bibliotecas necessárias para executar a aplicação.

6. Desativando o Ambiente Virtual:

Quando você terminar de trabalhar em seu projeto, você pode desativar o ambiente virtual. Basta usar o seguinte comando:

```bash
deactivate
```
Isso restaurará seu ambiente Python para o padrão do sistema.

### Inicialização da Aplicação
Para iniciar a aplicação, execute o arquivo `run.py`. Isso inicializará o servidor de desenvolvimento do Flask.

Certifique-se de criar um ambiente virtual (venv) e instalar todas as dependências antes de executar a aplicação. Você pode fazer isso executando:

```
pip install -r requirements.txt
```

### Uso da API
A API permite que você crie e gerencie equipes de Pokémon. Aqui estão algumas operações que você pode realizar:

#### Criar uma nova equipe de Pokémon
Para criar uma nova equipe, faça uma solicitação POST para /api/teams com os seguintes dados no corpo da solicitação:

``` json
{
  "user": "Nome de Usuário",
  "team": [
    "Pokemon1", 
    "Pokemon2", 
    "Pokemon3",
    "Pokemon4",
    "Pokemon5",
    "Pokemon6"
  ]
}
```

Substitua "Nome de Usuário" pelo nome do usuário que está criando a equipe e "Pokemon1", "Pokemon2", "Pokemon3", "Pokemon4", "Pokemon5" e "Pokemon6" pelos nomes dos Pokémon na equipe.

A API retornará uma mensagem de sucesso junto com a ID única da equipe criada.

### Listar todas as equipes
Para listar todas as equipes registradas, faça uma solicitação GET para /api/teams. A API retornará uma lista de todas as equipes com detalhes dos Pokémon em formato JSON.

### Buscar uma equipe por ID
Para buscar uma equipe específica por sua ID única, faça uma solicitação GET para /api/teams/{id}, onde {id} é a ID da equipe desejada. A API retornará detalhes da equipe, incluindo os Pokémon que a compõem.

## Observações
Certifique-se de configurar corretamente a chave secreta e a URI do banco de dados no arquivo config.py. O projeto utiliza um banco de dados SQLite por padrão.

## Desenvolvedor
Este projeto foi desenvolvido por **Vinícius Brandão Nassif** como parte do desafio da **Triágil** para demonstrar habilidades em desenvolvimento de API e Docker.

