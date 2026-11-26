"""App factory: builds the Flask app. The website, the worker and the tests all call create_app()."""
from flask import Flask, g, render_template
from flask_wtf.csrf import CSRFProtect

import config
from app.database import close_db

csrf = CSRFProtect()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(config)          # copies every UPPERCASE name from config.py
    if test_config:
        app.config.update(test_config)      # tests point at codeexam_test here

    csrf.init_app(app)                      # every POST needs a CSRF token
    app.teardown_appcontext(close_db)       # always close the DB connection
    # US-01 adds: app.before_request(load_current_user)

    @app.context_processor
    def inject_current_user():
        # Every template can use {{ current_user }} (None until US-01 adds login)
        return {"current_user": g.get("user")}

    _register_routes(app)
    _register_error_pages(app)
    return app


def _register_routes(app):
    from app.routes.main_routes import MainRoutes

    # Add one line per routes class as stories are built (US-01 adds AuthRoutes).
    for routes in (MainRoutes(),):
        app.register_blueprint(routes.register())


def _register_error_pages(app):
    @app.errorhandler(403)
    def forbidden(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template("errors/500.html"), 500
