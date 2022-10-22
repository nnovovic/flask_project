from os import path

from app.util.paths import app_dir, base_dir


def test_app_dir():
    assert path.join(path.abspath(path.dirname(path.dirname(path.dirname(__file__)))), 'app') == app_dir()


def test_base_dir():
    assert path.abspath(path.dirname(path.dirname(path.dirname(__file__)))) == base_dir()