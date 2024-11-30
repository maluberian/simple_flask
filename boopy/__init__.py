import os

from flask import Flask

import logging
from BoopyStructuredLogFormatter import BoopyStructuredLogFormatter

from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)
formatter = BoopyStructuredLogFormatter()
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)
@app.route('/')
def hello_world():
    val = os.getenv("test_val")
    logger.error('Hello World!', extra={ 'test': 'value', 'val': val })
    return f"<p>Hello {val}!</p>"

