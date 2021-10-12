from .settings import *

DEBUG = True

SECRET_KEY = 't8fu&n&q&hk!-(d4mc0czl*06_cr(h!!eor$c*r8^-@s+)hqh_'



DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['127.0.0.1']