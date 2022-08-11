# Makueni Sand conseration & Utilization Authority
This is a website for the Makueni Sand conseration & Utilization Authority developed under the Python Django Framework

## Live link
Visit the test application on [Heroku](https://makueni-sand-authotiry.herokuapp.com/)


## Features
* Blog Post
* Call to action featues
* User chat section
* User Feedback form


## Prerequisites
Be sure you have the following installed on your development machine:
+ Python >= 3.10
+ Git
+ pip
+ Virtualenv

## Project Installation
To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
virtualenv venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 
```

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),
```bash
mkvirtualenv -p python3 {{project_name}}   # create and activate environment
workon {{project_name}}   # reactivate existing environment
```

Clone GitHub Project,
```bash
https://github.com/KobbyTechnologies/MCSCUA-Website

cd MCSCUA-Website
```

Install development dependencies,
```bash
pip install -r requirements.txt
```

Migrate Database,
```bash
python manage.py migrate
```

Run the web application locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```

Create Superuser,
```bash
python manage.py createsuperuser
```