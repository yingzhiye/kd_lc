import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True

class ProductionConfig(Config):
    """Uses production database server."""
    # TODO: Change to production database server
    

class DevelopmentConfig(Config):
    DEBUG = True
    DB_SERVER = '10.91.221.46'
    DB_PORT = '5432'
    ENV = 'development'
    SECRET_KEY = 'lTacSAjgOmVVAI2YP60g'

    @property
    def DATABASE_URI(self):
        return 'postgresql://postgres:3@{}/KidneyBioDB'.format(self.DB_SERVER)
