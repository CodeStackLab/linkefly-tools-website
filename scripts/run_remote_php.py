#!/usr/bin/env python3
import json
import ftplib
import ssl
import urllib.request
import uuid
import sys
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"

def run_php(code: str):
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)

    token = uuid.uuid4().hex
    filename = f"runner_{token}.php"

    full_code = f"""<?php
require_once __DIR__ . '/components/vendor/autoload.php';
$app = require_once __DIR__ . '/components/bootstrap/app.php';
$kernel = $app->make(Illuminate\\Contracts\\Http\\Kernel::class);
$response = $kernel->handle(
    $request = Illuminate\\Http\\Request::capture()
);

header('Content-Type: text/plain; charset=utf-8');
try {{
{code}
}} catch (\\Throwable $e) {{
    echo "ERROR: " . $e->getMessage() . "\\n" . $e->getTraceAsString();
}}
"""

    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg["port"], timeout=30)
    ftp.login(cfg["username"], cfg["password"])

    import io
    ftp.storbinary(f"STOR {filename}", io.BytesIO(full_code.encode("utf-8")))

    # Request via HTTP
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(f"https://linkefly.xyz/{filename}", headers={"User-Agent": "Mozilla/5.0"})
    output = ""
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            output = resp.read().decode("utf-8")
    except Exception as e:
        output = f"HTTP Request Error: {e}"
    finally:
        try:
            ftp.delete(filename)
        except Exception:
            pass
        ftp.quit()

    return output

if __name__ == "__main__":
    test_code = """
    echo "DB Connection test: ";
    $res = DB::select('SELECT 1 as val');
    echo "OK: " . $res[0]->val;
    """
    print(run_php(test_code))
