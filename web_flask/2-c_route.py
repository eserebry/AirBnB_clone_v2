#!/usr/bin/python3
# starts a Flask web application

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def flask():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C %s' % text

if __name__ == "__main__":
    app.run(host="0.0.0.0")
