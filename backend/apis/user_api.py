from flask import Flask
from backend import app
from markupsafe import escape
from ..managers.user_manager import UserManager
# from ..managers import user_manager
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

