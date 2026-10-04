#!/usr/bin/env python3
import json
import os
import sys
import ftplib
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"

def load_config():
    if not CONFIG_FILE.exists():
        print(f"Config file not found: {CONFIG_FILE}")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def get_ftp():
    cfg = load_config()
    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg.get("port", 21), timeout=15)
    ftp.login(cfg["username"], cfg["password"])
    if "remote_dir" in cfg and cfg["remote_dir"]:
        try:
            ftp.cwd(cfg["remote_dir"])
        except Exception:
            pass
    return ftp

def list_files(remote_path=""):
    ftp = get_ftp()
    if remote_path:
        ftp.cwd(remote_path)
    print(f"Current Directory: {ftp.pwd()}")
    print("Files & Directories:")
    ftp.dir()
    ftp.quit()

def upload_file(local_path, remote_path=None):
    ftp = get_ftp()
    local_p = Path(local_path)
    if not local_p.is_file():
        print(f"File not found: {local_path}")
        return
    rem_name = remote_path if remote_path else local_p.name
    with open(local_p, "rb") as f:
        ftp.storbinary(f"STOR {rem_name}", f)
    print(f"Uploaded: {local_path} -> {rem_name}")
    ftp.quit()

def download_file(remote_path, local_path=None):
    ftp = get_ftp()
    loc_name = local_path if local_path else Path(remote_path).name
    with open(loc_name, "wb") as f:
        ftp.retrbinary(f"RETR {remote_path}", f.write)
    print(f"Downloaded: {remote_path} -> {loc_name}")
    ftp.quit()

def main():
    if len(sys.argv) < 2:
        print("Usage: ftp_sync.py <list|upload|download> [args...]")
        sys.exit(1)
    cmd = sys.argv[1].lower()
    if cmd == "list":
        path = sys.argv[2] if len(sys.argv) > 2 else ""
        list_files(path)
    elif cmd == "upload":
        if len(sys.argv) < 3:
            print("Usage: ftp_sync.py upload <local_file> [remote_file]")
            sys.exit(1)
        upload_file(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif cmd == "download":
        if len(sys.argv) < 3:
            print("Usage: ftp_sync.py download <remote_file> [local_file]")
            sys.exit(1)
        download_file(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
