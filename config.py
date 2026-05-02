import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # --- SECURITY ---
    SECRET_KEY = os.environ.get('SECRET_KEY', 'lcm_secret_key_2026')
    
    # --- DATABASE ---
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Harryd')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'LCM')
    
    # --- FILE HANDLING ---
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # --- EMAIL SETTINGS ---
    MAIL_SERVER = os.environ.get('MAIL_HOST', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 465))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'True').lower() == 'true'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'False').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')

    # --- MPESA SETTINGS (DARAJA API) ---
    MPESA_CONSUMER_KEY = os.environ.get('MPESA_CONSUMER_KEY')
    MPESA_CONSUMER_SECRET = os.environ.get('MPESA_CONSUMER_SECRET')
    MPESA_SHORTCODE = os.environ.get('MPESA_SHORTCODE')
    MPESA_PASSKEY = os.environ.get('MPESA_PASSKEY')
    MPESA_CALLBACK_URL = os.environ.get('MPESA_CALLBACK_URL')
    
    # Logic to switch between Sandbox and Production automatically
    # In .env, set MPESA_ENV='live' when you go to production
    MPESA_ENV = os.environ.get('MPESA_ENV', 'sandbox').lower()
    
    if MPESA_ENV == 'live':
        MPESA_BASE_URL = "https://api.safaricom.co.ke"
    else:
        MPESA_BASE_URL = "https://sandbox.safaricom.co.ke"

    # ... your existing database and mail settings ...
    SETUP_TOKEN = os.getenv('SETUP_TOKEN', 'l-c-m') # Uses .env, defaults to l-c-m