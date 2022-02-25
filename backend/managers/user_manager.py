from flask import Flask
from flask import request
from ..models import db, User

#utiliser une classe et enlever underscore 
class UserManager():
    @classmethod
    def hello(self):
        return "Hello!"

    @classmethod
    def welcome(self):
        #default valeur = unknown person
        #if get doesn't find key "name" in dict, it will return "unkwown person"
        name = request.args.get("name", "unknown person")
        #name_recover =name <=> variable = valeur 
        #name_recover is reused in welcome.html
        return name
    
    @classmethod
    def users_display(self):
        db.create_all()
        db.session.commit()
        alert = None
        if request.method == 'POST':
            #retrieve args
            new_username = request.form.get('username')
            new_password = request.form.get('password')
            new_name = request.form.get('name')
            new_firstname = request.form.get('firstname')

            same_username = User.query.filter_by(username = new_username).first()
            if same_username:
                alert = 1
            else:
                # secure_password = calcul_hash(new_password)
                #create object
                user= User(username= new_username, password= new_password, name = new_name, firstname = new_firstname)
                db.session.add(user)
                db.session.commit()  
            
        users = User.query.all()
        table = (alert, users)
        return table

    