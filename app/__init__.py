from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())
db = SQLAlchemy()
migrate = Migrate()


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.models import Page

    migrate.init_app(app, db, directory='app/migrations')

    from app.blueprints import main, page
    app.register_blueprint(main)
    app.register_blueprint(page)

    return app
