"""
Django settings for alpha project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+_^umb&*n#&$_nw03d)2lna!+v)##4z_lf8^5u8bl6cgw9*+(h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = [('Emanuel Zuniga', 'emanuelziga@gmail.com'), ]


ALLOWED_HOSTS = ['35.165.154.94', '127.0.0.1', 'localhost', 'app.fudesemillas.net', ]


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'livereload',
    'widget_tweaks',
    'rest_framework',
    'django.contrib.humanize',
    'accounting.apps.AccountingConfig',
    'general.apps.GeneralConfig',
    'sales.apps.SalesConfig',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'alpha.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')),
                 ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('pyjade.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
            'builtins': ['pyjade.ext.django.templatetags'],
        },
    },
]

if DEBUG:
    WSGI_APPLICATION = 'alpha.wsgi.application'

if not DEBUG:
    WSGI_APPLICATION = 'alpha.wsgi-prod.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fudesemillas',
            'USER': 'emanuelziga',
            'PASSWORD': 'emma101421',
            'HOST': '127.0.0.1',
            'PORT': '5432',
            }
        }

JET_SIDE_MENU_COMPACT = False

JET_SIDE_MENU_CUSTOM_APPS = [
    ('auth', [  # Each list element is a tuple with application name (app_label) and list of models
        'User',
        'Profile',
        'Group',
        ]),
    ('general', [
        'Contact',
        'Company',
        'Currency',
        ]),
    ('sales', [
        'Product',
        'Client',
        ]),
    ('accounting', [
        'Entry',
        'Account',
        'Report',
        ]),

        ]
# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
    }

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Costa_Rica'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/admin/login/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        ]

    STATIC_URL = '/static/'
    STATIC_ROOT = ''

if not DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = (os.path.join(BASE_DIR, 'static'))

MEDIA_URL = '/media/'
MEDIA_ROOT = ''
