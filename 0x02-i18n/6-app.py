#!/usr/bin/env python3
"""
Use user locale
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ sets up default configurations for babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('3-app.Config')
"""sets all the defaults in class config """


@babel.localeselector
def get_locale():
    """ Use user locale """
    localLanguage = request.args.get('locale')
    userId = request.args.get('login_as')
    if userId:
        localLanguage = users[int(userId)]['locale']
        if localLanguage in app.config['LANGUAGES']:
            return localLanguage
    localLanguage = request.headers.get('locale')
    if localLanguage in app.config['LANGUAGES']:
        return localLanguage
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_template():
    """ gets index file for the flask app """
    return render_template('5-index.html')


def get_user():
    """ gets user id from the link or arg """
    if request.args.get('login_as'):
        userId = int(request.args.get('login_as'))
        if userId in users:
            return users.get(userId)
    else:
        return None

@app.before_request
def before_request():
    """ uses =>get_user() to get user if any """
    g.user = get_user()


if __name__ == '__main__':
    app.run()


