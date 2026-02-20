# Copyright 2026 UsamaAliceWhite All Rights Reserved


# サードパーティーライブラリ
import screeninfo


# --- モニターの幾何学情報を取得 ---
def get_monitor_geometry(monitor_number: int) -> tuple[int, int, int, int]:
    """
    Parameter:
        monitor_number = モニターの識別番号（1以上）
    Return:
        tuple = モニターの幾何学情報（x, y, width, height）
    """
    try:
        monitors: list[screeninfo.Monitor] = screeninfo.get_monitors()
        if monitor_number < 1 or len(monitors) < monitor_number:
            raise RuntimeError("Monitor not found.")
        monitor: screeninfo.Monitor = monitors[monitor_number - 1]
    except Exception as e:
        raise RuntimeError("Failed to retrieve monitor information.") from e
    
    return monitor.x, monitor.y, monitor.width, monitor.height