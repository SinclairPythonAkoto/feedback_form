from flask import flash, session, redirect, url_for
from functools import wraps


def login_required(func):
    """Redirect user to login page if not logged in"""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get("logged_in") is None:
            flash("You need to log in first")
            return redirect(url_for("login"))
        return func(*args, **kwargs)

    return decorated_function
