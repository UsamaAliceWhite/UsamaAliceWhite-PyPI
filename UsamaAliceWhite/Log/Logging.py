# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import datetime
import inspect
import logging
import pathlib
import typing

# Local Module
from ._Handler import ConsoleHandler, ConsoleHandlerArguments
from ._Handler import FileSizeRotationHandler, FileSizeRotationHandlerArguments
from ._Handler import TimeRotationHandler, TimeRotationHandlerArguments
from ._Logger import GetLogger
from .Core import Constant, SingletonPattern



# --- Declaration ---
class Declaration:
    @staticmethod
    def console(
        *,
        log_level: int = Constant.Log.Level.Debug,
        log_format: str = Constant.Log.Format.Default,
        log_datetime: str = Constant.Log.Datetime.Default
    ) -> None:
        ConsoleHandler(
            args= ConsoleHandlerArguments(
                level= log_level,
                message_format= log_format,
                datetime_format= log_datetime
            )
        ).create()
    
    @staticmethod
    def file_size_rotation(
        *,
        log_level: int = Constant.Log.Level.Debug,
        log_format: str = Constant.Log.Format.Default,
        log_datetime: str = Constant.Log.Datetime.Default,
        file_mode: str = Constant.Log.FileSizeRotation.Mode.Append,
        file_max_bytes: int = Constant.Byte.MB010,
        file_path: pathlib.Path | str = Constant.Log.FilePath.UserHome,
        file_backup_count: int = 10,
        file_encoding: str | None = Constant.Encode.UTF8,
        file_delay: bool = False,
        file_errors: str | None = None
    ) -> None:
        FileSizeRotationHandler(
            args= FileSizeRotationHandlerArguments(
                level= log_level,
                message_format= log_format,
                datetime_format= log_datetime,
                mode= file_mode,
                max_bytes= file_max_bytes,
                file_path= file_path,
                backup_count= file_backup_count,
                encoding= file_encoding,
                delay= file_delay,
                errors= file_errors
            )
        ).create()
    
    @staticmethod
    def time_rotation(
        *,
        log_level: int = Constant.Log.Level.Debug,
        log_format: str = Constant.Log.Format.Default,
        log_datetime: str = Constant.Log.Datetime.Default,
        file_path: pathlib.Path | str = Constant.Log.FilePath.UserHome,
        file_when: str = Constant.Log.TimeRotation.When.Midnight,
        file_interval: int = 1,
        file_backup_count: int = 10,
        file_encoding: str = Constant.Encode.UTF8,
        file_delay: bool = False,
        file_utc: bool = False,
        file_attime: datetime.time | None = None,
        file_errors: str | None = None
    ) -> None:
        TimeRotationHandler(
            args= TimeRotationHandlerArguments(
                level= log_level,
                message_format= log_format,
                datetime_format= log_datetime,
                file_path= file_path,
                when= file_when,
                interval= file_interval,
                backup_count= file_backup_count,
                encoding= file_encoding,
                delay= file_delay,
                utc= file_utc,
                attime= file_attime,
                errors= file_errors
            )
        ).create()


# --- Emitter ---
class Emitter:
    @staticmethod
    def debug(message: str, name: str | None = None) -> None:
        name = name or inspect.currentframe().f_back.f_globals.get("__name__", "Anonymous")
        _emitter_log(message= message, name= name, level= Constant.Log.Level.Debug)

    @staticmethod
    def info(message: str, name: str | None = None) -> None:
        name = name or inspect.currentframe().f_back.f_globals.get("__name__", "Anonymous")
        _emitter_log(message= message, name= name, level= Constant.Log.Level.Info)

    @staticmethod
    def warning(message: str, name: str | None = None) -> None:
        name = name or inspect.currentframe().f_back.f_globals.get("__name__", "Anonymous")
        _emitter_log(message= message, name= name, level= Constant.Log.Level.Warning)

    @staticmethod
    def error(message: str, name: str | None = None) -> None:
        name = name or inspect.currentframe().f_back.f_globals.get("__name__", "Anonymous")
        _emitter_log(message= message, name= name, level= Constant.Log.Level.Error)

    @staticmethod
    def critical(message: str, name: str | None = None) -> None:
        name = name or inspect.currentframe().f_back.f_globals.get("__name__", "Anonymous")
        _emitter_log(message= message, name= name, level= Constant.Log.Level.Critical)

def _emitter_log(message: str, name: str, level: int) -> None:
    instances: dict[type, typing.Any] = SingletonPattern._instances
    if not instances:
        Declaration.console()
        instances = SingletonPattern._instances
    for instance in instances.values():
        if instance.handler:
            logger: logging.Logger = GetLogger(handler= instance.handler, name= name)
    logger.log(level= level, msg= message, stacklevel= 4)