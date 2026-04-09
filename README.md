## Information
### Overview
1. **Purpose**
    - Python utility library
1. **Author**
    - UsamaAliceWhite
1. **Copyright**
    - Copyright 2026 UsamaAliceWhite All Rights Reserved
### Environment
1. **Language**
    - Python
1. **Standard Library**
    - pathlib
    - socket
    - subprocess
    - threading
    - typing
1. **Third-Party Library**
    - None
1. **Support OS**
    - Window
    - Linux
    - Mac
## Specification
### Core
1. **SingletonPattern**
    1. Purpose
        - Thread-safe Singleton pattern using a metaclass.
    1. Arguments
        - None= None
    1. Returns
        - None= None
    1. SampleCode
        ```
        from UsamaAliceWhite.Core import SingletonPattern

        class SeaOtter(metaclass= SingletonPattern):
            def __init__(self) -> None:
                pass

        one: SeaOtter = SeaOtter()
        two: SeaOtter = SeaOtter()

        assert one is two
        ```
### System
1. **is_remote_debug_port_active**
    1. Purpose
        - Check the usage status of the remote debugging port.
    1. Arguments
        - port= Remote debugging port number
        - host= Target host address
        - timeout= Connection timeout in seconds
    1. Returns
        - True= Port is in use
        - False= Port is available
    1. SampleCode
        ```
        from UsamaAliceWhite.System import is_remote_debug_port_active

        if is_remote_debug_port_active(port= 5368):
            print("Port is in use.")
        else:
            print("Port is available.")
        ```
1. **launch_browser_with_remote_debug**
    1. Purpose
        - Launch the browser with a specified remote debugging port.  
          Supports Chrome, Edge, and other Chromium browsers.
    1. Arguments
        - browser_path= Path to the browser executable
        - profile_path= Path to the profile directory
        - debug_port= Remote debugging port number
        - cmdline_args= Additional command-line arguments  
          (--user-data-dir and --remote-debugging-port are added automatically)
    1. Returns
        - subprocess.Popen= The launched browser process instance
    1. SampleCode
        ```
        from UsamaAliceWhite.System import launch_browser_with_remote_debug
        from subprocess import Popen

        process: Popen = launch_browser_with_remote_debug(
            browser_path= "C:/Program Files/Google/Chrome/Application/chrome.exe",
            profile_path= "C:/UsamaAliceWhite/Profile/",
            debug_port= 5368,
            cmdline_args= ["--no-first-run", "--start-maximized"]
        )
        ```
## Structure
```
UsamaAliceWhite-PyPI/
├── UsamaAliceWhite/
│   ├── Core/
│   │   ├── __init__.py
│   │   └── MetaClass.py
│   ├── System/
│   │   ├── __init__.py
│   │   └── Process.py
│   ├── __init__.py
│   └── py.typed
├── LICENSE
├── pyproject.toml
└── README.md
```