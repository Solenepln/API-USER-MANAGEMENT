from flask import Flask
from flask_restx import Namespace
from flask_restx import Api, Resource
from backend import app
from flask import request
from markupsafe import escape
from ..managers.user_manager import UserManager
from flask import render_template
import os

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        access_user, alert_username, current_user = UserManager.login()
        return render_template('login.html', access_user = access_user, alert_username = alert_username)
    else:
        return render_template('login_home.html')

@app.route('/login/token', methods=['GET', 'POST'])
def token():
    if request.method == 'POST':
        result = UserManager.check_token()
        alert_username = result[0]
        alert_connexion_latency = result[1]
        token_success = result[2] 
        return render_template('token.html',alert_username = alert_username, alert_connexion_latency = alert_connexion_latency, token_success = token_success, )
    else:
        return render_template('home_token.html')