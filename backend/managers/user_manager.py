from flask import Flask
from flask import request
import bcrypt
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
                hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                #create object
                user= User(username= new_username, password= hashed, name = new_name, firstname = new_firstname)
                db.session.add(user)
                db.session.commit()  
            
        users = User.query.all()
        table = (alert, users)
        return table

    @classmethod
    def info_user(self,username:str): 
        # found_username = 1  
        # if request.method == 'POST':
        #     research_username = request.args.get("username", "no one mentionned")
        #     found_username = User.query.filter_by(username = research_username).first()
            
        #     if found_username:
        #         found_username = found_username 
        # return found_username
        
        research_username = username
        found_username = User.query.filter_by(username = research_username).first()
            
        if found_username:
            found_username = found_username
        
        else:
            found_username = 1
        
        return found_username


    