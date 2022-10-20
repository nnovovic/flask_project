import os


class Config:
    APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    BASE_DIR = os.path.dirname(APP_DIR)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_NAME = 'sid'
