from .settings import *
import os

DEBUG = True

#Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h'

# Você também pode deixar em branco com colchetes vazios [] 
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}