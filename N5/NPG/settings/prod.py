from .base import *

DEBUG = False

ALLOWED_HOSTS = ["www.nepmia.fr"]

DATABASES = {
    
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': os.getenv("POSTGRES_DB"),

        'USER': os.getenv("POSTGRES_USER"),

        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),

        'HOST': 'db',

        'PORT': '5432',

    }

}
