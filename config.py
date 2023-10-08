import os 
from dotenv import load_dotenv 
from datetime import timedelta 



basedir = os.path.abspath(os.path.dirname(__file__)) 

load_dotenv(os.path.join(basedir, '.env'))

class Config():


    FLASK_APP = os.environ.get('FLASK_APP') 
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = True 
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Capstone Project" 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  