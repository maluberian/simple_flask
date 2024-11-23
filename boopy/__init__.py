from flask import Flask

import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)

formatter = jsonlogger.JsonFormatter()
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)
@app.route('/')
def hello_world():
    logger.info('Hello World!', extra={ 'test': 'value'})
    return "<p>Hello World! Take 2</p>"

