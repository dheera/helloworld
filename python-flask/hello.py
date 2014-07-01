#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<path:path>')
def hello_path(path):
    return 'Hello {}!'.format(path)

if __name__ == '__main__':
    app.run()
