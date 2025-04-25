import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True

class ProductionConfig(Config):
    """Uses production database server."""
    # TODO: Change to production database server
    DEBUG = False
    DB_SERVER = '10.91.221.46'
    DB_PORT = '5432'
    ENV = 'production'
    SECRET_KEY = 'lTacSAjgOmVVAI2YP60g'
    DB_NAME = 'KidneyBioDB'
    USER = 'postgres'
    KEY = 'Ying17876'
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        sqluri = 'postgresql://{}:{}@{}:{}/{}'.format(self.USER, self.KEY, self.DB_SERVER, self.DB_PORT, self.DB_NAME)
        return sqluri
    

class DevelopmentConfig(Config):
    DEBUG = True
    DB_SERVER = 'localhost'
    DB_PORT = '5432'
    ENV = 'development'
    SECRET_KEY = 'lTacSAjgOmVVAI2YP60g'
    DB_NAME = 'KidneyBioDB'
    USER = 'postgres'
    KEY = '3'
    

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        sqluri = 'postgresql://{}:{}@{}:{}/{}'.format(self.USER, self.KEY, self.DB_SERVER, self.DB_PORT, self.DB_NAME)
        return sqluri