from app import app, db

def main():
    # Inicializa o objeto SQLAlchemy associado à aplicação
    db.init_app(app)

    try:
        # Criar o banco de dados antes da primeira requisição
        with app.app_context():
            db.create_all()
        print('Banco de dados criado com sucesso!')
    except Exception as e:
        print('Utilizando banco de dados existente!', e)
        pass

    # Inicia o servidor de desenvolvimento do Flask com depuração ativada
    app.run(debug=True)

if __name__ == '__main__':
    main()