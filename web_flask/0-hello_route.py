#!/usr/bin/python3
# starts a Flask web application

from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    @app.route('/', strict_slashes=False)
    def hello_flask():
        return 'Hello HBNB!'

    app.run(host="0.0.0.0", port="5000")
