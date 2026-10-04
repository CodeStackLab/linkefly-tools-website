#!/usr/bin/env python3
import json
import ftplib
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"
IMG_DIR = Path(__file__).parent / "blog_images"

def main():
    with open(CONFIG_FILE, "r") as f:
        cfg = json.load(f)

    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg.get("port", 21), timeout=20)
    ftp.login(cfg["username"], cfg["password"])

    remote_dir = "assets/img/blog"
    # Ensure remote directory exists
    try:
        ftp.cwd(remote_dir)
    except Exception:
        ftp.mkd(remote_dir)
        ftp.cwd(remote_dir)

    print(f"Connected to FTP, uploading to {remote_dir}...")

    # Upload all post11 to post30 images
    uploaded = 0
    for num in range(11, 31):
        pattern = f"post{num}-*"
        files = list(IMG_DIR.glob(pattern))
        for f in files:
            print(f"Uploading {f.name} ({f.stat().st_size:,} bytes)...")
            with open(f, "rb") as fp:
                ftp.storbinary(f"STOR {f.name}", fp)
            uploaded += 1

    ftp.quit()
    print(f"\nSUCCESS: Uploaded {uploaded} images to assets/img/blog/")

if __name__ == "__main__":
    main()
