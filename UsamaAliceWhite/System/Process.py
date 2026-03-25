# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Libraries
import pathlib
import socket
import subprocess


# --- Checks the usage status of the remote debugging port ---
def is_remote_debug_port_active(port: int, timeout: float = 3.0) -> bool:
    """
    Contents:
        Checks the usage status of the remote debugging port.
    Parameters:
        port = Remote debugging port number.
        timeout = Connection timeout in seconds.
    Returns:
        True = Port is in use.
        False = Port is available.
    """
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex(("127.0.0.1", port)) == 0


# --- Launches the browser with a specified remote debugging port ---
def launch_browser_with_remote_debug(
        browser_path: pathlib.Path | str,
        profile_path: pathlib.Path | str,
        debug_port: int,
        add_cmdline_args: list[str] | None = None
    ) -> subprocess.Popen:
    """
    Contents:
        Launches the browser with a specified remote debugging port.
        (Uses Chromium based browser arguments (Chrome, Edge, etc.).)
    Parameters:
        browser_path = Path to the browser executable.
        profile_path = Path to the profile directory.
        debug_port = Remote debugging port number.
        add_cmdline_args = Additional command line arguments.
        ('--user-data-dir' and '--remote-debugging-port' are automatically added.)
    Returns:
        subprocess.Popen = The launched browser process instance.
    """
    browser_path: pathlib.Path = pathlib.Path(browser_path)
    profile_path: pathlib.Path = pathlib.Path(profile_path)
    if not browser_path.exists():
        raise FileNotFoundError(f"Browser not found: {browser_path}")
    profile_path.mkdir(parents= True, exist_ok= True)
    args: list[str] = [
        str(browser_path),
        f"--user-data-dir={str(profile_path)}",
        f"--remote-debugging-port={str(debug_port)}",
        *(add_cmdline_args or [])
    ]
    return subprocess.Popen(args= args)