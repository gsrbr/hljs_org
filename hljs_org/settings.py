import os
from configparser import ConfigParser
from collections import ChainMap


parser = ConfigParser()
parser.optionxform = str  # don't lowercase keys
parser.read('/etc/hljs_org/environment.ini')
env = ChainMap(os.environ, parser.defaults()).get

DEBUG = env('DEBUG') != '0'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'highlightjs.org']
ADMINS = [('Ivan Sagalaev', 'info@highlightjs.org')]

TIME_ZONE = 'US/Pacific'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False
USE_TZ = True

SECRET_KEY = env('SECRET_KEY', 'debug' if DEBUG else '')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hljs_org',
    }
}

if env('MEMCACHE'):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
            'LOCATION': env('MEMCACHE'),
        },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hljs_org',
]

ROOT_URLCONF = 'hljs_org.urls'
WSGI_APPLICATION = 'hljs_org.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {'format': '%(asctime)s %(levelname)s %(name)s %(message)s'},
    },
    'filters': {
        'debug-false': {'()': 'django.utils.log.RequireDebugFalse'},
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
        },
        'mail': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'filters': ['debug-false'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'mail'],
            'level': env('LOG_LEVEL', 'INFO')
        }
    },
}
LOGGING_CONFIG = None
import logging.config
logging.config.dictConfig(LOGGING)

HLJS_SOURCE = env('HLJS_SOURCE', '../highlight.js')
HLJS_CACHE = env('HLJS_CACHE', '../cache')

STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT', '')
# Include highlight.js built static content in DEBUG mode so `runserver` could
# serve it automatically. In production it's going to break `collectstatic`.
if DEBUG:
    STATICFILES_DIRS = ['../static']

HLJS_CODESTYLES = [
    'default',
    'solarized-dark',
    'solarized-light',
    'github',
    'railscasts',
    'monokai-sublime',
    'mono-blue',
    'tomorrow',
    'color-brewer',
    'zenburn',
    'agate',
    'androidstudio',
    'dracula',
    'rainbow',
    'vs',
    'atom-one-dark',
    'atom-one-light',
]

HLJS_SNIPPETS = [
    'python',
    'xml',
    'javascript',
    'http',
    'cpp',
    'sql',
    'clojure',
    'csharp',
    'objectivec',
    'java',
    'swift',
    'css',
    'ruby',
    'makefile',
    'go',
    'coffeescript',
    'bash',
    'ini',
    'rust',
    'handlebars',
    'prolog',
    'typescript',
    'elm',
    'json',  # needed as a sub-language for 'http'
]

HLJS_CDNS = [
    (
        'cdnjs',
        '//cdnjs.cloudflare.com/ajax/libs/highlight.js/%s/highlight.min.js',
        '//cdnjs.cloudflare.com/ajax/libs/highlight.js/%s/styles/default.min.css',
    ),
    (
        'jsdelivr',
        '//cdn.jsdelivr.net/gh/highlightjs/cdn-release@%s/build/highlight.min.js',
        '//cdn.jsdelivr.net/gh/highlightjs/cdn-release@%s/build/styles/default.min.css',
    ),
]
