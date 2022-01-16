from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# using django-environ to read .env file
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR.parent, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1',])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'translation_manager',
    'website.apps.WebsiteConfig',
    'tailwind',
    'theme',
    'parler',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'transfeminiinit.urls'

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

WSGI_APPLICATION = 'transfeminiinit.wsgi.application'


# Database

DATABASES = {
    'default': env.db_url('DATABASE_URL')
}


# Password validation

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


# Internationalization

# default language
LANGUAGE_CODE = 'fi'

# supported languages
LANGUAGES = (
    ('fi', 'Suomi'),
    ('sv', 'Svenska'),
    ('en', 'English'),
)

PARLER_LANGUAGES = {
    None: tuple({'code': lang[0],} for lang in LANGUAGES),
    'default': {
        'fallback': 'fi',
        'hide_untranslated': False,
    }
}

# for internationalization support
USE_I18N = True

# Contains the path list where Django should look into for django.po files for all supported languages
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# format numbers and dates to locale
USE_L10N = True

# time zone support
USE_TZ = True
TIME_ZONE = 'UTC' # used to avoid DST issues in the database

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# media
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media/"

CKEDITOR_UPLOAD_PATH = "uploads/"

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# whitenoise
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# enforce SSL
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)

# tailwind
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = env.list('INTERNAL_IPS', default=["127.0.0.1",])
