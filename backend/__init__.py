'''app entry point'''
from flask import Flask

app = Flask(__name__)

#SQL ALCHEMY CONFIGURATION
#use protocole sqlite, va chercher au format sqlite le fichier test.db qui a tel chemin
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SESSION CONFIGURATION
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

from .models import db
db.init_app(app)

from .apis.user_api import *

from .apis import api
api.init_app(app)


Session(app)



