from . import db
from uuid import uuid4
from datetime import datetime, timedelta
from time import sleep

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    mail = db.Column(db.String(80), nullable=False)
    token_value = db.Column(db.String(100), nullable=True)
    token_expiration = db.Column(db.String(100), nullable=True)


    def __repr__(self):
        #return 'Username: %r Name: %r Firstname: %r' (self.username,self.name,self.firstname) 
        return f'Username: {self.username}, Name:{self.name}, Firstname:{self.firstname}'

def token_generated():
        id_generated = str(uuid4())
        return id_generated

class Token(): 
    def __init__(self):
        self.value = token_generated()
        self.expiration = datetime.now().replace(microsecond=0) + timedelta(minutes=10)
        
    def __repr__(self):
        #return 'Value: %r Date: %r' (self.value,self.expiration)
        return f'Value: {self.value}, Date: {self.expiration}'





