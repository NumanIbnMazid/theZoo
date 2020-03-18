# import django_heroku
from theZoo.settings.common import *
from decouple import config, Csv
# import dj_database_url

DOMAIN = "127.0.0.1:8000"

ENVIRONMENT = 'production'

# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = "rwgpxlqmz(mr36bd$!b*r4ab($s^5d@(@4!4nsia#dc9moiekn"
# SECRET_KEY = os.environment.get(
#     'SECRET_KEY', 'rwgpxlqmz(mr36bd$!b*r4ab($s^5d@(@4!4nsia#dc9moiekn')
DEBUG = config('DEBUG', default=False, cast=bool)
# MANAGERS = ADMINS
# TEMPLATE_DEBUG = DEBUG
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['dacourier.herokuapp.com']
EMAIL_BACKEND = config('EMAIL_BACKEND', default='')
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)

# FACEBOOK_CLIENT_ID_DEV = config('FACEBOOK_CLIENT_ID_DEV', default='')
# FACEBOOK_SECRET_KEY_DEV = config('FACEBOOK_SECRET_KEY_DEV', default='')

# Database Settings Module

# DATABASES['default'] = os.environment.get(
#     'DATABASE_URL', 'postgres://glhdktambrrchn:a930749ddbb8e1d8fbdce2b93665a9e345fc940c52bdc0dbdcdb4c0e56e3ea3d@ec2-174-129-254-249.compute-1.amazonaws.com:5432/d195r6a9nj6ovg'
# )


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': '',
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#             'autocommit': True,
#             'use_unicode': True,
#             'init_command': 'SET storage_engine=INNODB,character_set_connection=utf8mb4,collation_connection=utf8mb4_unicode_ci',
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         },
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME_PS'),
#         'USER': config('DB_USER_PS'),
#         'PASSWORD': config('DB_PASSWORD_PS'),
#         'HOST': config('DB_HOST_PS'),
#         'PORT': config('DB_PORT_PS'),
#         # 'OPTIONS': {
#         #     'charset': 'utf8mb4',
#         #     'autocommit': True,
#         #     'use_unicode': True,
#         #     'init_command': 'SET storage_engine=INNODB,character_set_connection=utf8mb4,collation_connection=utf8mb4_unicode_ci',
#         #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         # },
#     }
# }


# Static Configs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_proj')
]

STATIC_ROOT = os.path.join('static_cdn', 'static_root')
MEDIA_ROOT = os.path.join('static_cdn', 'media_root')


# HEROKU DEPLOYMENT

CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDER_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000
SECURE_FRAME_DENY = True

# HEROKU DEPLOYMENT

# Activate Django-Heroku.
# django_heroku.settings(locals())
