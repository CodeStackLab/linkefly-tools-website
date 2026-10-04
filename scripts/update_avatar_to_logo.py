#!/usr/bin/env python3
import json
import ftplib
from pathlib import Path
from run_remote_php import run_php

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"

def main():
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)

    # 1. Upload new brand logo avatar
    print("Connecting to FTP...")
    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg["port"], timeout=30)
    ftp.login(cfg["username"], cfg["password"])
    ftp.cwd("assets/img")

    print("Uploading avatar.png...")
    with open("linkefly_avatar.png", "rb") as f:
        ftp.storbinary("STOR avatar.png", f)

    print("Uploading avatar.jpg...")
    with open("linkefly_avatar.jpg", "rb") as f:
        ftp.storbinary("STOR avatar.jpg", f)

    ftp.quit()
    print("Uploaded avatar.png and avatar.jpg successfully.")

    # 2. Update Database with cache-busting URL
    php_code = """
    DB::table('users')->where('id', 1)->update([
        'avatar' => 'https://linkefly.xyz/assets/img/avatar.png?v=2',
        'updated_at' => now(),
    ]);

    Artisan::call('cache:clear');
    Artisan::call('view:clear');
    echo "USER AVATAR UPDATED TO BRAND LOGO AND CACHES CLEARED.\\n";
    """

    res = run_php(php_code)
    print("--- RESULT ---")
    print(res)

if __name__ == "__main__":
    main()
