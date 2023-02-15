import json
import os
import django_heroku
import dj_database_url
# import storages.backends.s3boto3


if os.path.exists('C:/json/config.json'):
    with open('C:/json/config.json') as config_file:
        config = json.load(config_file)
        SECRET_KEY = config.get('SECRET_KEY')

        AWS_ACCESS_KEY_ID = config.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config.get('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config.get('AWS_STORAGE_BUCKET_NAME')
        DEBUG = config.get('DEBUG_VALUE')
        ALLOWED_HOSTS = config.get('ALLOWED_HOSTS')
        DATABASES = {
            'default': {
                'ENGINE': config.get('DB_ENGINE'),
                'NAME': config.get('DB_NAME'),
                'USER': config.get('DB_USER'),
                'PASSWORD': config.get('DB_PASSWORD'),
                'HOST': config.get('DB_HOST'),
                'PORT': config.get('DB_PORT'),
            }
        }
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    DEBUG = os.environ.get('DEBUG_VALUE')
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
    DATABASES = {}
    if 'DYNO' in os.environ:  # Dette sker kun på Heroku, hvis man er på heroku så skal dette settes op
        DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.environ.get('DB_NAME'),
                'USER': os.environ.get('DB_USER'),
                'PASSWORD': os.environ.get('DB_PASSWORD'),
                'HOST': os.environ.get('DB_HOST'),
                'PORT': os.environ.get('DB_PORT'),
            }
        }

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'case.apps.CaseConfig',
    'caseworker.apps.CaseworkerConfig',
    'crispy_forms',
    'storages',
    'django_extensions',
    'extra_views',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

django_heroku.settings(locals())

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

LOGIN_REDIRECT_URL = '/case/'

# Feature toggles
FEATURES = {}
if os.path.exists('C:/json/features.json'):
    with open('C:/json/features.json') as feature_file:
        FEATURES = json.load(feature_file)
        print(f"FEATURES: {FEATURES}")
elif 'FEATURES' in os.environ:
    FEATURES = json.loads(os.environ.get('FEATURES'))
