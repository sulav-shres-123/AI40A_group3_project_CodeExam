"""All settings in one place (as in the module lesson), read from .env so no secret is in the code."""
import os

from dotenv import load_dotenv

load_dotenv()  # reads .env in the project root, if it exists

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is missing. Copy .env.example to .env and fill it in.")

# MySQL
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "codeexam")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "codeexam_dev")

# Judge0 (used from US-21)
JUDGE0_URL = os.getenv("JUDGE0_URL", "http://localhost:2358")

# Environment
APP_ENV = os.getenv("APP_ENV", "development")
DEBUG = APP_ENV != "production"

# Session cookie safety (US-11: HttpOnly, Secure, SameSite=Lax)
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = APP_ENV == "production"   # HTTPS only on the real server

# CSRF protection (Flask-WTF). Tests switch it off.
WTF_CSRF_ENABLED = True
