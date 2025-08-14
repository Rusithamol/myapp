import os
from pathlib import Path
import pymysql

# Use PyMySQL as MySQLdb
pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# Security
# -----------------------
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'myapp-2-z7fd.onrender.com').split(',')

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
# Database (MySQL on Render)
# -----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'django_db'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'aws.connect.psdb.cloud'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'ssl': {'ca': os.getenv('MYSQL_SSL_CA', None)},  # Render may provide a CA certificate
        },
    }
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
STATIC_ROOT = BASE_DIR / 'staticfiles'    # collected static files for production

# -----------------------
# Default primary key field type
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------
# Custom user model
# -----------------------
AUTH_USER_MODEL = 'authentication.User'

