#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """ Configuration Babel 
        set default values
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Locale language

        Return:
            Best match to the language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Greeting

        Return:
            Initial template html
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")