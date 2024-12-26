# Vidly - Movie Rental Service

A Django web application for managing a movie rental service. View the live demo at [https://django-vidly.onrender.com](https://django-vidly.onrender.com) (Note: Initial load may take up to 2 minutes as the service spins up).

![image](https://github.com/user-attachments/assets/dc0728fb-cfcf-4513-badb-128891cf183a)

## Features

- Browse available movies with their details
- View movie information including title, genre, stock, and daily rate
- RESTful API for accessing movie data
- Admin interface for managing movies and genres

## Tech Stack

- Django 5.1.4
- Django Tastypie (for REST API)
- WhiteNoise (for static file serving)
- Bootstrap 5.3.3
- SQLite (Database)
- Gunicorn (Production server)

## Project Structure

The project consists of two main Django apps:

- `movies`: Handles the movie listing and detail views
- `api`: Provides REST API endpoints for movie data

## Local Development

1. Clone the repository
2. Install dependencies:

```py
pipenv install
```

3. Activate the virtual environment:

```py
pipenv shell
```

4. Run migrations:

```py
python3 manage.py migrate
```

5. Create a superuser (for admin access):

```py
python3 manage.py createsuperuser
```

6. Start the development server:

```py
python3 manage.py runserver
```

Visit `http://localhost:8000` to view the application.

## API Endpoints

- GET `/api/movie/`: List all movies
- GET `/api/movie/{id}/`: Get specific movie details

## Admin Interface

Access the admin interface at `/admin` to manage:

- Movies (title, genre, stock, daily rate)
- Genres (name)

## Deployment

The application is deployed on Render.com with the following configuration:

- Build Command: `./build.sh`
- Start Command: `gunicorn vidly.wsgi:application`
- Python Version: 3.12
