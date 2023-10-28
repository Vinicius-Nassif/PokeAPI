import os
from app import app, db

def main():
    # Inicializa o objeto SQLAlchemy associado à aplicação
    db.init_app(app)
    
    # Verifica se o arquivo do banco de dados já existe
    db_file = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///','')
    if not os.path.exists(db_file):
        with app.app_context():
            db.create_all()
            print('Banco de dados criado com sucesso!')
    else:
        print('O arquivo do banco de dados já existe.')

    # Inicia o servidor de desenvolvimento do Flask com depuração ativada
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()
