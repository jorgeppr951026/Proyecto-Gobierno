from .base import *

DEBUG = True


ALLOWED_HOSTS = []

DATABASES = {
  'default': {
        #'#ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        #'ENGINE': 'django.db.backends.mysql',
        #'ENGINE': 'django.db.backends.oracle',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gobierno2',
        'USER': 'openpg',
        'PASSWORD': 'openpgpwd',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}