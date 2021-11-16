# flake8: noqa
# type: ignore
from .base import *

# https://docs.djangoproject.com/en/3.2/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', True)

# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# https://docs.djangoproject.com/en/3.2/topics/cache/#setting-up-the-cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
        'OPTIONS': {},
    }
}

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configuring-internal-ips
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']
