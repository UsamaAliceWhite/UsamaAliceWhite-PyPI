# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import logging
import pathlib


# --- Constant ---
class Constant:
    class Byte:
        KB100: int = 100 * 1024
        KB500: int = 500 * 1024
        MB001: int = 1 * 1024 * 1024
        MB005: int = 5 * 1024 * 1024
        MB010: int = 10 * 1024 * 1024
        MB050: int = 50 * 1024 * 1024
        MB100: int = 100 * 1024 * 1024
        MB500: int = 500 * 1024 * 1024
        GB001: int = 1 * 1024 * 1024 * 1024
    class Encode:
        UTF8: str = "utf-8"
        UTF16: str = "utf-16"
        ShiftJis: str = "shift_jis"
    class Log:
        class Datetime:
            Default: str = "%Y-%m-%d %H:%M:%S"
        class FilePath:
            UserHome: pathlib.Path = pathlib.Path.home() / "UsamaAliceWhite.log"
        class FileSizeRotation:
            class Mode:
                Append: str = "a"
                Write: str = "w"
        class Format:
            Default: str = "%(asctime)s [%(levelname)-8s] %(name)-20s:%(funcName)-20s:%(lineno)-4d - %(message)s"
        class Level:
            Debug: int = logging.DEBUG
            Info: int = logging.INFO
            Warning: int = logging.WARNING
            Error: int = logging.ERROR
            Critical: int = logging.CRITICAL
        class TimeRotation:
            class When:
                Second: str = "S"
                Minute: str = "M"
                Hour: str = "H"
                Day: str = "D"
                Midnight: str = "midnight"
                WeekMonday: str = "W0"
                WeekTuesday: str = "W1"
                WeekWednesday: str = "W2"
                WeekThursday: str = "W3"
                WeekFriday: str = "W4"
                WeekSaturday: str = "W5"
                WeekSunday: str = "W6"