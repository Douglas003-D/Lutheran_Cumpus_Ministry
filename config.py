import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    # --- SECURITY ---
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    
    # --- DATABASE ---
    # Using MySQL as specified in system requirements
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = os.environ.get('MYSQL_DB')
    
    # --- FILE HANDLING ---
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # --- EMAIL SETTINGS ---
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False').lower() == 'true'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')

    # --- MPESA SETTINGS ---
    # These will now use the credentials and the Pinggy tunnel URL from your .env
    MPESA_CONSUMER_KEY = os.environ.get('MPESA_CONSUMER_KEY')
    MPESA_CONSUMER_SECRET = os.environ.get('MPESA_CONSUMER_SECRET')
    MPESA_SHORTCODE = os.environ.get('MPESA_SHORTCODE')
    MPESA_PASSKEY = os.environ.get('MPESA_PASSKEY')
    
    # This now pulls: https://lvnop-...-free.link/mpesa-callback
    MPESA_CALLBACK_URL = os.environ.get('MPESA_CALLBACK_URL')
    
    MPESA_ENV = os.environ.get('MPESA_ENV', 'sandbox').lower()
    
    # Base URL determined by Environment
    if MPESA_ENV == 'live':
        MPESA_BASE_URL = "https://api.safaricom.co.ke"
    else:
        MPESA_BASE_URL = "https://sandbox.safaricom.co.ke"

    # --- SETUP & SECURITY ---
    SETUP_TOKEN = os.environ.get('SETUP_TOKEN')