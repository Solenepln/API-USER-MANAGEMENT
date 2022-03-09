from flask import Flask
from flask_restx import Namespace
from flask_restx import Api, Resource
from backend import app
from flask import request
from markupsafe import escape
from ..managers.user_manager import UserManager
from flask import render_template
import os

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

@app.route('/users/<username>', methods=['GET'])
def show_user_info(username):
    if username:
        found_username = UserManager.info_user(username)
    
    return render_template('user_info.html', found_username = found_username)
