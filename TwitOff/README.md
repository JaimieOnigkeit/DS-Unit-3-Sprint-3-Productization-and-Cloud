# Installation
```sh
git clone git@github.com:JaimieOnigkeit/DS-Unit-3-Sprint-3-Productization-and-Cloud
cd TwitOff
```

# Setup
```sh
pipenv install
```

# Migrate the db:
```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```

# Usage
## Mac:
```sh
FLASK_APP=web_app flask run
```
## Windows:
```sh
export FLASK_APP=web_app # one-time thing, to set the env var
flask run
```