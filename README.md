# DjangoRest

## How to setup Django Rest 

```
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
py -m venv env
On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..

```

Sync your database first time

```
py manage.py makemigrations
py manage.py migrate
```