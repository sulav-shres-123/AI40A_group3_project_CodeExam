"""URL for the home page → MainController."""
from flask import Blueprint

from app.controllers.main_controller import MainController


class MainRoutes:
    def __init__(self):
        self.bp = Blueprint("main", __name__)
        self.controller = MainController()

    def register(self):
        # US-01 wraps this in login_required
        self.bp.add_url_rule("/", "home", self.controller.home)
        return self.bp
