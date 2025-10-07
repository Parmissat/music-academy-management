from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# تنظیمات پنل مدیریت
ADMIN_SITE_HEADER = "مدیریت آموزشگاه موسیقی"
ADMIN_SITE_TITLE = "پنل مدیریت"
ADMIN_INDEX_TITLE = "به سیستم مدیریت آموزشگاه خوش آمدید"

# مسیر پایه پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# امنیت
SECRET_KEY = 'django-insecure-yk2e3_4d_yfn=)by$%w0uosmg-(95)45x)!j!vaeh0=hjc$d8%'
DEBUG = True
ALLOWED_HOSTS = []

# اپلیکیشن‌ها
INSTALLED_APPS = [
   #'jazzmin',   # فعال کردن در صورت نیاز
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'jalali_date',
    'core.apps.CoreConfig',
]

JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            'admin/js/django_jalali.min.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

# میان‌افزارها
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# مسیر اصلی URLها
ROOT_URLCONF = 'academy.urls'

# قالب‌ها
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
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

# WSGI
WSGI_APPLICATION = 'academy.wsgi.application'

# پایگاه داده
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# اعتبارسنجی رمز عبور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# بین‌المللی‌سازی
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# فایل‌های استاتیک و مدیا
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'core/static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# کلید پیش‌فرض
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
