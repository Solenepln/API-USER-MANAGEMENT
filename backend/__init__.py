from flask import Flask


app = Flask(__name__)

#SQL ALCHEMY CONFIGURATION
#use protocole sqlite, va chercher au format sqlite le fichier test.db qui a tel chemin
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from .models import db
db.init_app(app)

from .apis.user_api import *



