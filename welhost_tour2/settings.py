"""
Django settings for welhost_tour2 project.
آخر تحديث: 19 يونيو 2025
"""
from pathlib import Path
import os
from datetime import timedelta

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# الأمان (Security)
# --------------------------------------------------
# ⚠️ في بيئة الإنتاج يُفضَّل جلب المفتاح من المتغيرات البيئية
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-pzjqgm#d7ycb^(!frsym(y1=60owz)441&aw84)m8)gg@$n*)0"
)

# DEBUG يُفترض إيقافه في الإنتاج
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

# النطاقات المسموح بها
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")

# --------------------------------------------------
# التطبيقات المثبَّتة
# --------------------------------------------------
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # أطراف ثالثة
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",  # JWT
    "corsheaders",                               # CORS (اختياري)

    # تطبيقات المشروع
    "accounts",
    "bookings",
    "services",
]

# --------------------------------------------------
# ميدل وير
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",          # قبل SessionMiddleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------
# عناوين CORS (اختياري)
# --------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# --------------------------------------------------
# عناوين المشروع
# --------------------------------------------------
ROOT_URLCONF = "welhost_tour2.urls"

# --------------------------------------------------
# القوالب (Templates)
# --------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "welhost_tour2.wsgi.application"

# --------------------------------------------------
# قاعدة البيانات (SQLite للتطوير فقط)
# --------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --------------------------------------------------
# نموذج المستخدم المخصص
# --------------------------------------------------
AUTH_USER_MODEL = "accounts.User"

# --------------------------------------------------
# التحقق من كلمات المرور
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------
# إعدادات Django REST Framework
# --------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
}

# إعدادات JWT الأساسية
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
}

# --------------------------------------------------
# اللغة والوقت
# --------------------------------------------------
LANGUAGE_CODE = "ar-sa"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# ملفات الستاتيك
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# --------------------------------------------------
# ملفات الوسائط (للصور المرفوعة)
# --------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------
# نوع المفتاح الافتراضي للجداول
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------
# التسجيل (Logging) – يُسهِّل تتبُّع الأخطاء
# --------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
