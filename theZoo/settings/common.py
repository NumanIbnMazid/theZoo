import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'sslserver',
    'django_countries',
    'django_cleanup',
    'widget_tweaks',
    # Local Apps
    'accounts',
    'animal',
    'food',
    'health',
    'maintenance',
    'staff',
    'util',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    # 'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom Middlewares
    'middlewares.middlewares.RequestMiddleware',
]

ROOT_URLCONF = 'theZoo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'theZoo.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static Configs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_proj')
]

STATIC_ROOT = os.path.join('static_cdn', 'static_root')
MEDIA_ROOT = os.path.join('static_cdn', 'media_root')


# Allauth Staffs
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = '/'
HOME_URL = '/'
SITE_NAME = 'theZoo'
ACCOUNT_EMAIL_MAX_LENGTH = 190
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_USERNAME_MIN_LENGTH = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # mandatory, optional, none
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'theZoo'
ACCOUNT_USERNAME_BLACKLIST = ['robot', 'hacker', 'virus', 'spam']
ACCOUNT_ADAPTER = 'theZoo.adapter.UsernameMaxAdapter'
# ACCOUNT_FORMS = {
#     'signup': 'theZoo.forms.CustomSignupForm',
# }
# AUTH_USER_MODEL = 'theZoo.accounts.models.UserProfile'
# ACCOUNT_SIGNUP_FORM_CLASS = 'theZoo.forms.CustomSignupForm'


# File Staffs
ALLOWED_IMAGE_TYPES = ['.jpg', '.jpeg', '.png']
ALLOWED_DOCUMENT_TYPES = ['.doc', '.docx', '.pdf']
ALLOWED_FILE_TYPES = ['.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx']
# 1.5MB - 1621440
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_IMAGE_UPLOAD_SIZE = 1621440
MAX_UPLOAD_SIZE = 1621440
