"""Home page. A placeholder until the real dashboards (US-10 teacher, US-12 student, US-29 admin)."""
from app.controllers.base_controller import BaseController


class MainController(BaseController):
    def home(self):
        return self.render("home.html")
