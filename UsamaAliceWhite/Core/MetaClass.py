# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Libraries
import threading
import typing


# --- Singleton Pattern ---
class SingletonPattern(type):
    _instances: dict[type, typing.Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance: typing.Any = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]