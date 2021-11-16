# flake8: noqa
# type: ignore
import logging

import environ

env = environ.Env()

# Build paths inside the project like this: os.path.join(ROOT_DIR, ...)
# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('apps')

# https://docs.djangoproject.com/en/3.2/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key
SECRET_KEY = env.str('DJANGO_SECRET_KEY', default='zi1k=@0b$h-cfxbgms70ps=wnvyqtwc4i=myn-w-_4z(+_+2a0')

# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# https://docs.djangoproject.com/en/3.2/ref/settings/#installed-apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
LOCAL_APPS = [
    'apps.movies.apps.MoviesConfig',
]
THIRD_PARTY_APPS = [
    'debug_toolbar',
    'django_extensions',
]
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# https://docs.djangoproject.com/en/3.2/topics/http/middleware/#activating-middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# https://docs.djangoproject.com/en/3.2/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR.path('templates'))],
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

# https://docs.djangoproject.com/en/3.2/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'

# https://docs.djangoproject.com/en/3.2/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///anime'),
}

# https://docs.djangoproject.com/en/3.2/ref/settings/#atomic-requests
DATABASES['default']['ATOMIC_REQUESTS'] = True

# https://docs.djangoproject.com/en/3.2/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# https://docs.djangoproject.com/en/3.2/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [APPS_DIR('static')]

# https://docs.djangoproject.com/en/3.2/topics/cache/#setting-up-the-cache
CACHES = {'default': {}}

# Project specific settings
# ------------------------------------------------------------------------------
LOCAL_SETTINGS = 'config.settings.local'
PRODUCTION_SETTINGS = 'config.settings.production'
SETTINGS_MODULE = env('DJANGO_SETTINGS_MODULE', default=LOCAL_SETTINGS)
