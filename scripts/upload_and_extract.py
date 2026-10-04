#!/usr/bin/env python3
import json
import os
import sys
import time
import ftplib
import ssl
import urllib.request
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"
ZIP_PATH = Path("/tmp/sumowebtools-2.0.3-patched.zip")

PHP_EXTRACTOR = """<?php
ini_set('max_execution_time', 300);
ini_set('memory_limit', '512M');

$zipFile = __DIR__ . '/sumowebtools.zip';

if (!file_exists($zipFile)) {
    die("Error: sumowebtools.zip not found!");
}

$zip = new ZipArchive();
$res = $zip->open($zipFile);
if ($res === TRUE) {
    $zip->extractTo(__DIR__);
    $zip->close();
    echo "EXTRACTION_SUCCESS";
} else {
    echo "ERROR_CODE_" . $res;
}
?>"""

def main():
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)

    print("Connecting to FTP...")
    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg["port"], timeout=30)
    ftp.login(cfg["username"], cfg["password"])
    print("Connected as", cfg["username"])
    print("Remote directory:", ftp.pwd())

    # Step 1: Upload unzip_installer.php
    print("Uploading unzip_installer.php...")
    import io
    ftp.storbinary("STOR unzip_installer.php", io.BytesIO(PHP_EXTRACTOR.encode("utf-8")))
    print("unzip_installer.php uploaded.")

    # Step 2: Upload sumowebtools.zip
    total_size = ZIP_PATH.stat().st_size
    print(f"Uploading {ZIP_PATH.name} ({total_size / (1024*1024):.2f} MB)...")
    
    uploaded_bytes = 0
    start_time = time.time()
    last_print = 0

    def callback(chunk):
        nonlocal uploaded_bytes, last_print
        uploaded_bytes += len(chunk)
        now = time.time()
        if now - last_print >= 2 or uploaded_bytes == total_size:
            pct = (uploaded_bytes / total_size) * 100
            elapsed = now - start_time
            speed = (uploaded_bytes / (1024 * 1024)) / elapsed if elapsed > 0 else 0
            print(f"Uploaded: {uploaded_bytes / (1024*1024):.2f} MB / {total_size / (1024*1024):.2f} MB ({pct:.1f}%) - {speed:.2f} MB/s", flush=True)
            last_print = now

    with open(ZIP_PATH, "rb") as f:
        ftp.storbinary("STOR sumowebtools.zip", f, blocksize=64*1024, callback=callback)

    print("Upload completed successfully!")
    ftp.quit()

    # Step 3: Trigger extraction via HTTP
    print("Triggering extraction via HTTP...")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request("https://linkefly.xyz/unzip_installer.php", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=120) as resp:
        result = resp.read().decode("utf-8").strip()
        print("Extraction Result:", result)

    if "EXTRACTION_SUCCESS" in result:
        print("Cleaning up remote unzip_installer.php and zip...")
        ftp = ftplib.FTP()
        ftp.connect(cfg["host"], cfg["port"], timeout=30)
        ftp.login(cfg["username"], cfg["password"])
        try:
            ftp.delete("unzip_installer.php")
            print("Deleted unzip_installer.php")
        except Exception as e:
            print("Failed to delete unzip_installer.php:", e)
        try:
            ftp.delete("sumowebtools.zip")
            print("Deleted remote sumowebtools.zip")
        except Exception as e:
            print("Failed to delete sumowebtools.zip:", e)
        print("Remote files now:")
        ftp.dir()
        ftp.quit()
        print("ALL DONE SUCCESSFULLY!")
    else:
        print("Extraction failed or returned unexpected output:", result)

if __name__ == "__main__":
    main()
