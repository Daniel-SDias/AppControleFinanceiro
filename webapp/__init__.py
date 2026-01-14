from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

DB_NAME = "database.db"
db = SQLAlchemy()


def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    # Inicializa o banco de dados no app
    db.init_app(app)

    # Importa os blueprints
    from .blueprints.home import home_bp
    from .blueprints.transacoes import transacoes_bp
    from .blueprints.dashboard import dashboard_bp

    # Registra os blueprints
    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(transacoes_bp, url_prefix="/transacoes")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

    # Cria o banco de dados se não existir
    from .models import Transaction
    create_db(app)

    return app


def create_db(app):
    if not path.exists("webapp/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Banco de dados criado com sucesso!")
    else:
        print("Banco de dados já existe!")
