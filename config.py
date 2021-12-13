import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    DB_SERVER = '10.91.221.46'
    DB_PORT = '5432'
    ENV = 'development'

    @property
    def DATABASE_URI(self):
        return 'postgresql://postgres:3@{}/KidneyBioDB'.format(self.DB_SERVER)
