from flask import Flask, redirect
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
        _get = 1
        return make_response(render_template('login.html', _get = _get))
    def post(self):
        connexion = UserManager.login()
        password_success = connexion[0]
        username_success = connexion[1]  
        return make_response(render_template('login.html', password_success = password_success, username_success = username_success))
    
@api.route('/token')
class UserToken(Resource):
    def get(self):
        _get = 1
        return make_response(render_template('token.html', _get = _get))

    def post(self):
        result = UserManager.check_token()
        alert_username = result[0]
        alert_connexion_latency = result[1]
        token_success = result[2]

        if token_success:
            return make_response(redirect(render_template('personal_page.html')))
        else:
            return make_response(render_template('token.html',alert_username = alert_username, alert_connexion_latency = alert_connexion_latency, token_success = token_success))