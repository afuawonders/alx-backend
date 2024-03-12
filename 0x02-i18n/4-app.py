#!/usr/bin/env python3
"""Basic Babel setup
In this task, you will implement a way to
force a particular locale by passing the locale=fr
parameter to your app’s URLs.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """Configuration Babel
    set default values for languages Timezone and locale
            detect if the incoming request contains locale
            argument and ifs value is a supported locale,
            return it. If not or if the parameter is not
            present, resort to the previous default behavior.
            Best match to the language
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
            detect if the incoming request contains locale
            argument and ifs value is a supported locale,
            return it. If not or if the parameter is not
            present, resort to the previous default behavior.
            Best match to the language
    """
    locale = request.args.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Greeting

        Return:
            Initial template html
            detect if the incoming request contains locale
            argument and ifs value is a supported locale,
            return it. If not or if the parameter is not
            present, resort to the previous default behavior.
            Best match to the language
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
