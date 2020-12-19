import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# LOGIN_REDIRECT_URL = "home:home"
# LOGIN_URL = "account:login"
# LOGOUT_REDIRECT_URL = "account:login"

SECRET_KEY = 'q)z#_2#w4kb^w8sr1ioxeom&8)#l573t*z#h%_l_@!wl_!9=l_'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'home_app',
    'account_app',
    'aboutus_app',
    'privacy_app',
    # packages
    'debug_toolbar',
    'django_render_partial',
    'parsley',
    'sorl.thumbnail',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'django_filters',
    'widget_tweaks',
    'stripe',
    'captcha',
    # sitemap
    'django.contrib.sitemaps',
    'django.contrib.sites',

]
SITE_ID = 1

INTERNAL_IPS = '127.0.0.1',

# EMAIL Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mhrxadev@gmail.com'
DEFAULT_FROM_EMAIL = 'mhrxadev@gmail.com'
SERVER_EMAIL = 'mhrxadev@gmail.com'
EMAIL_HOST_PASSWORD = 'M96m96@75#75$'
EMAIL_PORT = 587

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# RECAPTCHA CONFIG
RECAPTCHA_PUBLIC_KEY = '6LfBINoZAAAAAEERzIdQNkSmZJnkCylvdQJzhxxx'
RECAPTCHA_PRIVATE_KEY = '6LfBINoZAAAAAJuzBhmv9QHhA1odWGn31siueYz_'

# CKEDITOR CONFIGS
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': 1100,
    },
}
CKEDITOR_UPLOAD_PATH = 'uploads/ckeditore'

# STRIPE CONFIG
if DEBUG:
    STRIPE_SECRET_KEY = 'sk_test_51HdrtzK50BOizoKa3hbQ9B17HTMdzhZxw3vMXqZDoToTiDQFuHPO1zr7HOSNUugDF3EVQdTp7FMKg7osBhA1zTsY00rYiWiMjU'
else:
    STRIPE_SECRET_KEY = ''

# CRISPY FORM CONFIG
CRISPY_TEMPLATE_PACK = 'bootstrap4'

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30

AUTH_USER_MODEL = 'account_app.User'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, "static", "site")
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")
