# Authentication & Production Server

## Author: Davee Sok

## Links & Resources

- [Davee's Django API Template](https://github.com/daveeS987/template-davees-django-api)

## Overview

Add authentication and switch to a production server

## Feature Tasks and Requirements

Features - Django

- Add JWT Authentication to your API.
  - Install needed libraries in project configuration and/or site settings.
- Keep any pre-existing authentication so DRF Browsable API still usable.
  - Install needed libraries in project configuration and/or site settings.

Features - Docker

- Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.
  - E.g. as a VS Code snippet, or a gist.
- Switch to using Gunicorn instead of Django’s built in development server.
  - mind the number of workers to avoid sluggishness

## How to run server and test routes

Run the following to start docker:

```iterm
docker-compose up
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

- Create super user
- go to localhost:8000/admin and create users and dummy data
- log out

- Sign in with http to token route. This will give us access and refresh tokens

```iterm
http POST :8000/api/token/ email='admin@gmail.com' password='admin'
```

- Use access token to go to certain routes

```iterm
http GET :8000/api/v1/movie/ 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'

# Gets One Item with pk=1
http GET :8000/api/v1/movie/1 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'

# Deletes One Item with pk=2
http DELETE :8000/api/v1/movie/2 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'
```

### Collaborators

Daniel Dills, Prabin Singh, Wondwosen Tsige, Michael Ryan, Garfield Grant
