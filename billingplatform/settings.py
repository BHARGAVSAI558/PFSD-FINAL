"""
Django settings for the billingplatform project.
"""

import os
from pathlib import Path
import dj_database_url  # make sure this is in requirements
from dotenv import load_dotenv

# Load local .env in development only (optional)
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")  # optional, used for local dev

# SECURITY
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key-for-dev")
DEBUG = os.environ.get("DEBUG", "False").lower() in ("1", "true", "yes")

# On Render you should set ALLOWED_HOSTS to your render service's URL
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "billingapp",
    "adminportal",
    "customerportal",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # WhiteNoise right after SecurityMiddleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "billingplatform.urls"

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

WSGI_APPLICATION = "billingplatform.wsgi.application"

# DATABASE: use DATABASE_URL env var (Render provides this for Postgres)
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get(
            "DATABASE_URL",
            # local fallback (optional) -- keep as convenience for local Postgres use
            "postgres://opbmsuser:12345@localhost:5432/opbmsdb",
        ),
        conn_max_age=600,
        ssl_require=False,  # set True if your DB requires SSL
    )
}

# Password validators (keep as you had)
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files settings (collectstatic -> STATIC_ROOT)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # local development static dir
STATIC_ROOT = BASE_DIR / "staticfiles"    # collectstatic output (served by WhiteNoise)

# WhiteNoise recommended storage for production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Authentication redirects
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "customerportal:dashboard"
LOGOUT_REDIRECT_URL = "login"
