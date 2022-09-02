#!/usr/bin/env python3
"""
babel setup
"""

from flask import Flask, render_template
import flask_babel import Babel
from babel.dates import UTC

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ sets up default confugarions for babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_oject(Config)
"""sets all the defaults in class config """

@app.route('/')
def get_template():
    """ gets index file for the flask app """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
