from flask import Flask
from flask import request
import bcrypt
from ..models import db, User
from uuid import uuid4
from sqlalchemy import insert
import smtplib
from email.message import EmailMessage

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
            new_mail = request.form.get('mail')
            

            same_username = User.query.filter_by(username = new_username).first()
            if same_username:
                alert = 1
            else:
                hashed = bcrypt.hashpw(new_password.encode('utf8'), bcrypt.gensalt())
                #create object
                user= User(username = new_username, password = hashed, name = new_name, firstname = new_firstname, mail = new_mail)
                db.session.add(user)
                db.session.commit()  
            
        users = User.query.all()
        
        return alert,users

    @classmethod
    def info_user(self,username:str):  
        research_username = username
        found_username = User.query.filter_by(username = research_username).first()
            
        if found_username:
            found_username = found_username
        
        else:
            found_username = 1
        
        return found_username

    @classmethod
    def token_generated(self):
        id_generated = str(uuid4())
        return id_generated

    @classmethod
    def login(self):
        alert_username = None
        access = None
        token_success = None
        users = User.query.all()

        if request.method == 'POST':
            connexion_userame = request.form.get('username')
            connexion_password = request.form.get('password')
            
            #check if username in db
            current_user = User.query.filter_by(username = connexion_userame).first()
            if current_user:  
                if bcrypt.checkpw(connexion_password.encode('utf8'), current_user.password):
                    access = 1
                    #update token for current_user
                    token = UserManager.token_generated()
                    current_user.token = token
                    db.session.commit()

                    #send token to current_user
                    msg = EmailMessage()
                    msg['Subject'] = "DO NOT REPLY"
                    msg['From'] = "verify@gmail.com"
                    msg['To'] = current_user.mail
                    msg.set_content(token)
                    server = smtplib.SMTP('22.0.6.248', 25)
                    server.send_message(msg)
                    server.quit()       
                else:
                    access = 0
            else:
                alert_username = 1
        return access, alert_username, current_user

    @classmethod
    def check_token(self):
        token_success = None  
        alert_username = None
        if request.method == 'POST':
            connected_user = request.form.get('username')
            user = User.query.filter_by(username = connected_user).first()
            token_filled = request.form.get('token')

            if user:
                if user.token == token_filled:
                    token_success = 1
            else:
                alert_username = 1
        return token_success, alert_username
