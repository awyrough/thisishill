"""
Django settings for thisishill project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from secret import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if os.environ.get('ENVIRONMENT', False) == 'production':
    DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.humanize',

    # third party
    'pipeline',
)

PROJECT_APPS = (
    'thisishill',
    'me',
    'trailheadlane',
)

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'thisishill.urls'

WSGI_APPLICATION = 'thisishill.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'thisishill',
        'USER': 'thisishill',
        'PASSWORD': 'thisishill',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

TEMPLATE_DIRS = (
    'templates',
)

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

from pipeline_settings import PIPELINE_ENABLED, PIPELINE_CSS, PIPELINE_JS

# LOGGING
CELERYD_LOG_FORMAT = "CELERY:%(levelname)s %(message)s"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'universal_formatter': {
            'format': '%(name)s:%(levelname)s [%(filename)s]: %(message)s'
        },
        'user_formatter': {
            'format': '%(name)s:%(levelname)s [USERNAME:%(user)s] [APP:%(app)s] [VIEW:%(view)s] [URL:%(path)s]'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'universal_handler':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'universal_formatter'
        },
        'user_handler':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'user_formatter'
        },
    },
    'loggers': {
        # General purpose logging
        'UNIVERSAL': {
            'handlers': ['universal_handler'],
            'propagate': False,
            'level': 'INFO',
        },
        # Log user activities in view
        'USER': {
            'handlers': ['user_handler'],
            'propagate': False,
            'level': 'INFO',
        },
        # Log cache information
        'CACHE': {
            'handlers': ['universal_handler'],
            'propagate': False,
            'level': 'INFO',
        },
        # View logger to log out user
        # Keep the Django DB quiet! (Remove this if you want to see DB logs)
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level':'DEBUG',
        },
        'debug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Restrict Google API client logging
        'googleapiclient.discovery': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        # Turn off stupid requests logging
        'requests': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
    }
}

if DEBUG:
    LOGGING["loggers"]["gunicorn.access"] = {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': False,
    }


if DEBUG and not os.environ.get('ENVIRONMENT', False) == 'staging':
    BROKER_URL = "amqp://localhost"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
else:
    BROKER_URL = os.environ["CLOUDAMQP_URL"]
    BROKER_POOL_LIMIT = 10
    CELERY_RESULT_BACKEND = os.environ["REDISCLOUD_URL"]
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']