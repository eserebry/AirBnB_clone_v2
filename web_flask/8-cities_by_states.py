#!/usr/bin/python3
# starts a Flask web application

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def flask():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
def python_is():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_is_magic(text='is_cool'):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def int_only(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    if n % 2 == 0:
        num = 'even'
    else:
        num = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, num=num)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
