from sqlalchemy import func
from sqlalchemy.orm import declared_attr

from app import db


class Base(db.Model):
    __abstract__ = True

    @declared_attr
    def date_created(cls):
        return db.Column(db.DateTime(timezone=True), default=func.now())

    @declared_attr
    def date_modified(cls):
        return db.Column(db.DateTime(timezone=True), onupdate=func.now(), default=func.now())
