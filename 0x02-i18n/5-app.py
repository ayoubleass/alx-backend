#!/usr/bin/env python3
"""
Basic flask app.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """
    Babel config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrives a user from the users dict.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    middleware that use get_user to find a user.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world() -> str:
    """
    Render a simple html page.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
