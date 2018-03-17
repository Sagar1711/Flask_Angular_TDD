import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #...
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:byte1711@localhost/flask-app"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    