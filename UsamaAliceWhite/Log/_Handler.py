# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import dataclasses
import datetime
import logging
import logging.handlers
import pathlib
import threading

# Local Module
from .Core import SingletonPattern


# --- Console Handler Manager ---
@dataclasses.dataclass(frozen= True)
class ConsoleHandlerArguments:
    level: int
    message_format: str
    datetime_format: str

class ConsoleHandler(metaclass= SingletonPattern):
    """
    Purpose:
        Manages a singleton console logging handler.
    Arguments:
        args= The configuration arguments for the handler.
    Returns:
        typing.Self= The singleton instance of ConsoleHandler.
    """
    _lock: threading.Lock = threading.Lock()

    def __init__(self, args: ConsoleHandlerArguments) -> None:
        self.args: ConsoleHandlerArguments = args
        self.handler: logging.StreamHandler | None = None
    
    def create(self) -> logging.StreamHandler:
        """
        Purpose:
            Retrieves or creates the console handler.
        Arguments:
            None= None.
        Returns:
            logging.StreamHandler= The configured console handler.
        """
        if self.handler is None:
            with self._lock:
                if self.handler is None:
                    handler: logging.StreamHandler = logging.StreamHandler()
                    handler.setLevel(level= self.args.level)
                    handler.setFormatter(
                        fmt= logging.Formatter(
                            fmt= self.args.message_format,
                            datefmt= self.args.datetime_format
                        )
                    )
                    self.handler = handler
        return self.handler


# --- FileSizeRotation Handler Manager ---
@dataclasses.dataclass(frozen= True)
class FileSizeRotationHandlerArguments:
    level: int
    message_format: str
    datetime_format: str
    mode: str
    max_bytes: int
    file_path: pathlib.Path | str
    backup_count: int
    encoding: str | None
    delay: bool
    errors: str | None

class FileSizeRotationHandler(metaclass= SingletonPattern):
    """
    Purpose:
        Manages a singleton file size rotation logging handler.
    Arguments:
        args= The configuration arguments for the handler.
    Returns:
        typing.Self= The singleton instance of FileSizeRotationHandler.
    """
    _lock: threading.Lock = threading.Lock()

    def __init__(self, args: FileSizeRotationHandlerArguments) -> None:
        self.args: FileSizeRotationHandlerArguments = args
        self.handler: logging.handlers.RotatingFileHandler | None = None
    
    def create(self) -> logging.handlers.RotatingFileHandler:
        """
        Purpose:
            Retrieves or creates the file size rotation handler.
        Arguments:
            None= None.
        Returns:
            logging.handlers.RotatingFileHandler= The configured file size rotation handler.
        """
        if self.handler is None:
            with self._lock:
                if self.handler is None:
                    directory_path: pathlib.Path = pathlib.Path(self.args.file_path).parent
                    directory_path.mkdir(parents= True, exist_ok= True)
                    handler: logging.handlers.RotatingFileHandler = \
                        logging.handlers.RotatingFileHandler(
                            filename= str(self.args.file_path),
                            mode= self.args.mode,
                            maxBytes= self.args.max_bytes,
                            backupCount= self.args.backup_count,
                            encoding= self.args.encoding,
                            delay= self.args.delay,
                            errors= self.args.errors
                        )
                    handler.setLevel(level= self.args.level)
                    handler.setFormatter(
                        logging.Formatter(
                            fmt= self.args.message_format,
                            datefmt= self.args.datetime_format
                        )
                    )
                    self.handler = handler
        return self.handler


# --- TimeRotation Handler Manager ---
@dataclasses.dataclass(frozen= True)
class TimeRotationHandlerArguments:
    level: int
    message_format: str
    datetime_format: str
    file_path: pathlib.Path | str
    when: str
    interval: int
    backup_count: int
    encoding: str | None
    delay: bool
    utc: bool
    attime: datetime.time | None
    errors: str | None

class TimeRotationHandler(metaclass= SingletonPattern):
    """
    Purpose:
        Manages a singleton time rotation logging handler.
    Arguments:
        args= The configuration arguments for the handler.
    Returns:
        typing.Self= The singleton instance of TimeRotationHandler.
    """
    _lock: threading.Lock = threading.Lock()

    def __init__(self, args: TimeRotationHandlerArguments) -> None:
        self.args: TimeRotationHandlerArguments = args
        self.handler: logging.handlers.TimedRotatingFileHandler | None = None
    
    def create(self) -> logging.handlers.TimedRotatingFileHandler:
        """
        Purpose:
            Retrieves or creates the time rotation handler.
        Arguments:
            None= None.
        Returns:
            logging.handlers.TimedRotatingFileHandler= The configured time rotation handler.
        """
        if self.handler is None:
            with self._lock:
                if self.handler is None:
                    directory_path: pathlib.Path = pathlib.Path(self.args.file_path).parent
                    directory_path.mkdir(parents= True, exist_ok= True)
                    handler: logging.handlers.TimedRotatingFileHandler = \
                        logging.handlers.TimedRotatingFileHandler(
                            filename= str(self.args.file_path),
                            when= self.args.when,
                            interval= self.args.interval,
                            backupCount= self.args.backup_count,
                            encoding= self.args.encoding,
                            delay= self.args.delay,
                            utc= self.args.utc,
                            atTime= self.args.attime,
                            errors= self.args.errors
                        )
                    handler.setLevel(level= self.args.level)
                    handler.setFormatter(
                        logging.Formatter(
                            fmt= self.args.message_format,
                            datefmt= self.args.datetime_format
                        )
                    )
                    self.handler = handler
        return self.handler