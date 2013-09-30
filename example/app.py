#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_yamlpage import FlaskYamlPage


app = Flask(__name__)
yamlpages = FlaskYamlPage(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
