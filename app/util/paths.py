from os import path


def app_dir() -> str:
    return path.abspath(path.dirname(path.dirname(__file__)))


def base_dir() -> str:
    return path.dirname(app_dir())
