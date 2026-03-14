# Copyright 2026 UsamaAliceWhite All Rights Reserved


# 標準モジュール
import pathlib
import socket
import subprocess

# サードパーティーライブラリ
import psutil


# --- ローカルホストのプロセスを確認 ---
def localhost_process_check(
        localhost_port: int,
        process_name: str = "chrome"
    ) -> bool:
    """
    Content:
        指定したプロセス名とポートの起動状況を確認する。
        起動しているプロセス名とポートが一致した場合にのみTrueを返す。
    Parameter:
        localhost_port = ローカルホストのポート番号
        process_name = 確認するプロセス名
    Return:
        bool = 同ポート番号の指定プロセスの起動状況(True=起動中,False=未起動)
    """
    for process in psutil.process_iter(attrs= ["name", "cmdline"]):
        try:
            if process.info["name"] and process_name in process.info["name"].lower():
                cmdline: list[str] = process.info["cmdline"] or []
                if any(arg == f"--remote-debugging-port={localhost_port}" for arg in cmdline):
                    return True
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            continue
    return False


# --- ローカルホストの使用状況を確認 ---
def localhost_active_check(
        localhost_port: int
    ) -> bool:
    """
    Content:
        指定したポートの使用状況を確認する。
    Parameter:
        localhost_port = ローカルホストのポート番号
    Return:
        bool = 同ポート番号の使用状況(True=使用中,False=未使用)
    """
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as connect:
        if connect.connect_ex(("localhost", localhost_port)) == 0:
            return True
    return False


# --- ローカルホストを指定してブラウザを起動 ---
def browser_execution(
        exe_path: pathlib.Path | str,
        profile_path: pathlib.Path | str,
        localhost_port: int,
        add_cmdline: list[str] | None = None
    ) -> None:
    """
    Content:
        指定したプロファイルとポートを使用してブラウザを起動する。
        ※Chromium系ブラウザ(Chrome,Edge等)専用の引数を使用します。
        ※初期コマンドライン(--user-data-dir,--remote-debugging-port)
    Parameter:
        exe_path = ブラウザの実行パス
        profile_path = プロファイルのディレクトリパス
        localhost_port = ローカルホストのポート番号
        add_cmdline = 追加するコマンドライン引数
    """
    pathlib.Path(profile_path).mkdir(parents= True, exist_ok= True)
    cmdline_arg: list[str] = [
        str(exe_path),
        f"--user-data-dir={profile_path}",
        f"--remote-debugging-port={localhost_port}"
    ]
    if add_cmdline:
        cmdline_arg.extend(add_cmdline)
    subprocess.Popen(args= cmdline_arg)