from app import app, db

if __name__ == '__main__':
    # Inicializa o objeto SQLAlchemy associado à aplicação
    db.init_app(app)

    # Função para criar o banco de dados antes da primeira requisição
    with app.app_context():
        db.create_all()

    # Inicia o servidor de desenvolvimento do Flask com depuração ativada
    app.run(debug=True)