from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

#initializing application
app = Flask(__name__, instance_relative_config = True)

from app import views

#setting up configuration
app.config.from_object('config')









