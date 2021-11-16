#!/bin/bash

# Bootstrap script for local development. Does the following:
# 1. Creates/resets the database
# 2. Installs requirements
# 3. Runs migrations
# 4. Sets up pre-commit hooks

E_NO_POSTGRES_USERNAME=60
POSTGRES_USERNAME="$1"
DATABASE_NAME="anime"

if [[ -z "$POSTGRES_USERNAME" ]]
then
  echo "Call `basename $0` with your postgres user as the first argument."
  exit "$E_NO_POSTGRES_USERNAME"
fi

echo "Dropping database $DATABASE_NAME ..."
dropdb --if-exists "$DATABASE_NAME"

echo "Creating database $DATABASE_NAME ..."
sudo -u postgres createdb -O "$POSTGRES_USERNAME" "$DATABASE_NAME"

echo "Installing requirements ..."
pip install -r requirements/local.txt

echo "Running migrations ..."
python manage.py migrate

echo "Setting pre-commit hooks ..."
pre-commit install

echo "Bootstrap done."
