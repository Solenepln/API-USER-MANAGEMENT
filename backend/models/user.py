from . import db

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return 'Username: %r Name: %r Firstname: %r' % (self.username,self.name,self.firstname) 