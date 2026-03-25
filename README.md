Copyright 2026 UsamaAliceWhite All Rights Reserved


## Overview
1. **Purpose**
    - Python用ユーティリティライブラリ
1. **Language**
    - Python
1. **Third Party Library**
    - None
1. **Platform**
    - Windows
    - Linux
    - Mac


## Function
### Core
1. **SingletonPattern**
    1. Purpose
        - スレッドセーフなシングルトンパターンのメタクラス
    1. SampleCode
        ```
        from UsamaAliceWhite.Core import SingletonPattern

        class SeaOtter(metaclass= SingletonPattern):
            def __init__(self) -> None:
                pass
        
        a = SeaOtter()
        b = SeaOtter()
        assert a is b
        ```
### System
1. **is_remote_debug_port_active**
    1. Purpose
        - リモートデバッグポートの使用状況を確認
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
        - Chromium系ブラウザをリモートデバッグモードで起動
    1. SampleCode
        ```
        from UsamaAliceWhite.System import launch_browser_with_remote_debug
        from subprocess import Popen

        process: Popen = launch_browser_with_remote_debug(
            browser_path= "C:/Program Files/Google/Chrome/Application/chrome.exe",
            profile_path= "C:/UsamaAliceWhite/Profile/",
            debug_port= 5368,
            add_cmdline_args= ["--no-first-run", "--start-maximized"]
        )
        ```

## DirectoryStructure
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
└── README.md
```