"""Login and logout. Teacher registration is added in US-01 once the team decides who may register."""
from flask import redirect, request, session, url_for

from app.controllers.base_controller import BaseController
from app.models.user import User

GENERIC_LOGIN_ERROR = "Wrong email or password."


class AuthController(BaseController):
    def login(self):
        if request.method == "GET":
            return self.render("auth/login.html")

        email = request.form.get("email", "")
        password = request.form.get("password", "")
        user = User.find_by_email(email) if email else None
        if user is None or not user.active or not user.check_password(password):
            # Same message for every failure, so nobody can tell which emails exist (US-01)
            return self.render("auth/login.html", error=GENERIC_LOGIN_ERROR, email=email), 401

        session.clear()                       # fresh session on login
        session["user_id"] = user.id

        next_url = request.args.get("next", "")
        if not next_url.startswith("/") or next_url.startswith("//"):   # only our own pages
            next_url = url_for("main.home")
        return redirect(next_url)

    def logout(self):                         # POST only, so another site can't log people out
        session.clear()
        return redirect(url_for("auth.login"))
