# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import logging
import threading


# --- Logger Manager ---
class GetLogger:
    """
    Purpose:
        Retrieves or creates a logger with the specified handler and name.
    Arguments:
        handler= The logging handler to attach to the logger.
        name= The name identifier for the logger.
    Returns:
        logging.Logger= The configured logger instance.
    """
    _lock: threading.Lock = threading.Lock()

    def __new__(cls, handler: logging.Handler, name: str) -> logging.Logger:
        with cls._lock:
            logger: logging.Logger = logging.getLogger(name= name)
            if handler not in logger.handlers:
                logger.setLevel(level= logging.DEBUG)
                logger.addHandler(hdlr= handler)
                logger.propagate = False
        return logger