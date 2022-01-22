from base import *

DEBUG = False

DATABASES = {
    
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': os.getenv("DB_NAME"),

        'USER': os.getenv("DB_USER"),

        'PASSWORD': os.getenv("DB_PSSWD"),

        'HOST': '127.0.0.1',

        'PORT': '5432',

    }

}
