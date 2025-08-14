import os
from pathlib import Path
import dj_database_url

# -----------------------
# Paths
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# Security
# -----------------------
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-vu@0qc(d-7a9)z^%v&7aet%mkq%avp$nj055kuut_l4kb7gqba'
)

DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*'] if DEBUG else os.getenv('ALLOWED_HOSTS', 'myapp-2-z7fd.onrender.com').split(',')

# -----------------------
# Installed apps
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'donar',
    'bootstrap5',
    'authentication',
]

# -----------------------
# Middleware
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myapp.urls'

# -----------------------
# Templates
# -----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myapp.wsgi.application'

# -----------------------
# Database
# -----------------------
if DEBUG:
    # Development: Local MySQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_db',
            'USER': 'root',
            'PASSWORD': '',  # Your local password
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
else:
    # Production: External PostgreSQL on Render
    DATABASES = {
        'default': dj_database_url.parse(
            os.getenv(
                'DATABASE_URL',
                'postgresql://django_db_ggnj_user:HhIElWSzcTv6fHjlwQZjTd5BjyRG2FC0@dpg-d2ep8andiees73847q10-a.oregon-postgres.render.com/django_db_ggnj'
            ),
            conn_max_age=600,
            ssl_require=True  # Required for Render PostgreSQL
        )
    }

# -----------------------
# Password validation
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------
# Internationalization
# -----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------
# Static files
# -----------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # local static files
STATIC_ROOT = BASE_DIR / 'staticfiles'    # production collectstatic

# -----------------------
# Default primary key field type
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------
# Custom user model
# -----------------------
AUTH_USER_MODEL = 'authentication.User'
