#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Return hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
