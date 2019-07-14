"""
The flask application package.

cloned __init__py here to seemlesly run it in Azure
"""

from flask import Flask

app = Flask(__name__)

import polls_web_app.views
