                    
                    # Turivius-Code-Challenge

## This is a code challenge as part of the Turivius recruitment process

### In this code challenge I'm developing a couple of apps as 2 different microservices where one is a django admin and the other one where is a django rest api app for consuming a manually populated json database, with sql and orm for data persistence, having to finally to render the results to a webpage. As extra efforts, I'm creating a helpful and organized readme file and dockerize this project making sure it works equally in any computer which supports and contains docker installed.

#### Required Stack:
- Python
- Django Framework
- Django REST Framework
- Bokeh Library
- SQL

How it's being built:

- $ mkdir <project_name>
- $ cd <project-name>
- $ python3 -m venv <venv_name>
- $ source <venv_name>/bin/activate
- $ pip install django
- $ django-admin startproject <project_name>
- $ python manager.py runserver
- $ pytho manage.py startapp <app_name>
- Create the models
- Registered the models
- Created super user
- $ pip install djangorestframework
- Created serializers module
- Created views/ViewSet
- Configured urls
- populated with a json file
- $ python manage.py loaddata <json_file_name>
- Dockerfile
- $ docker build .
- docker-compose.yml
- $ docker-compose build
- run the container $ docker-compose up -d
- Bokeh counter and graph rendering


# Endpoints for GET, POST, PUT and DELETE:

- /lawsuits
- /lawsuits/id
- /admin
- /admin/court_app/lawsuit/
- /status


# References:

- https://www.djangoproject.com/
- https://www.django-rest-framework.org/tutorial/quickstart/#serializers
- https://www.youtube.com/watch?v=BKChTO8GADk
- https://docs.djangoproject.com/en/3.0/howto/initial-data/#providing-data-with-fixtures
- https://docs.djangoproject.com/en/3.0/topics/serialization/
- https://code.djangoproject.com/wiki/Fixtures
- https://howtojsonapi.com/django.html
- https://forum.djangoproject.com/t/getting-a-deserializationerror-when-trying-to-load-data-from-json-to-db/2713
- https://stackoverflow.com/questions/54617353/django-deserialization-error-problem-installing-fixture
- https://medium.com/@beatrizuezu/visualizando-query-sql-a-partir-do-orm-django-5771370a9c55
- https://github.com/beatrizuezu/de-sql-para-orm-django/tree/master/core/categorias
- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
- https://docs.docker.com/engine/reference/builder/
- https://github.com/theyogicoderRI/DjangoInchByInch/blob/master/Data%20Visualization%20Django%20And%20Bokeh/views.py
- https://github.com/cryptopotluck/plotly-dash-django-udemy/blob/master/home/views.py
- https://www.django-rest-framework.org/api-guide/renderers/
- https://hackernoon.com/integrating-bokeh-visualisations-into-django-projects-a1c01a16b67a
