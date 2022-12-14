#!/usr/bin/env python3
"""
babel setup
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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
    """ looks for french language to use from the given objects """
    localLanguage = request.args.get('locale')

    if localLanguage in app.config['LANGUAGES']:
        return localLanguage
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_template():
    """ gets index file for the flask app """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()


