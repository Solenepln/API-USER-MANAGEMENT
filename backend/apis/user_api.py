from flask import Flask
from sqlalchemy.sql.expression import table
from backend import app
from flask import request
from markupsafe import escape
from ..managers.user_manager import UserManager
from flask import render_template
import os

@app.route('/')
def hello():
    hello_display = UserManager.hello()
    return render_template("home.html")

@app.route('/welcome', methods=['GET'])
def welcome_page():
    name = UserManager.welcome()
    return render_template("welcome.html", name_recover = name)

@app.route('/users', methods=['GET', 'POST'])
def afficher_users():
    #database with users
    table = UserManager.users_display()
    alert = table[0]
    users = table[1]
    return render_template('users.html', alert=alert, users = users)

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
        table = UserManager.login()
        access_user = table[0]
        alert_username = table[1]
        current_user = table[2]
        return render_template('login.html', access_user = access_user, alert_username = alert_username)
    else:
        return render_template('login_home.html')

@app.route('/login/token', methods=['GET', 'POST'])
def token():
    if request.method == 'POST':
        table = UserManager.check_token()
        alert_username = table[0]
        alert_connexion_latency = table[1]
        token_success = table[2] 
        return render_template('token.html',alert_username = alert_username, alert_connexion_latency = alert_connexion_latency, token_success = token_success, )
    else:
        return render_template('home_token.html')