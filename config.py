import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://ficapostgres:Beni1982@localhost:5432/ficaflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
