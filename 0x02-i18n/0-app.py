#!/usr/bin/env python3
"""
Basic flask app.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Render a simple html page.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
