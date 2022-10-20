from app import db
from app.models import Base


class Page(Base):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=True)
    content = db.Column(db.Text, nullable=True)
    slug = db.Column(db.String(128), nullable=True)
