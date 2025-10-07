
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)^z@*z#1xa73h^!^_%apk$7ti2-s1!@3jl&u041sjv4dt(ra*!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.55.129', '127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    #'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'core.apps.CoreConfig',
    #'django_jalali'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware',  
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # اگر پوشه templates داری
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # مسیر جمع‌آوری فایل‌های استاتیک

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



"""SIMPLEUI_DEFAULT_THEME = 'simpleui-x.css'  

SIMPLEUI_LOGO = 'https://i.imgur.com/xyz123.png'  
SIMPLEUI_HOME_TITLE = 'داشبورد مدیریت آوای هنر'
SIMPLEUI_HOME_INFO = False 
SIMPLEUI_ANALYSIS = False
SIMPLEUI_STATIC_OFFLINE = True

SIMPLEUI_CONFIG = {
    'system_keep': False,  
    'menus': [
        {
            'name': 'مدیریت آموزش',
            'icon': 'fas fa-school',
            'models': [
                {'name': 'اساتید', 'icon': 'fas fa-chalkboard-teacher', 'url': '/admin/core/teacher/'},
                {'name': 'هنرجویان', 'icon': 'fas fa-user-graduate', 'url': '/admin/core/student/'},
                {'name': 'کلاس‌ها', 'icon': 'fas fa-music', 'url': '/admin/core/class/'},
            ]
        },
        {
            'name': 'امور مالی',
            'icon': 'fas fa-credit-card',
            'models': [
                {'name': 'پرداخت‌ها', 'icon': 'fas fa-money-bill', 'url': '/admin/core/payment/'},
                {'name': 'شهریه‌ها', 'icon': 'fas fa-wallet', 'url': '/admin/core/tuition/'},
            ]
        },
        {
            'name': 'مدیریت سیستم',
            'icon': 'fas fa-cogs',
            'models': [
                {'name': 'کاربران', 'icon': 'fas fa-user', 'url': '/admin/auth/user/'},
                {'name': 'گروه‌ها', 'icon': 'fas fa-users-cog', 'url': '/admin/auth/group/'},
            ]
        }
    ]
}
"""