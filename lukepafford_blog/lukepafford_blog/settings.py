"""
Django settings for lukepafford_blog project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env(
    env.str("ENV_PATH", os.path.join(BASE_DIR, "lukepafford_blog", ".env"))
)

# False if not in os.environ
DEBUG = env("DEBUG")

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")

SQLITE_URL = env("SQLITE_URL")

if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "192.168.1.21"]
else:
    ALLOWED_HOSTS = ["192.168.1.21"]

# CACHES = {
#    # read os.environ['CACHE_URL'] and raises ImproperlyConfigured exception if not found
#    'default': env.cache(),
#    # read os.environ['REDIS_URL']
#    'redis': env.cache('REDIS_URL')
# }


# if not DEBUG:
#    ALLOWED_HOSTS = [env("DOMAIN")]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    # Third Party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "markdown_deux",
    # Custom apps
    "user.apps.UserConfig",
    "blog.apps.BlogConfig",
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

ROOT_URLCONF = "lukepafford_blog.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "lukepafford_blog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": SQLITE_URL,}}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# All-Auth Settings
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID = 1
AUTH_USER_MODEL = "user.User"

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#    'google': {
#        # For each OAuth based provider, either add a ``SocialApp``
#        # (``socialaccount`` app) containing the required client
#        # credentials, or list them here:
#        'APP': {
#            'client_id': '123',
#            'secret': '456',
#            'key': ''
#        }
#    }
# }

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# Markdown settings
MARKDOWN_DEUX_STYLES = {
    "default": {
        #       "safe_mode": "escape",
        "extras": {
            "code-friendly": None,
            "pyshell": None,
            "demote-headers": 1,
            "html-classes": {"pre": "prettyprint"},
            "cuddled-lists": None,
            "footnotes": None,
            "header-ids": None,
            "fenced-code-blocks": None,
            "metadata": None,
            "tables": None,
        },
    },
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "public"),
]
