"""
The flask application package.
"""

from flask import Flask

app = Flask(__name__)

import polls_web_app.views
