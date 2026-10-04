#!/usr/bin/env python3
import json
import ftplib
import ssl
import urllib.request
import uuid
from pathlib import Path
from posts_data import POSTS

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"

def main():
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)

    # 1. Upload posts.json
    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg["port"], timeout=30)
    ftp.login(cfg["username"], cfg["password"])

    posts_bytes = json.dumps(POSTS, ensure_ascii=False, indent=2).encode("utf-8")
    import io
    ftp.storbinary("STOR posts_temp.json", io.BytesIO(posts_bytes))
    print("Uploaded posts_temp.json successfully.")

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
    $jsonFile = __DIR__ . '/posts_temp.json';
    if (!file_exists($jsonFile)) {
        die("ERROR: posts_temp.json not found!");
    }

    $posts = json_decode(file_get_contents($jsonFile), true);
    if (!$posts) {
        die("ERROR: Failed to parse JSON!");
    }

    // 1. Delete dummy posts
    $dummy_slugs = [
        'single-article',
        'what-is-lorem-ipsum',
        'why-do-we-use-it',
        'where-does-it-come-from',
        'where-can-i-get-some',
        'lovely-and-cosy-apartment',
        'the-storms-of-the-waves'
    ];
    $old_pages = DB::table('pages')->whereIn('slug', $dummy_slugs)->pluck('id');
    DB::table('page_translations')->whereIn('page_id', $old_pages)->delete();
    DB::table('pages')->whereIn('id', $old_pages)->delete();
    echo "DELETED " . count($old_pages) . " OLD DUMMY POSTS.\\n";

    $locales = ['en', 'ar', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'tr', 'vi'];
    $now = now();
    $count = 0;

    foreach ($posts as $p) {
        $existing = DB::table('pages')->where('slug', $p['slug'])->first();
        if ($existing) {
            $page_id = $existing->id;
            DB::table('pages')->where('id', $page_id)->update([
                'featured_image' => $p['featured_image'],
                'category_id' => $p['category_id'],
                'popular' => 1,
                'post_status' => 1,
                'page_status' => 1,
                'updated_at' => $now,
            ]);
            DB::table('page_translations')->where('page_id', $page_id)->delete();
        } else {
            $page_id = DB::table('pages')->insertGetId([
                'slug' => $p['slug'],
                'target' => '_self',
                'type' => 'post',
                'featured_image' => $p['featured_image'],
                'tool_name' => null,
                'icon_image' => null,
                'custom_tool_link' => null,
                'post_status' => 1,
                'page_status' => 1,
                'tool_status' => 1,
                'ads_status' => 1,
                'popular' => 1,
                'position' => 1,
                'category_id' => $p['category_id'],
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
        echo "POST #" . $count . " SAVED: " . $p['slug'] . " (ID: " . $page_id . ")\\n";
    }

    unlink($jsonFile);

    try {
        Artisan::call('cache:clear');
        Artisan::call('view:clear');
        echo "CACHES CLEARED.\\n";
    } catch (\\Throwable $t) {
        echo "CACHE CLEAR: " . $t->getMessage() . "\\n";
    }

    echo "ALL DONE SUCCESSFULLY! Total Posts: " . $count . "\\n";

} catch (\\Throwable $e) {
    echo "EXCEPTION: " . $e->getMessage() . "\\n" . $e->getTraceAsString();
}
"""

    ftp.storbinary(f"STOR {php_filename}", io.BytesIO(php_script.encode("utf-8")))
    print(f"Uploaded {php_filename}")

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
            ftp.delete("posts_temp.json")
        except Exception:
            pass
        ftp.quit()

    print("--- OUTPUT ---")
    print(output)

if __name__ == "__main__":
    main()
