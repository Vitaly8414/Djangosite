"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL

import os

from dotenv import load_dotenv  

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
# django-insecure-ki)fobhh$=f(#0*5&8*(sdymua0f#p+!+%l-sgyxwy6kn%+a17
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool(os.environ.get("DEBUG"))

SESSION_COOKIE_SECURE = True  
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [
    "127.0.0.1", 
    "vvv8414.pythonanywhere.com",
    ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'myapp2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {  
#     "default": {  
#         "ENGINE": "django.db.backends.mysql",  
#         "NAME": os.getenv("MYSQL_DBNAME"),  
#         "USER": os.getenv("MYSQL_USER"),  
#         "PASSWORD": os.getenv("MYSQL_PASSWORD"),  
#         "HOST": os.getenv("MYSQL_HOST"),  
#         "OPTIONS": {  
#             "init_command": "SET NAMES 'utf8mb4';SET sql_mode = 'STRICT_TRANS_TABLES'",  
#             "charset": "utf8mb4",  
#         },  
#     }  
# }

if os.getenv("DB_USED", default="").lower() == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("MYSQL_DBNAME"),
            "USER": os.getenv("MYSQL_USER"),
            "PASSWORD": os.getenv("MYSQL_PASSWORD"),
            "HOST": os.getenv("MYSQL_HOST"),
            "OPTIONS": {
                "init_command": "SET NAMES 'utf8mb4';SET sql_mode = 'STRICT_TRANS_TABLES'",
                "charset": "utf8mb4",
            },
        }
    }
elif os.getenv("DB_USED", default="").lower() == "sqlite3":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "dev_db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"  
STATIC_ROOT = BASE_DIR / "static/"  

MEDIA_URL = "media/"  
MEDIA_ROOT = BASE_DIR / "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

