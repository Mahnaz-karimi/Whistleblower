import json
import os
import django_heroku
# import storages.backends.s3boto3

if (os.path.exists('/etc/config.json')):
    with open('/etc/config.json') as config_file:
        config = json.load(config_file)
        SECRET_KEY = config.get('SECRET_KEY')
        EMAIL_HOST_USER = config.get('EMAIL_USER')
        EMAIL_HOST_PASSWORD = config.get('EMAIL_PASS')
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
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    DEBUG = os.environ.get('DEBUG_VALUE')
    ALLOWED_HOSTS = ['www.reporteasily.com', '172.104.154.174']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'wb',
            'USER': 'postgres',
            'PASSWORD': 'hest3fiskesovs',
            'HOST': '172.105.74.176',
            'PORT': '5432',
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
