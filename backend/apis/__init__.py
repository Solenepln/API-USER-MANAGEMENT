import os
from flask import Flask, redirect, url_for
from flask_restx import Api, Resource, Namespace
from backend import app
from flask import request, render_template, make_response
from ..managers.user_manager import UserManager

from .user_api import api as user_display
from .login_api import api as login_action

api = Api(
    title = "User Management"
)

# @api.route("")
# def test():
#     return 'hello'

@api.route("/home")
class HomePage(Resource):
    def get(self):
        hello_display = UserManager.hello()
        return make_response(render_template("home.html"))
        
@api.route("/welcome")
class WelcomePerson(Resource):
    def get(self): 
        name = UserManager.welcome()
        return make_response(render_template("welcome.html", name_recover = name))


api.add_namespace(user_display, path="/users")
api.add_namespace(login_action, path="/login")