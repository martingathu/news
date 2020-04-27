from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

#Initializing application
app = Flask(__name__, instance_relative_config = True)

from app import views

#Setting up configuration
app.config.from_object('config')









