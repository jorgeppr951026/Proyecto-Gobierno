from .base import *
import django_heroku

DEBUG = True



ALLOWED_HOSTS = ['*']



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


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


#Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Activate Django-Heroku.
django_heroku.settings(locals())

import dj_database_url

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)