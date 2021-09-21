import os

class Config:
  '''
  General configuration parent class
  '''
  SECRET_KEY = 'SECRET'
  
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST ='app/static/photos'

  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")    

class ProdConfig(Config):
  '''
  Production configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  

class TestConfig(Config):
  '''
  Testing configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:12345678@localhost/pitches'
  DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'test': TestConfig }
