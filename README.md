# ALX Travel App

## Overview

ALX Travel App is a Django-based web application for managing travel accommodations. The platform connects hosts with guests, allowing hosts to list properties and guests to make bookings and leave reviews.

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

3. Install dependencies (from pyproject.toml):

```bash
pip install --upgrade pip
pip install .
```

4. Create a `.env` file in `alx_travel_app/` (same directory as manage.py) with at least:

```
# Core
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*

# Database (MySQL)
DATABASE_NAME=alx_travel
DATABASE_HOST=127.0.0.1
DATABASE_USER=dbuser
DATABASE_PASSWORD=dbpassword
DATABASE_PORT=3306

# Payment (Chapa)
CHAPA_SECRET_KEY=your_chapa_secret
CHAPA_BASE_URL=https://api.chapa.co/v1
APP_URL=http://127.0.0.1
APP_PORT=8000

# RabbitMQ
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest
RABBITMQ_HOST=127.0.0.1
RABBITMQ_PORT=5672

# Celery Results
CELERY_RESULT_BACKEND=django-db
CELERY_RESULT_EXTENDED=True
```

Note: settings.py reads the .env from `BASE_DIR` which is the project directory `alx_travel_app/`. By default the database is MySQL.

5. Apply migrations (including django-celery-results):

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

Celery is used for async tasks (e.g., sending booking/payment confirmation emails).

- Ensure RabbitMQ is running and env vars are set as above.
- Start a worker in a separate terminal:

```bash
celery -A alx_travel_app worker --loglevel=info
```

If you plan to use periodic tasks, also run beat (not configured by default):

```bash
celery -A alx_travel_app beat --loglevel=info
```

### Task Results Storage
This project uses django-celery-results, saving task results to your database.
- Make sure migrations are applied.
- Inspect recent results with a SQL query:

```sql
SELECT id, task_id, task_name, status, date_done
FROM django_celery_results_taskresult
ORDER BY date_done DESC
LIMIT 10;
```

## API Endpoints & Docs

- Base API path: `/api/` (see `listings/urls.py` for available endpoints)
- Swagger UI: `/swagger/` (served via project urls)
- Payment verification callback: `GET /api/payment/verify/<tx_ref>/` (invoked by Chapa return flow)

## Email

- Email backend is set to console for development, so emails are printed to the server/worker console.
- Optionally set `DEFAULT_FROM_EMAIL` in settings or via env if you change to a real email backend.

## Development

### Running Tests

```bash
python alx_travel_app/manage.py test
```

### Code Style

This project follows PEP 8 coding standards for Python.

## Troubleshooting

- MySQL connection errors: verify DATABASE_* env vars and that the DB user has privileges.
- Celery connection errors: verify RabbitMQ is running and RABBITMQ_* env vars. Ensure your RabbitMQ user exists and has permissions; defaults are guest/guest on localhost only.
- Task results not appearing: run `python alx_travel_app/manage.py migrate django_celery_results` and confirm CELERY_RESULT_BACKEND=django-db in .env.
- Emails not sent: in development they are printed to console; for real emails configure EMAIL_BACKEND and DEFAULT_FROM_EMAIL.
- Custom user model: AUTH_USER_MODEL is `listings.User`; ensure migrations are applied before creating superuser.

## License

This project is licensed under the MIT License.