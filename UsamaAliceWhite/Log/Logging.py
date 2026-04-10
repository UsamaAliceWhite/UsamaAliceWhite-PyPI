# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import datetime
import logging
import pathlib

# Local Module
from .Logic import Handler, HandlerArgs, GetLogger


# --- Declaration ---
class Declaration:
    """
    Purpose:
        Declares the logging handler settings for the entire application.
    Arguments:
        handler_mode= The type of handler to create
        (Console, FileSizeRotation, FileTimeRotation)
        log_level= Logging severity level
        (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_message_format= The format string for the log message content
        log_datetime_format= The format string for the timestamp in log messages
        file_path= The file system path where log messages will be written
        file_backup_count= The maximum number of old log files to retain
        file_encoding= The text encoding used to open the log file
        file_delay= Postpones file opening until the first log message is emitted
        file_errors= Specifies how encoding errors are handled
        file_size_mode= The file open mode used when initializing the log file
        file_size_max_bytes= The maximum size of the log file in bytes before it rotates
        file_time_when= Specifies the type of time interval for rotation
        (S, M, H, D, W0-W6, midnight)
        file_time_interval= The amount of time between rotations
        file_time_utc= Determines whether to use Universal Coordinated Time
        file_time_attime= The specific time of day when rotation occurs
    Returns:
        None= None
    """
    def __new__(
        cls,
        handler_mode: str = "Console",
        log_level: int = logging.DEBUG,
        log_message_format: str = "%(asctime)s [%(levelname)-8s] %(name)-20s:%(funcName)-20s:%(lineno)-4d - %(message)s",
        log_datetime_format: str = "%Y-%m-%d %H:%M:%S",
        *,
        file_path: pathlib.Path | str = pathlib.Path.home() / "UsamaAliceWhite.log",
        file_backup_count: int = 10,
        file_encoding: str | None = "utf-8",
        file_delay: bool = False,
        file_errors: str | None = None,
        file_size_mode: str = "a",
        file_size_max_bytes: int = 10 * 1024 * 1024,
        file_time_when: str = "midnight",
        file_time_interval: int = 1,
        file_time_utc: bool = False,
        file_time_attime: datetime.time | None = None
    ) -> None:
        args: HandlerArgs = HandlerArgs(
            level= log_level,
            message_format= log_message_format,
            datetime_format= log_datetime_format,
            file_path= file_path,
            backup_count= file_backup_count,
            encoding= file_encoding,
            delay= file_delay,
            errors= file_errors,
            mode= file_size_mode,
            max_bytes= file_size_max_bytes,
            when= file_time_when,
            interval= file_time_interval,
            utc= file_time_utc,
            attime= file_time_attime
        )
        instance: Handler = Handler(args= args)
        if handler_mode == "Console":
            instance.create_console_handler()
        elif handler_mode == "FileSizeRotation":
            instance.create_size_rotation_handler()
        elif handler_mode == "FileTimeRotation":
            instance.create_time_rotation_handler()
        else:
            raise RuntimeError(f"Invalid handler_mode: {handler_mode}")
        return None


# --- Emitter ---
class Emitter:
    @staticmethod
    def debug(message: str, name: str = "Anonymous") -> None:
        """
        Purpose:
            Emit a DEBUG level message for diagnostic.
        Arguments:
            message= The log message content
            name= The logger name to identify the source
        Returns:
            None= None
        """
        log_output(name= name, level= logging.DEBUG, message= message)

    @staticmethod
    def info(message: str, name: str = "Anonymous") -> None:
        """
        Purpose:
            Emit an INFO level message for confirmation.
        Arguments:
            message= The log message content
            name= The logger name to identify the source
        Returns:
            None= None
        """
        log_output(name= name, level= logging.INFO, message= message)

    @staticmethod
    def warning(message: str, name: str = "Anonymous") -> None:
        """
        Purpose:
            Emit a WARNING level message for unexpected events.
        Arguments:
            message= The log message content
            name= The logger name to identify the source
        Returns:
            None= None
        """
        log_output(name= name, level= logging.WARNING, message= message)

    @staticmethod
    def error(message: str, name: str = "Anonymous") -> None:
        """
        Purpose:
            Emit an ERROR level message for serious problems.
        Arguments:
            message= The log message content
            name= The logger name to identify the source
        Returns:
            None= None
        """
        log_output(name= name, level= logging.ERROR, message= message)

    @staticmethod
    def critical(message: str, name: str = "Anonymous") -> None:
        """
        Purpose:
            Emit a CRITICAL level message for fatal errors.
        Arguments:
            message= The log message content
            name= The logger name to identify the source
        Returns:
            None= None
        """
        log_output(name= name, level= logging.CRITICAL, message= message)

def log_output(name: str, level: int, message: str) -> None:
    instance: Handler = Handler()
    handler: logging.Handler = instance.handler or instance.create_console_handler()
    logger: logging.Logger = GetLogger(handler= handler, name= name, level= logging.DEBUG)
    if level == logging.DEBUG:
        logger.debug(msg= message, stacklevel= 3)
    elif level == logging.INFO:
        logger.info(msg= message, stacklevel= 3)
    elif level == logging.WARNING:
        logger.warning(msg= message, stacklevel= 3)
    elif level == logging.ERROR:
        logger.error(msg= message, stacklevel= 3)
    elif level == logging.CRITICAL:
        logger.critical(msg= message, stacklevel= 3)