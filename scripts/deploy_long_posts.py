#!/usr/bin/env python3
import json
import ftplib
import io
import ssl
import urllib.request
import uuid
from pathlib import Path
from long_posts_part1 import POSTS_PART_1
from long_posts_part2 import POSTS_PART_2

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"

def main():
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)

    all_posts = POSTS_PART_1 + POSTS_PART_2
    print(f"Total posts to deploy: {len(all_posts)}")

    # 1. Upload long_posts_temp.json
    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg["port"], timeout=30)
    ftp.login(cfg["username"], cfg["password"])

    posts_bytes = json.dumps(all_posts, ensure_ascii=False, indent=2).encode("utf-8")
    ftp.storbinary("STOR long_posts_temp.json", io.BytesIO(posts_bytes))
    print("Uploaded long_posts_temp.json successfully.")

    # 2. Upload runner PHP
    token = uuid.uuid4().hex
    php_filename = f"runner_{token}.php"

    php_script = """<?php
require_once __DIR__ . '/components/vendor/autoload.php';
$app = require_once __DIR__ . '/components/bootstrap/app.php';
$kernel = $app->make(Illuminate\\Contracts\\Http\\Kernel::class);
$response = $kernel->handle($request = Illuminate\\Http\\Request::capture());

header('Content-Type: text/plain; charset=utf-8');

try {
    $jsonFile = __DIR__ . '/long_posts_temp.json';
    if (!file_exists($jsonFile)) {
        die("ERROR: long_posts_temp.json not found!");
    }

    $posts = json_decode(file_get_contents($jsonFile), true);
    $locales = ['en', 'ar', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'tr', 'vi'];
    $now = now();
    $count = 0;

    foreach ($posts as $p) {
        $existing = DB::table('pages')->where('slug', $p['slug'])->first();
        if ($existing) {
            $page_id = $existing->id;
            // Ensure category_id is null and tool_status is 0 so posts never appear in tool grid
            DB::table('pages')->where('id', $page_id)->update([
                'type' => 'post',
                'category_id' => null,
                'tool_status' => 0,
                'post_status' => 1,
                'popular' => 1,
                'updated_at' => $now,
            ]);
            DB::table('page_translations')->where('page_id', $page_id)->delete();
        } else {
            $page_id = DB::table('pages')->insertGetId([
                'slug' => $p['slug'],
                'target' => '_self',
                'type' => 'post',
                'featured_image' => 'https://linkefly.xyz/assets/img/blog/post' . $p['id_num'] . '-featured.jpg',
                'tool_name' => null,
                'icon_image' => null,
                'custom_tool_link' => null,
                'post_status' => 1,
                'page_status' => 1,
                'tool_status' => 0,
                'ads_status' => 1,
                'popular' => 1,
                'position' => 1,
                'category_id' => null,
                'created_at' => $now,
                'updated_at' => $now,
            ]);
        }

        foreach ($locales as $loc) {
            DB::table('page_translations')->insert([
                'locale' => $loc,
                'page_title' => $p['title'],
                'robots_meta' => 1,
                'sitename_status' => 1,
                'title' => $p['title'],
                'subtitle' => $p['subtitle'],
                'short_description' => $p['short_description'],
                'description' => $p['description'],
                'page_id' => $page_id,
                'created_at' => $now,
                'updated_at' => $now,
            ]);
        }
        $count++;
        echo "UPDATED LONG-FORM POST #" . $count . ": " . $p['slug'] . " (Length: " . strlen($p['description']) . " chars)\\n";
    }

    unlink($jsonFile);

    try {
        Artisan::call('cache:clear');
        Artisan::call('view:clear');
        echo "CACHES CLEARED.\\n";
    } catch (\\Throwable $t) {
        echo "CACHE CLEAR: " . $t->getMessage() . "\\n";
    }

    echo "ALL 10 LONG-FORM PILLAR POSTS DEPLOYED SUCCESSFULLY!\\n";

} catch (\\Throwable $e) {
    echo "EXCEPTION: " . $e->getMessage() . "\\n" . $e->getTraceAsString();
}
"""

    ftp.storbinary(f"STOR {php_filename}", io.BytesIO(php_script.encode("utf-8")))
    print(f"Uploaded {php_filename}.")

    # 3. Call via HTTP
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(f"https://linkefly.xyz/{php_filename}", headers={"User-Agent": "Mozilla/5.0"})
    output = ""
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            output = resp.read().decode("utf-8")
    except Exception as e:
        output = f"HTTP Error: {e}"
    finally:
        try:
            ftp.delete(php_filename)
        except Exception:
            pass
        try:
            ftp.delete("long_posts_temp.json")
        except Exception:
            pass
        ftp.quit()

    print("--- OUTPUT ---")
    print(output)

if __name__ == "__main__":
    main()
