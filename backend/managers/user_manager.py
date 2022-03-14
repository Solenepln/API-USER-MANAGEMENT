from flask import Flask
from flask import request
import bcrypt
from ..models import db, User, Token
from uuid import uuid4
from sqlalchemy import insert
import smtplib
from email.message import EmailMessage
from datetime import datetime
 
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
    def display_users(self):
        db.create_all()
        db.session.commit()
        users = User.query.all()
        return users
   
    @classmethod
    def create_user(self):
        alert = None
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
            
        users = UserManager.display_users()
        result = (alert,users)
        
        return result

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
    def send_mail(self, mail:str, content:str):
        msg = EmailMessage()
        msg['Subject'] = "DO NOT REPLY"
        msg['From'] = "verify@gmail.com"
        msg['To'] = mail
        msg.set_content(content)
        server = smtplib.SMTP('22.0.6.248', 25)
        server.send_message(msg)
        server.quit()       

    @classmethod
    def login(self):
        password_success = 0
        connexion_userame = request.form.get('username')
        connexion_password = request.form.get('password')
            
        #check if username in db
        user = User.query.filter_by(username = connexion_userame).first()
        if user:
            username_success = 1  
            if bcrypt.checkpw(connexion_password.encode('utf8'), user.password):
                password_success = 1
                token = Token()
                user.token_value = token.value
                user.token_expiration = token.expiration
                db.session.commit()

                #send token to user
                UserManager.send_mail(user.mail,token.value)
            else:
                password_success = 0
        else:
            username_success = 0
        result = (password_success, username_success, user)
        return result

    @classmethod
    def check_token(self):
        connexion_time  = datetime.now().replace(microsecond=0)
        token_success = None  
        alert_username = None
        alert_connexion_latency = None
        connected_user = request.form.get('username')
        user = User.query.filter_by(username = connected_user).first()
        token_filled = request.form.get('token')

        if user:
            username = user.username
            #string format
            _date = user.token_expiration
            #datetime format
            expiration_token_date = datetime.strptime(_date, "%Y-%m-%d %H:%M:%S")
                
            if connexion_time < expiration_token_date:
                if user.token_value == token_filled:
                    token_success = 1
                else:
                    token_success = token_success                   
            else:
                alert_connexion_latency = 1
                token = Token()
                user.token_value = token.value
                user.token_expiration = token.expiration
                db.session.commit()
                UserManager.send_mail(user.mail,token.value)
        else:
            alert_username = 1
        result = (alert_username, alert_connexion_latency, token_success, username)
        return result




