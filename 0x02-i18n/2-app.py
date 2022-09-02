#!/usr/bin/env python3
"""
babel setup
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ sets up default confugarions for babel """
    
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_oject('1-app.Config')
"""sets all the defaults in class config """


@babel.localeselector
def get_locale():
    """ looks for the best language to use from the given objects """
    request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def get_template():
    """ gets index file for the flask app """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
