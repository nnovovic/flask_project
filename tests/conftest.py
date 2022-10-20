import pytest
from app import create_app
from app.config import TestingConfig


@pytest.fixture()
def app():
    app = create_app(TestingConfig)

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
