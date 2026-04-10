# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import logging
import threading


# --- LoggerFunction ---
class GetLogger:
    _lock: threading.Lock = threading.Lock()

    def __new__(cls, handler: logging.Handler, name: str, level: int) -> logging.Logger:
        with cls._lock:
            logger: logging.Logger = logging.getLogger(name= name)
            if handler not in logger.handlers:
                logger.setLevel(level= level)
                logger.addHandler(hdlr= handler)
                logger.propagate = False
        return logger