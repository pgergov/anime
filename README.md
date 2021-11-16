# Anime movies search application

## Minimum System Requirements

* Python 3.9.0
* PostgreSQL 13

## How to install locally

If you've went through the setup at least once do:

```bash
./utility/bootstrap.sh <username>
```

### Add virtual environment with Python 3.9.0

* Install pyenv <https://github.com/pyenv/pyenv>
* Install pyenv-update <https://github.com/pyenv/pyenv-update>
* Install pyenv-virtualenv <https://github.com/pyenv/pyenv-virtualenv>

```bash
pyenv update
pyenv install 3.9.0
pyenv virtualenv 3.9.0 anime-3.9.0
pyenv activate anime-3.9.0
pip install -r requirements/local.txt
```

### Create PostgreSQL database

* Install PostgreSQL <https://www.postgresql.org/download/linux/>

```bash
sudo -u postgres createdb -O <your-username> anime
python manage.py migrate
```

### How to run locally

Run the server:

```bash
python manage.py runserver
```

Run the tests:

```bash
py.test
```

### Setup hooks

```bash
pre-commit install
```

The project is using:

* [Flake8](https://flake8.pycqa.org/en/latest/) for linting
* [Black](https://github.com/psf/black) for code formatting
* [Isort](https://github.com/PyCQA/isort) for consistent imports
* [MyPy](https://github.com/pre-commit/mirrors-mypy) for type checking

## CI

GitHub actions is used for continuous integration. For reference https://docs.github.com/en/actions/guides/building-and-testing-python

Each commit, in every branch, triggers test & linting build.
