import pytest

from app import create_app, db


@pytest.fixture()
def app():
    mp = pytest.MonkeyPatch()
    mp.setenv('TESTING', 'True')
    mp.setenv('FLASK_SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')

    app = create_app()

    with app.app_context():
        db.create_all()

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
