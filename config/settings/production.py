# flake8: noqa
# type: ignore
from .base import *

# https://docs.djangoproject.com/en/3.2/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# Project settings
# ------------------------------------------------------------------------------
SETTINGS_MODULE = PRODUCTION_SETTINGS
