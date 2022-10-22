from app.models import Page


def test_load_page(app, client):
    from app import db

    page = Page(
        title='Test title',
        content='Test body',
        slug='test'
    )

    with app.app_context():
        db.session.add(page)
        db.session.commit()

    r = client.get('/p/test')
    assert 'Test body' in r.text


def test_invalid_slug(app, client):
    r = client.get('/p/invalid')

    assert r.status_code == 404
