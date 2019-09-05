"""
Project: Jinja2-ExploitMe
File: app.py
---
Launch w/ Live Reload:
export FLASK_ENV=development; flask run
"""

import os
from flask import Flask, render_template, render_template_string, request


app = Flask(__name__)


@app.route("/")
def index():
    """
    This route is vulnerable to Server Side Template Injection attacks.
    Your goal is to exploit it in as many ways as possible.
    Once you've found at least two (2) exploits, share your findings with a peer.
    Finally, fix this code so that this route is no longer exploitable.
    """
    exploit_filter = request.args.get('exploit')
    if exploit_filter != None:
        if "{{" or "<script>" in exploit_filter:
            exploit_filter = "Oy! You there! What are you tring to do? Thought I wouldn't notice, didn't you?"
    exploit = exploit_filter
    rendered_template = render_template("app.html", exploit=exploit)
    return render_template_string(rendered_template)


if __name__ == "__main__":
    app.run(debug=True, port=4444)
