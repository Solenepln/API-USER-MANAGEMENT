from flask import Flask
from flask_restx import Namespace
from flask_restx import Api, Resource
from backend import app
from flask import request
from ..managers.user_manager import UserManager
from flask import render_template, make_response
import os

api = Namespace("users", description="user related")

@api.route("")
class UserApi(Resource):
    def get(self):
        #database with users
        users = UserManager.display_users()
        return make_response(render_template('users.html', users = users))

@api.route("/")
class InfosUser(Resource):
    def get(self):
        return make_response(render_template('user_info.html'))

@api.route('/<username>')
class InfosUserKnown(Resource):
    def get(self,username):
        if username:
            found_username = UserManager.info_user(username)  
        return make_response(render_template('user_info.html', found_username = found_username))
