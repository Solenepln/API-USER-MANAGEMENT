import os
from flask import Flask
from flask_restx import Api, Resource, Namespace
from backend import app
from flask import request, render_template
from markupsafe import escape
from ..managers.user_manager import UserManager

api = Api(app)

# @app.route('/')
# def hello():
#     hello_display = UserManager.hello()
#     return render_template("home.html")

@api.route('/welcome')
class WelcomeHome(Resource):
    def get(self):
        return "hello API!"
        # name = UserManager.welcome()
        # return render_template("welcome.html", name_recover = name)