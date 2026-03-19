Copyright 2026 UsamaAliceWhite All Rights Reserved


## Functions
### Core
MetaClassやDecoratorなどの基底システムに関するライブラリ。
1. SingletonPattern
    * シングルトンパターン。メタクラスとして使用。
    ```
    from UsamaAliceWhite.Core import SingletonPattern
    class DatabaseManager(metaclass= SingletonPattern):
        def __init__(self) -> None:
            pass
    db1 = DatabaseManager()
    db2 = DatabaseManager()
    assert db1 is db2
    ```


### Device
モニターやマウスなどハードウェアに関するライブラリ。
1. get_monitor_geometry() -> tuple[int, int, int, int]
    * モニターの幾何学情報(x,y,width,height)を取得する。


### System
システムに関するライブラリ。
1. is_localhost_active() -> bool
    * 指定のローカルホスト(port)の使用状況を確認する。
1. is_process_on_localhost_active() -> bool
    * 指定したプロセスがローカルホスト(ポート)での起動状況を確認。
1. launch_browser_on_localhost() -> subprocess.Popen
    * 指定したプロファイルとローカルホスト(port)にてブラウザを起動する。


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
├── pyproject.toml
└── README.md
```