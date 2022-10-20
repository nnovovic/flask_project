from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
db = SQLAlchemy()


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.models import Page
    with app.app_context():
        db.create_all()

    from app.blueprints import main, page
    app.register_blueprint(main)
    app.register_blueprint(page)

    return app
