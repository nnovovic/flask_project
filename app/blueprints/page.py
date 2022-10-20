from flask import Blueprint, render_template

from app import db
from app.models import Page

page = Blueprint('page', __name__, url_prefix='/p')


@page.route('/<string:slug>')
def index(slug: str):
    result = db.session.query(Page).filter(Page.slug == slug).first_or_404()
    return render_template('page/index.html', page=result)
