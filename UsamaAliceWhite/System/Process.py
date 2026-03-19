# Copyright 2026 UsamaAliceWhite All Rights Reserved


# 標準モジュール
import pathlib
import socket
import subprocess

# サードパーティーライブラリ
import psutil


# --- Localhost(Port)の使用状況を確認 ---
def is_localhost_active(localhost_port: int) -> bool:
    """
    Contents:
        指定のローカルホスト(ポート)の使用状況を確認する。
    Parameters:
        localhost_port = ローカルホストのポート番号
    Returns:
        True = 使用中
        False = 未使用
    """
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as s:
        if s.connect_ex(("localhost", localhost_port)) == 0:
            return True
    return False


# --- Process(Localhost(Port))の起動状況を確認 ---
def is_process_on_localhost_active(
        localhost_port: int,
        process_name: str = "chrome"
    ) -> bool:
    """
    Contents:
        指定したプロセスがローカルホスト(ポート)での起動状況を確認。
    Parameters:
        localhost_port = ローカルホストのポート番号
        process_name = プロセス名(部分一致)
    Returns:
        True = 起動中
        False = 未起動
    """
    for p in psutil.process_iter(attrs= ["name", "cmdline"]):
        try:
            if p.info["name"] and process_name in p.info["name"].lower():
                cmdline: list[str] = p.info["cmdline"] or []
                if any(arg == f"--remote-debugging-port={localhost_port}" for arg in cmdline):
                    return True
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            continue
    return False


# --- Browser(Localhost(Port))を起動 ---
def launch_browser_on_localhost(
        browser_path: pathlib.Path | str,
        profile_path: pathlib.Path | str,
        localhost_port: int,
        add_cmdline: list[str] | None = None
    ) -> subprocess.Popen:
    """
    Contents:
        指定したプロファイルとローカルホスト(ポート)にてブラウザを起動する。
        ※Chromium系ブラウザ(Chrome,Edgeなど)専用の引数を使用。
    Parameters:
        browser_path = ブラウザの実行ファイルパス
        profile_path = プロファイルのディレクトリパス
        localhost_port = ローカルホストのポート番号
        add_cmdline = 追加するコマンドライン引数(default= --user-data-dir,--remote-debugging-port)
    Returns:
        起動したブラウザのインスタンス
    """
    pathlib.Path(profile_path).mkdir(parents= True, exist_ok= True)
    args: list[str] = [
        str(browser_path),
        f"--user-data-dir={profile_path}",
        f"--remote-debugging-port={localhost_port}",
        *(add_cmdline or [])
    ]
    return subprocess.Popen(args= args)