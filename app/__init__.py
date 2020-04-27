from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

#initializing application
def create_app(config_name):
    app = Flask(__name__)
    
    #setting up configuration
    app.config.from_object(DevConfig)
    app.config.from_pyfile('config.py')

    return app








