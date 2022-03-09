from flask import Flask
from flask_restx import Namespace
from flask_restx import Api, Resource
from backend import app
from flask import request
from markupsafe import escape
from ..managers.user_manager import UserManager
from flask import render_template, make_response
import os

api = Namespace("login", description="login related")

@api.route("")
class UserLogin(Resource):
    def get (self):
        return make_response(render_template('login_home.html'))
    def post(self):
        access_user, alert_username, current_user = UserManager.login()
        return make_response(render_template('login.html', access_user = access_user, alert_username = alert_username))
    

@api.route('/token')
class UserToken(Resource):
    def post(self):
        result = UserManager.check_token()
        alert_username = result[0]
        alert_connexion_latency = result[1]
        token_success = result[2] 
        return make_response(render_template('token.html',alert_username = alert_username, alert_connexion_latency = alert_connexion_latency, token_success = token_success))
    
    def get(self):
        return make_response(render_template('home_token.html'))