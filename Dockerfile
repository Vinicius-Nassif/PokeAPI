# Descreve como a aplicação Flask será empocatada em um contêiner Docker.
# Use a imagem base do Python 3.8
FROM python:3.8

# Define a variável de ambiente PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1

# Configuração do diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do projeto para o contêiner
COPY . /app/

# Exponha a porta que a aplicação Flask irá escutar
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "run.py"]
