from curses import flash
from functools import wraps
from flask import Flask, session, request, render_template, make_response, redirect, url_for
from flask_session import Session
from flask_restx import Namespace
from flask_restx import Api, Resource
from backend import app
from ..managers.user_manager import UserManager
import os
from ..utils import login_required
  
api = Namespace("users", description="user related")

@api.route("")
class UserApi(Resource):
    @login_required
    def get(self):
        #database with users
        users = UserManager.display_users()
        return make_response(render_template('users.html', users = users))

@api.route("/")
class InfosUser(Resource):
    @login_required
    def get(self):
        username_missing = 1
        return make_response(render_template('user_info.html', username_missing = username_missing))

@api.route('/<username>')
class InfosUserKnown(Resource):
    @login_required
    def get(self,username):
        alert_rights = 0
        found_username = None
        if username == session["username"]:
            found_username = UserManager.info_user(username)
        else:
            alert_rights = 1
        return make_response(render_template('user_info.html', alert_rights = alert_rights, found_username = found_username))
