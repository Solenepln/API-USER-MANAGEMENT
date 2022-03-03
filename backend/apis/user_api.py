from flask import Flask
from backend import app
from flask import request
from markupsafe import escape
from ..managers.user_manager import UserManager
from flask import render_template
import os

@app.route('/')
def hello():
    hello_display = UserManager.hello()
    return hello_display

@app.route('/welcome', methods=['GET'])
def welcome_page():
    name = UserManager.welcome()
    return render_template("welcome.html", name_recover = name)

@app.route('/users', methods=['GET', 'POST'])
def afficher_users():
    #database with users
    table_users = UserManager.users_display()
    alert = table_users[0]
    table = table_users[1]
    return render_template('users.html', alert=alert, users = table)

@app.route('/users/')
def look_for_user_info():
    return render_template('user_info.html')

# @app.route('/users', defaults={'username': None})  
@app.route('/users/<username>', methods=['GET'])
def show_user_info(username):
    if username:
        found_username = UserManager.info_user(username)
    
    return render_template('user_info.html', found_username = found_username)

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        success_login = UserManager.login()
        access_user = success_login[0]
        alert_username = success_login[1]
        current_user = success_login[2]
        
        return render_template('login.html', access_user = access_user, alert_username = alert_username)
    else:
        return render_template('login_home.html')

@app.route('/login/token', methods=['GET', 'POST'])
def token():
    if request.method == 'POST':
        success_token = UserManager.check_token()
        token_success = success_token[0]
        alert_username = success_token[1]
        return render_template('token.html',token_success = token_success, alert_username = alert_username)
    else:
        return render_template('home_token.html')