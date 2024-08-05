"""
Django settings for lifebook project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# import os
# from pathlib import Path
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api


# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-biq8w=y8f#i2l5q*dnlgm(&f!1(l(er7&k-nfog&a!@q_j!b(u'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'diary',
#     'rest_framework',
#     'rest_framework.authtoken',  # For APIs
#     'storages',  # For AWS S3
#     'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.google',
#     'cloudinary',
#     'cloudinary_storage',
#     'channels',
#     'corsheaders',
#     'webpack_loader',
# ]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
# }

# ACCOUNT_UNIQUE_EMAIL=True

# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'CACHE': not DEBUG,
#         'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
#         'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats.json'),
#         'POLL_INTERVAL': 0.1,
#         'TIMEOUT': None,
#         'IGNORE': ['.+\.hot-update.js', '.+\.map']
#     }
# }


# CORS_ALLOW_ALL_ORIGINS = True

# # CORS_ALLOWED_ORIGINS = [
# #     "http://localhost:3000",  # React development server
# # ]


# ASGI_APPLICATION = 'lifebook.asgi.application'

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [('127.0.0.1', 6379)],
#         },
#     },
# }

# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# # CLOUDINARY_STORAGE = {
# #     'CLOUD_NAME': 'dvyajjkya',
# #     'API_KEY': '175875286981214',
# #     'API_SECRET': 'eCr01NCcCLgCVFWXLTA3ZCekCeA',
# # }
# CLOUDINARY = {
#     'cloud_name': 'dvyajjkya',
#     'api_key': '175875286981214',
#     'api_secret': 'eCr01NCcCLgCVFWXLTA3ZCekCeA'
# }

# cloudinary.config(
#     cloud_name=CLOUDINARY['cloud_name'],
#     api_key=CLOUDINARY['api_key'],
#     api_secret=CLOUDINARY['api_secret']
# )
# # from decouple import Config

# # config = Config()

# # CLOUDINARY = {
# #     'cloud_name': config('CLOUDINARY_CLOUD_NAME'),
# #     'api_key': config('CLOUDINARY_API_KEY'),
# #     'api_secret': config('CLOUDINARY_API_SECRET')
# # }

# # cloudinary.config(
# #     cloud_name=CLOUDINARY['cloud_name'],
# #     api_key=CLOUDINARY['api_key'],
# #     api_secret=CLOUDINARY['api_secret']
# # )


# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'scrapbookdb',
#         'USER': 'postgres',
#         'PASSWORD': '12345',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# SITE_ID = 1

# ACCOUNT_EMAIL_VERIFICATION = "none"
# ACCOUNT_EMAIL_REQUIRED = True
# LOGIN_REDIRECT_URL = '/entry_list/'

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'allauth.account.middleware.AccountMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
# ]

# ROOT_URLCONF = 'lifebook.urls'

# AUTH_USER_MODEL = 'diary.User'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         # 'DIRS': [],
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'lifebook.wsgi.application'

# # Password validation
# # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# # Internationalization
# # https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = 'static/'


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'diary/static'),
# ]


# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-biq8w=y8f#i2l5q*dnlgm(&f!1(l(er7&k-nfog&a!@q_j!b(u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary',
    'rest_framework',  # For APIs
    'storages',  # For AWS S3
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'cloudinary',
    'cloudinary_storage',
    
    'corsheaders',
    'custom_filters',
    
]





# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels.layers.InMemoryChannelLayer',
#     },
# }

CORS_ALLOW_ALL_ORIGINS = True

ASGI_APPLICATION = 'lifebook.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        },
    },
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'dvyajjkya',
#     'API_KEY': '175875286981214',
#     'API_SECRET': 'eCr01NCcCLgCVFWXLTA3ZCekCeA',
# }
CLOUDINARY = {
    'cloud_name': 'dvyajjkya',
    'api_key': '175875286981214',
    'api_secret': 'eCr01NCcCLgCVFWXLTA3ZCekCeA'
}

cloudinary.config(
    cloud_name=CLOUDINARY['cloud_name'],
    api_key=CLOUDINARY['api_key'],
    api_secret=CLOUDINARY['api_secret']
)
# from decouple import Config

# config = Config()

# CLOUDINARY = {
#     'cloud_name': config('CLOUDINARY_CLOUD_NAME'),
#     'api_key': config('CLOUDINARY_API_KEY'),
#     'api_secret': config('CLOUDINARY_API_SECRET')
# }

# cloudinary.config(
#     cloud_name=CLOUDINARY['cloud_name'],
#     api_key=CLOUDINARY['api_key'],
#     api_secret=CLOUDINARY['api_secret']
# )


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# DATABASES = {
#     "default": dj_database_url.parse("postgresql://adrian_user:NdDfYYQjDzQLDuAd8S9Iqy36EznkxrCU@dpg-cqie9n8gph6c738nsg80-a.oregon-postgres.render.com/adrian")
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = "diary.User"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'lifebook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
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

WSGI_APPLICATION = 'lifebook.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [BASE_DIR / "diary/static"]


MEDIA_ROOT = os.path.join(BASE_DIR, 'diary/media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'