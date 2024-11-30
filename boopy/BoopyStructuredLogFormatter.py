import logging
from datetime import datetime, timezone
from typing import Dict, Any

from pythonjsonlogger import jsonlogger

class BoopyStructuredLogFormatter(jsonlogger.JsonFormatter):
    def  __init__(self, *args, **kwargs) -> None:
        super().__init__(args, kwargs)

    def add_fields(self, log_record: Dict[str, Any], record: logging.LogRecord, message_dict: Dict[str, Any]) -> None:
        super().add_fields(log_record, record, message_dict)

        log_record['timestamp'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        log_record['level'] = record.levelname
        log_record['logger_name'] = record.name