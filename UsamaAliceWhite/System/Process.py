# Copyright 2026 UsamaAliceWhite All Rights Reserved


# Standard Library
import pathlib
import socket
import subprocess


# --- RemoteDebugPortMonitor ---
def is_remote_debug_port_active(
    port: int,
    host: str = "127.0.0.1",
    timeout: float = 1.0
) -> bool:
    """
    Purpose:
        Check the usage status of the remote debugging port.
    Arguments:
        port= Remote debugging port number
        host= Target host address
        timeout= Connection timeout in seconds
    Returns:
        True= Port is in use
        False= Port is available
    """
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


# --- LaunchBrowserWithRemoteDebugPort ---
def launch_browser_with_remote_debug(
    browser_path: pathlib.Path | str,
    profile_path: pathlib.Path | str,
    debug_port: int,
    cmdline_args: list[str] | None = None
) -> subprocess.Popen:
    """
    Purpose:
        Launch the browser with a specified remote debugging port.
        Supports Chrome, Edge, and other Chromium browsers.
    Arguments:
        browser_path= Path to the browser executable
        profile_path= Path to the profile directory
        debug_port= Remote debugging port number
        cmdline_args= Additional command-line arguments
            (--user-data-dir and --remote-debugging-port are added automatically)
    Returns:
        subprocess.Popen= The launched browser process instance
    """
    browser_path: pathlib.Path = pathlib.Path(browser_path)
    profile_path: pathlib.Path = pathlib.Path(profile_path)
    profile_path.mkdir(parents= True, exist_ok= True)
    args: list[str] = [
        str(browser_path),
        f"--user-data-dir={str(profile_path)}",
        f"--remote-debugging-port={str(debug_port)}",
        *(cmdline_args or [])
    ]
    return subprocess.Popen(args= args)