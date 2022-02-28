from flask import Flask
from backend import app
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
    page = UserManager.welcome()
    return render_template("welcome.html", name_recover = page)

@app.route('/users', methods=['GET', 'POST'])
def afficher_users():
    table_users = UserManager.users_display()
    alert = table_users[0]
    table = table_users[1]
    return render_template('users.html', alert=alert, users = table)

@app.route('/info', methods=['GET', 'POST'])
def informations_user():
    infos_user = UserManager.info_user()
    found_username = infos_user[0]
    users = infos_user[1]
    return render_template('user_info.html', found_username = found_username, users = users)

