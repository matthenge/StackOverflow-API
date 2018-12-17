import os

class Config():
    """The main configuration class"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    

class DevtConfiguration(Config):
    """The development configuration class"""
    DEBUG = True
    TESTING = True

class ProdConfiguration(Config):
    """The production configuration"""
    DEBUG = False
    TESTING = False  

class TestConfiguration(Config):
    DEBUG = True
    TESTING = True
    
configuration = {
    "devt": DevtConfiguration,
    "prod": ProdConfiguration,
    "test": TestConfiguration
}