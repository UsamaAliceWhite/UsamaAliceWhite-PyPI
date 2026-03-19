# Copyright 2026 UsamaAliceWhite All Rights Reserved


# サードパーティーライブラリ
import screeninfo


# --- モニターの幾何学情報を取得 ---
def get_monitor_geometry(monitor_number: int) -> tuple[int, int, int, int]:
    """
    Contents:
        モニターの幾何学情報を取得する。
    Parameters:
        monitor_number = モニターの幾何学情報(1以上)
    Returns:
        モニターの幾何学情報(x, y, width, height)
    """
    if monitor_number < 1:
        raise ValueError("Invalid monitor number.")
    try:
        monitors: list[screeninfo.Monitor] = screeninfo.get_monitors()
        monitor: screeninfo.Monitor = monitors[monitor_number - 1]
    except IndexError as e:
        raise IndexError("Target monitor not found.") from e
    except Exception as e:
        raise RuntimeError("Failed to retrieve monitor information.") from e
    return monitor.x, monitor.y, monitor.width, monitor.height