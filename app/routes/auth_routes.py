"""URLs for login and logout → AuthController methods."""
from flask import Blueprint

from app.auth import login_required
from app.controllers.auth_controller import AuthController


class AuthRoutes:
    def __init__(self):
        self.bp = Blueprint("auth", __name__)
        self.controller = AuthController()

    def register(self):
        self.bp.add_url_rule("/login", "login", self.controller.login, methods=["GET", "POST"])
        self.bp.add_url_rule("/logout", "logout", login_required(self.controller.logout), methods=["POST"])
        return self.bp
