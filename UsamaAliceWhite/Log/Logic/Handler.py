# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import dataclasses
import datetime
import logging
import logging.handlers
import pathlib
import threading

# Local Module
from ..Core import SingletonPattern

# --- HandlerFunction ---
@dataclasses.dataclass
class HandlerArgs:
    # console & size & time
    level: int = logging.DEBUG
    message_format: str = "%(asctime)s [%(levelname)-8s] %(name)-20s:%(funcName)-20s:%(lineno)-4d - %(message)s"
    datetime_format: str = "%Y-%m-%d %H:%M:%S"
    # size & time
    file_path: pathlib.Path | str = pathlib.Path.home() / "UsamaAliceWhite.log"
    backup_count: int = 10
    encoding: str | None = "utf-8"
    delay: bool = False
    errors: str | None = None
    # size
    mode: str = "a"
    max_bytes: int = 10 * 1024 * 1024
    # time
    when: str = "midnight"
    interval: int = 1
    utc: bool = False
    attime: datetime.time | None = None

class Handler(metaclass= SingletonPattern):
    _lock: threading.Lock = threading.Lock()

    def __init__(self, args: HandlerArgs = HandlerArgs()) -> None:
        self.args: HandlerArgs = args
        self.handler: logging.Handler | None = None

    def _setup_handler(self, handler: logging.Handler) -> None:
        handler.setLevel(level= self.args.level)
        handler.setFormatter(logging.Formatter(
            fmt= self.args.message_format,
            datefmt= self.args.datetime_format
        ))

    def _create_directory(self) -> None:
        directory_path: pathlib.Path = pathlib.Path(self.args.file_path).parent
        directory_path.mkdir(parents= True, exist_ok= True)

    def create_console_handler(self) -> logging.StreamHandler:
        if self.handler is None:
            with self._lock:
                if self.handler is None:
                    handler: logging.StreamHandler = logging.StreamHandler()
                    self._setup_handler(handler= handler)
                    self.handler: logging.StreamHandler = handler
        return self.handler
    
    def create_size_rotation_handler(self) -> logging.handlers.RotatingFileHandler:
        if self.handler is None:
            with self._lock:
                if self.handler is None:
                    self._create_directory()
                    handler: logging.handlers.RotatingFileHandler = \
                        logging.handlers.RotatingFileHandler(
                            filename= self.args.file_path,
                            mode= self.args.mode,
                            maxBytes= self.args.max_bytes,
                            backupCount= self.args.backup_count,
                            encoding= self.args.encoding,
                            delay= self.args.delay,
                            errors= self.args.errors
                        )
                    self._setup_handler(handler= handler)
                    self.handler: logging.handlers.RotatingFileHandler = handler
        return self.handler
    
    def create_time_rotation_handler(self) -> logging.handlers.TimedRotatingFileHandler:
        if self.handler is None:
            with self._lock:
                if self.handler is None:
                    self._create_directory()
                    handler: logging.handlers.TimedRotatingFileHandler = \
                        logging.handlers.TimedRotatingFileHandler(
                            filename= self.args.file_path,
                            when= self.args.when,
                            interval= self.args.interval,
                            backupCount= self.args.backup_count,
                            encoding= self.args.encoding,
                            delay= self.args.delay,
                            utc= self.args.utc,
                            atTime= self.args.attime,
                            errors= self.args.errors
                        )
                    self._setup_handler(handler= handler)
                    self.handler: logging.handlers.TimedRotatingFileHandler = handler
        return self.handler