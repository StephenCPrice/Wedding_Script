from dotenv import load_dotenv
import os
'''import sshtunnel

from dbssh import create_ssh_tunnel'''

load_dotenv("creds.env")


class Config:
    """Base config."""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    #SQLALCHEMY_DATABASE_URI = dbssh.py
    SQLALCHEMY_POOL_RECYCLE = 280
    STATIC_FOLDER='static'
    TEMPLATES_FOLDER = 'templates'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_DEBUG = True
    
#Connecting to the database requires a tunnel to be created when remote 
class devConfig(Config):
    """Development config."""
    ENV = 'development'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"{os.environ.get('dev_mysql_creds')}"
    SQLALCHEMY_POOL_RECYCLE = 280

class serverConfig(Config):
    """Local config."""
    ENV = 'local'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("mysql_creds")