"""URL for the home page → MainController."""
from flask import Blueprint

from app.auth import login_required
from app.controllers.main_controller import MainController


class MainRoutes:
    def __init__(self):
        self.bp = Blueprint("main", __name__)
        self.controller = MainController()

    def register(self):
        self.bp.add_url_rule("/", "home", login_required(self.controller.home))
        return self.bp
