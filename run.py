from app import app, db

def main():
    # Inicializa o objeto SQLAlchemy associado à aplicação
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Inicia o servidor de desenvolvimento do Flask com depuração ativada
    app.run(debug=True)

if __name__ == '__main__':
    main()