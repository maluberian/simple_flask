import os

from fastapi import FastAPI
import uvicorn

import logging
from BoopyStructuredLogFormatter import BoopyStructuredLogFormatter

from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)
formatter = BoopyStructuredLogFormatter()
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()

@app.get('/test/{id}')
def test(id: str):
    val = os.getenv("test_val")
    logger.error(f"Hello {id}!", extra={ 'test': 'value', 'val': val })
    return {"message": id}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)