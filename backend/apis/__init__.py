from curses import flash
from functools import wraps
import os
from flask import Flask, redirect, url_for, session
from flask_session import Session
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
        return redirect(url_for('welcome_person'))

@api.route("/welcome")
class WelcomePerson(Resource):
    def get(self): 
        name = UserManager.welcome()
        return make_response(render_template("home.html", name_recover = name))

@api.route("/registration")
class SubscribePage(Resource):
    def get(self):
        _get = 1
        return make_response(render_template("registration.html", _get = _get))
    def post(self):
        alert = UserManager.create_user()
        return make_response(render_template("registration.html", alert=alert))

@api.route("/YourHome")
class PersonalHome(Resource):
    def get(self):
        return make_response(render_template("personal_page.html"))

@api.route("/logout")
class LogOut(Resource):
    def get(self):
        session["username"] = None
        return redirect(url_for("home_page"))

api.add_namespace(user_display, path="/users")
api.add_namespace(login_action, path="/login")