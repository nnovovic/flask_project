# Flask project
This is an example of how to structure a Flask application. It includes a Github Workflow to build and push the container to Docker registry.

### Structure
* app
  * blueprints - Flask blueprints
  * migrations - Flask-Migrate (Alembic) migrations
  * models - Flask-SQLAlchemy models
  * static - static files
  * templates - template files
  * util - utility (helper) functions
  * \_\_init__.py - initialization of our Flask application (create_app function)
* tests
  * blueprints - blueprints tests
  * util - utility functions tests
  * conftest.py - setup pytest fixtures
* .env.example - example configuration file
* .gitignore
* Dockerfile
* requirements.txt
* run.py - run development server
* setup.cfg
* wsgi.py - used by Gunicorn


### Configuration
We use .env file for our configuration variables.


### Packages that are used:
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
* [Gunicorn](https://gunicorn.org/)
* [Python-Dotenv](https://pypi.org/project/python-dotenv/)
* [Pytest](https://docs.pytest.org/en/7.2.x/)

### Continuous integration

#### This repository includes as Github Workflow that is triggered on push to the main branch and does the following
* Install dependencies
* Run tests
* Build docker container
* Push to docker registry

#### Actions secrets
* DOCKERHUB_REPOSITORY
* DOCKERHUB_TOKEN
* DOCKERHUB_USERNAME


