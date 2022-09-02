#!/usr/bin/env python3
"""
 Basic Flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_file():
    """ returns the contents of index.html in the flask application """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
