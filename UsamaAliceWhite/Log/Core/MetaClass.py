# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import threading
import typing


# --- SingletonPattern ---
class SingletonPattern(type):
    """
    Purpose:
        Thread-safe Singleton pattern using a metaclass.
    Arguments:
        None= None
    Returns:
        None= None
    """
    _instance: dict[type, typing.Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        if cls not in cls._instance:
            with cls._lock:
                if cls not in cls._instance:
                    instance: typing.Any = super().__call__(*args, **kwargs)
                    cls._instance[cls] = instance
        return cls._instance[cls]