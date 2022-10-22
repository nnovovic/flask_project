import os

from app.util.parse import parse_bool


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = parse_bool(os.environ.get('DEBUG'))
    TESTING = parse_bool(os.environ.get('TESTING'))
