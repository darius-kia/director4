"""
Django settings for director project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from typing import Container, Iterable, List, Pattern

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "1=8bz5v!#jke@p!&8x1=u-6%(m4(+s_pmgk9&)36nnduta(6io"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "director",
    "director.csl.tjhsst.edu",
    "director.tjhsst.edu",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "channels",
    "django_extensions",
    "director.apps.auth",
    "director.apps.users",
    "director.apps.sites",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "director.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "director.apps.context_processors.base_context",
            ]
        },
    }
]

WSGI_APPLICATION = "director.wsgi.application"
ASGI_APPLICATION = "director.routing.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = ("director.apps.auth.oauth.IonOauth2",)

SOCIAL_AUTH_USER_FIELDS = [
    "username",
    "first_name",
    "last_name",
    "email",
    "id",
    "is_teacher",
    "is_student",
]

SOCIAL_AUTH_URL_NAMESPACE = "social"

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "director.apps.auth.oauth.get_username",
    "social_core.pipeline.social_auth.associate_by_email",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
)

AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_URL = "auth:login"
LOGIN_REDIRECT_URL = "auth:index"
LOGOUT_REDIRECT_URL = "auth:index"

SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 2 * 7 * 24 * 60 * 60
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SOCIAL_AUTH_ALWAYS_ASSOCIATE = True
SOCIAL_AUTH_LOGIN_ERROR_URL = "/"
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "serve")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Celery
CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"

# Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {"hosts": [("127.0.0.1", 6379)]},
    }
}


# Director-related stuff

# Site name blacklisting/whitelisting

# Sites with these names will be allowed, even if they are blacklisted below.
WHITELISTED_SITE_NAMES: Container[str] = set()

# Creating sites with these names that are in BLACKLISTED_SITE_NAMES, or with names that match a
# regular expression in BLACKLISTED_SITE_REGEXES (for efficiency, regexes must be compiled with
# re.compile()), will be blocked (unless they are whitelisted above).
# Editing sites with these names may also not work properly, so sites should be deleted before
# blacklisting their name or blacklisting by regex.
BLACKLISTED_SITE_NAMES: Container[str] = set()
BLACKLISTED_SITE_REGEXES: Iterable[Pattern[str]] = []


# A list of the hosts each of the appservers are running on (or can be reached
# on via some kind of proxy). If a proxy is used, it should support both HTTP
# requests and Websocket connections.
# These are host:port combos. They are NOT URLs. This list should also not be
# taken from unsafe sources, as they may be interpolated into URLs without any
# form of escaping or validation.
# Example: ["localhost:5443", "director-app1.example.com:5443"]
DIRECTOR_APPSERVER_HOSTS: List[str] = []

# Set this to None to disable SSL. Set it to a dictionary like this to enable SSL:
# {
#     "cafile": "<path to CA file used to verify appserver certificates>",
#     "client_cert": {
#         "certfile": "<path to client certificate file>",  # Required
#         "keyfile": "<path to client private key file>",  # Taken from certfile
#         # if not passed
#         "password": "<private key password>",  # Required if private key is
#         # encrypted
#     },
# }
# Yes, the SSL settings must be the same for all appservers. This is by design.
DIRECTOR_APPSERVER_SSL = None

try:
    from .secret import *  # noqa  # pylint: disable=unused-import
except ImportError:
    pass

CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = not DEBUG

DIRECTOR_NUM_APPSERVERS = len(DIRECTOR_APPSERVER_HOSTS) if DIRECTOR_APPSERVER_HOSTS else 0
