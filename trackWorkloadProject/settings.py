import sys
import dj_database_url
from os import getenv, path
from pathlib import Path
from django.core.management.utils import get_random_secret_key
from datetime import timedelta
import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = BASE_DIR / '.env'

if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

DEVELOPMENT_MODE = getenv('DEVELOPMENT_MODE', 'False') == 'True'


SECRET_KEY = getenv('DJANGO_SECRET_KEY', get_random_secret_key())

DEBUG = getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS',
                       '127.0.0.1,localhost').split(',')

CORS_ALLOW_HEADERS = [
    'access-control-allow-origin',
    'authorization',
    'content-type',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'djoser',
    'storages',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'trackWorkloadProject.urls'

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

WSGI_APPLICATION = 'trackWorkloadProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


if DEVELOPMENT_MODE is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if getenv('DATABASE_URL', None) is None:
        raise Exception('DATABASE_URL environment variable not defined')
    DATABASES = {
        'default': dj_database_url.parse(getenv('DATABASE_URL')),
    }

DOMAIN = getenv('DOMAIN')
SITE_NAME = 'Track workload'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


if DEVELOPMENT_MODE is True:
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static'
    MEDIA_URL = 'media/'
    MEDIA_ROOT = BASE_DIR / 'media'
else:
    STORAGES = {
        'default': {'BACKEND': 'custom_storages.CustomS3Boto3Storage'},
        'staticfiles': {'BACKEND': 'storages.backends.s3boto3.S3StaticStorage'}
    }

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': False,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{token}',
    'ACTIVATION_URL': 'activation/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,
    'SERIALIZERS': {
        'user_create': 'users.serializers.CustomUserCreateSerializer',
        'user': 'users.serializers.CustomUserSerializer',
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=999),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=999),
}

AUTH_COOKIE = 'access'
AUTH_COOKIE_MAX_AGE = None
AUTH_COOKIE_SECURE = getenv('AUTH_COOKIE_SECURE', 'True') == 'True'
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'

CORS_ALLOWED_ORIGINS = getenv(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost:3000,http://127.0.0.1:3000'
).split(',')

CORS_ALLOW_CREDENTIALS = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.UserAccount'
