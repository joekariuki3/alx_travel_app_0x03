from pathlib import Path
import environ
import os
from datetime import timedelta

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
env.read_env(os.path.join(BASE_DIR, ".env"))

# ENVIRONMENT either development, testing or production
ENVIRONMENT = env("ENVIRONMENT", default="development").upper()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env(f"{ENVIRONMENT}_SECRET_KEY", default=os.urandom(256).hex())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool(f"{ENVIRONMENT}_DEBUG", default=False)

ALLOWED_HOSTS = env.list(f"{ENVIRONMENT}_ALLOWED_HOSTS", default=[])


# Application definition

INSTALLED_APPS = [
    "listings.apps.ListingsConfig",
    "rest_framework",
    "drf_yasg",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "django_celery_results",
    "rest_framework_simplejwt.token_blacklist",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = "alx_travel_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "alx_travel_app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
db_name = env(f"{ENVIRONMENT}_DATABASE_NAME")
db_user = env(f"{ENVIRONMENT}_DATABASE_USER")
db_password = env(f"{ENVIRONMENT}_DATABASE_PASSWORD")
db_host = env(f"{ENVIRONMENT}_DATABASE_HOST")
db_port = env(f"{ENVIRONMENT}_DATABASE_PORT")

DEVELOPMENT_DATABASE = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": db_name,
        "HOST": db_host,
        "USER": db_user,
        "PASSWORD": db_password,
        "PORT": db_port,
    },
}
# production db details
# PRODUCTION_DATABASE = {
#     'default': dj_database_url.config(
#         default=f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}',
#         conn_max_age=600
#     )
# }
PRODUCTION_DATABASE = {
    "default": {
        # 'ENGINE': 'django.db.backends.postgresql',
        "ENGINE": "django.db.backends.mysql",
        "NAME": db_name,
        "HOST": db_host,
        "USER": db_user,
        "PASSWORD": db_password,
        "PORT": db_port,
    },
}

TESTING_DATABASE = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

DATABASES = (
    DEVELOPMENT_DATABASE
    if ENVIRONMENT == "DEVELOPMENT"
    else PRODUCTION_DATABASE
    if ENVIRONMENT == "PRODUCTION"
    else TESTING_DATABASE
)

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
if not DEBUG and ENVIRONMENT == "PRODUCTION":
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "listings.User"

# celery settings
rb_user = env(f"{ENVIRONMENT}_RABBITMQ_USERNAME", default="guest")
rb_password = env(f"{ENVIRONMENT}_RABBITMQ_PASSWORD", default="guest")
rb_host = env(f"{ENVIRONMENT}_RABBITMQ_HOST", default="localhost")
rb_port = env(f"{ENVIRONMENT}_RABBITMQ_PORT", default="5672")
CELERY_BROKER_URL = f"amqp://{rb_user}:{rb_password}@{rb_host}:{rb_port}//"
CELERY_RESULT_BACKEND = env(f"{ENVIRONMENT}_CELERY_RESULT_BACKEND", default="django-db")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
CELERY_RESULT_EXTENDED = env.bool(f"{ENVIRONMENT}_CELERY_RESULT_EXTENDED", default=True)

# Email settings console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# rest authentication
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),  # "Bearer <Token>"
}
