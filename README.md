# ALX Travel App

## Overview

ALX Travel App is a Django-based web application for managing travel accommodations. The platform connects hosts with guests, allowing users to list properties for rent, make bookings, and leave reviews.

## Features

- **User Management**: Registration, authentication, and profile management
- **Property Listings**: Hosts can create and manage property listings
- **Booking System**: Guests can book properties with booking status tracking
- **Review System**: Guests can leave reviews and ratings
- **Location-based Search**: Filter accommodations by location

## Technical Stack

- **Backend**: Django 5.2.x with Django REST Framework
- **Database**: MySQL (configured via env).
- **API Documentation**: Swagger via drf-yasg
- **Authentication**: Django's built-in authentication system; custom User model
- **Task Processing**: Celery for asynchronous tasks
- **CORS**: Enabled via django-cors-headers (allow all in dev)

## Project Structure

Key apps and files:
- `alx_travel_app/` – Django project (settings, urls, swagger)
- `listings/` – domain app (models, serializers, views, tasks, admin, tests)
- `listings/management/commands/seed.py` – load sample data from CSVs

Core models:
- **User**: Custom user model (UUID primary key)
- **Location**: Stores country, state, and city information
- **Listing**: Property listings with details like title, price, and description
- **Booking**: Manages reservations with statuses (active, cancelled, pending)
- **Review**: Stores ratings and comments from guests

## Setup and Installation

### Prerequisites

- Python 3.10.x
- virtualenv
- MySQL server (for default settings) and a database/user
- RabbitMQ (for Celery).

### Installation Steps

1. Clone the repository
2. Create and activate a virtual environment:

```bash
python -m virtualenv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r alx_travel_app/alx_travel_app/requirement.txt
```

4. Create a `.env` file in `alx_travel_app/alx_travel_app/` (same directory as settings.py) with at least:

```
# Core
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (MySQL)
DATABASE_NAME=alx_travel
DATABASE_HOST=localhost
DATABASE_USER=dbuser
DATABASE_PASSWORD=dbpassword
DATABASE_PORT=3306

# RabbitMQ
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
```

Note: settings.py reads the .env from the project directory (alx_travel_app/alx_travel_app). If you prefer SQLite for quick local runs, you can change DATABASES in settings.py to use sqlite3, but by default it's MySQL.

5. Apply migrations:

```bash
python alx_travel_app/manage.py migrate
```

6. (Optional) Seed sample data:

```bash
python alx_travel_app/manage.py seed
```

7. Create a superuser:

```bash
python alx_travel_app/manage.py createsuperuser
```

8. Start the development server:

```bash
python alx_travel_app/manage.py runserver
```

## Running Celery

Celery is used for async tasks (e.g., sending booking confirmation emails).

- Ensure RabbitMQ is running and env vars are set as above.
- Start a worker in a separate terminal:

```bash
celery -A alx_travel_app worker --loglevel=info
```

If you plan to use periodic tasks, also run beat (not configured by default):

```bash
celery -A alx_travel_app beat --loglevel=info
```

## API Endpoints & Docs

- Base API path: `/api/` (see `listings/urls.py` for available endpoints)
- Swagger UI: `/swagger/` (served via project urls)

## Development

### Running Tests

```bash
python alx_travel_app/manage.py test
```

### Code Style

This project follows PEP 8 coding standards for Python.

## Troubleshooting

- MySQL connection errors: verify DATABASE_* env vars and that the DB user has privileges.
- Celery connection errors: verify RabbitMQ is running and RABBITMQ_* env vars.
- Custom user model: AUTH_USER_MODEL is `listings.User`; ensure migrations are applied before creating superuser.

## License

This project is licensed under the MIT License.