# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "balde moudjitaba!"


if __name__ == "__main__": 
    app.run()
