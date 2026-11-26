"""Who is logged in, and decorators that protect pages: login_required, role_required, admin_required."""
from functools import wraps

from flask import abort, g, jsonify, redirect, request, session, url_for

from app.models.user import User


def load_current_user():
    """Runs before every request (registered in create_app)."""
    user_id = session.get("user_id")
    g.user = User.find_by_id(user_id) if user_id else None
    if g.user is not None and not g.user.active:   # deactivated users are logged out at once
        session.clear()
        g.user = None


def _wants_json():
    return request.path.startswith("/api/")


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if g.user is None:
            if _wants_json():
                return jsonify(error="login_required", message="Please log in."), 401
            return redirect(url_for("auth.login", next=request.path))
        return view(*args, **kwargs)
    return wrapped


def role_required(*roles):
    """Use like:  @role_required("teacher", "admin")"""
    def decorator(view):
        @wraps(view)
        @login_required
        def wrapped(*args, **kwargs):
            if g.user.role not in roles:
                if _wants_json():
                    return jsonify(error="forbidden", message="You don't have access to this."), 403
                abort(403)
            return view(*args, **kwargs)
        return wrapped
    return decorator


def admin_required(view):
    """Kept so the lesson's name still works."""
    return role_required("admin")(view)
