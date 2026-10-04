#!/usr/bin/env python3
import json
import ftplib
import time
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"
OUTPUT_FILE = Path(__file__).parent / "linkefly_complete_backup_with_db.zip"

def main():
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)

    ftp = ftplib.FTP()
    print(f"Connecting to FTP {cfg['host']}...")
    ftp.connect(cfg["host"], cfg["port"], timeout=60)
    ftp.login(cfg["username"], cfg["password"])
    ftp.voidcmd('TYPE I')

    remote_file = "linkefly_full_backup.zip"
    try:
        total_size = ftp.size(remote_file)
        print(f"Remote file size: {total_size:,} bytes (~{total_size / (1024*1024):.1f} MB)")
    except Exception:
        total_size = 120089693
        print(f"Remote file size: ~{total_size / (1024*1024):.1f} MB")

    downloaded = 0
    start_time = time.time()
    last_print = 0

    with open(OUTPUT_FILE, "wb") as f:
        def callback(chunk):
            nonlocal downloaded, last_print
            f.write(chunk)
            downloaded += len(chunk)
            now = time.time()
            if now - last_print >= 2 or downloaded == total_size:
                elapsed = now - start_time
                speed = (downloaded / 1024 / 1024) / elapsed if elapsed > 0 else 0
                pct = (downloaded / total_size) * 100 if total_size else 0
                print(f"Progress: {downloaded:,} / {total_size:,} bytes ({pct:.1f}%) | {speed:.2f} MB/s")
                last_print = now

        ftp.retrbinary(f"RETR {remote_file}", callback, blocksize=65536)

    ftp.quit()
    elapsed = time.time() - start_time
    print(f"\nSUCCESS: Downloaded to {OUTPUT_FILE} in {elapsed:.1f}s!")

if __name__ == "__main__":
    main()
