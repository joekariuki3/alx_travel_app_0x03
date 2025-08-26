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

- **Backend**: Django 5.x with Django REST Framework
- **Database**: SQLite (development) with option for MySQL (production)
- **API Documentation**: Swagger/OpenAPI via drf-yasg
- **Authentication**: Django's built-in authentication system
- **Task Processing**: Celery for asynchronous tasks

## Project Structure

The application is organized around the following models:

- **User**: Extended Django user model with UUID as primary key
- **Location**: Stores country, state, and city information
- **Listing**: Property listings with details like title, price, and description
- **Booking**: Manages reservations with statuses (active, cancelled, pending)
- **Review**: Stores ratings and comments from guests

## Setup and Installation

### Prerequisites

- Python 3.10.x
- virtualenv

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

4. Set up environment variables by creating a `.env` file in the project root with:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# For MySQL (optional)
# DATABASE_NAME=alx_travel
# DATABASE_HOST=localhost
# DATABASE_USER=dbuser
# DATABASE_PASSWORD=dbpassword
# DATABASE_PORT=3306
```

5. Run migrations:

```bash
python alx_travel_app/manage.py migrate
```

6. Create a superuser:

```bash
python alx_travel_app/manage.py createsuperuser
```

7. Start the development server:

```bash
python alx_travel_app/manage.py runserver
```

## API Documentation

API documentation is available via Swagger UI at `/swagger/` when the server is running.

## Development

### Running Tests

```bash
python alx_travel_app/manage.py test
```

### Code Style

This project follows PEP 8 coding standards for Python.

## License

This project is licensed under the MIT License - see the LICENSE file for details.