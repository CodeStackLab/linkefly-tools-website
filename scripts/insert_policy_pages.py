#!/usr/bin/env python3
import json
import ftplib
import io
import ssl
import urllib.request
import uuid
from pathlib import Path
from policy_pages_data import PAGES

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"

def main():
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)

    # 1. Upload policy pages JSON
    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg["port"], timeout=30)
    ftp.login(cfg["username"], cfg["password"])

    pages_bytes = json.dumps(PAGES, ensure_ascii=False, indent=2).encode("utf-8")
    ftp.storbinary("STOR policy_pages_temp.json", io.BytesIO(pages_bytes))
    print("Uploaded policy_pages_temp.json.")

    # 2. Upload runner PHP script
    token = uuid.uuid4().hex
    php_filename = f"runner_{token}.php"

    php_script = """<?php
require_once __DIR__ . '/components/vendor/autoload.php';
$app = require_once __DIR__ . '/components/bootstrap/app.php';
$kernel = $app->make(Illuminate\\Contracts\\Http\\Kernel::class);
$response = $kernel->handle($request = Illuminate\\Http\\Request::capture());

header('Content-Type: text/plain; charset=utf-8');

try {
    $jsonFile = __DIR__ . '/policy_pages_temp.json';
    if (!file_exists($jsonFile)) {
        die("ERROR: policy_pages_temp.json not found!");
    }

    $pages = json_decode(file_get_contents($jsonFile), true);
    $locales = ['en', 'ar', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'tr', 'vi'];
    $now = now();

    // 1. Insert/update the 4 policy pages
    foreach ($pages as $p) {
        $existing = DB::table('pages')->where('slug', $p['slug'])->first();
        if ($existing) {
            $page_id = $existing->id;
            DB::table('pages')->where('id', $page_id)->update([
                'type' => 'page',
                'page_status' => 1,
                'post_status' => 0,
                'tool_status' => 0,
                'ads_status' => 1,
                'popular' => 0,
                'updated_at' => $now,
            ]);
            DB::table('page_translations')->where('page_id', $page_id)->delete();
        } else {
            $page_id = DB::table('pages')->insertGetId([
                'slug' => $p['slug'],
                'target' => '_self',
                'type' => 'page',
                'featured_image' => null,
                'tool_name' => null,
                'icon_image' => null,
                'custom_tool_link' => null,
                'post_status' => 0,
                'page_status' => 1,
                'tool_status' => 0,
                'ads_status' => 1,
                'popular' => 0,
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
        echo "SAVED POLICY PAGE: " . $p['slug'] . " (ID: " . $page_id . ")\\n";
    }

    unlink($jsonFile);

    // 2. Enhance Contact & Report pages description
    $contactDesc = '<p class="lead">Have a question about one of our 150+ free web tools? Want to report a technical issue, suggest a new feature, or discuss advertising and partnerships? We would love to hear from you.</p><p>Please fill out the contact form below or reach out directly to our support team at <a href="mailto:support@linkefly.xyz" class="fw-bold text-primary">support@linkefly.xyz</a>. We typically respond within 24 to 48 business hours.</p>';
    DB::table('page_translations')->where('page_id', 3)->update([
        'description' => $contactDesc,
        'subtitle' => 'Get in touch with the LinkeFly support and engineering team',
        'updated_at' => $now,
    ]);
    echo "UPDATED CONTACT PAGE TRANSLATIONS.\\n";

    $reportDesc = '<p class="lead">Found a broken link, unexpected error, or malfunctioning converter? Help us maintain the highest standard of reliability for millions of developers and users worldwide.</p><p>Please enter the URL or details below so our engineering team can investigate and fix it immediately.</p>';
    DB::table('page_translations')->where('page_id', 4)->update([
        'description' => $reportDesc,
        'subtitle' => 'Help us keep LinkeFly 100% fast, reliable, and error-free',
        'updated_at' => $now,
    ]);
    echo "UPDATED REPORT PAGE TRANSLATIONS.\\n";

    // 3. Clean up and set Header Menus
    DB::table('menus')->delete();
    $newMenus = [
        ['text' => 'Home', 'url' => '/', 'target' => '_self', 'menu_items' => '#', 'icon' => 'fas fa-home', 'type' => 'link', 'class' => null, 'parent_id' => 0, 'sort' => 1],
        ['text' => 'All Tools', 'url' => '#tools-box', 'target' => '_self', 'menu_items' => '#', 'icon' => 'fas fa-th-large', 'type' => 'link', 'class' => null, 'parent_id' => 0, 'sort' => 2],
        ['text' => 'Blog', 'url' => 'blog', 'target' => '_self', 'menu_items' => '#', 'icon' => 'fas fa-newspaper', 'type' => 'link', 'class' => null, 'parent_id' => 0, 'sort' => 3],
        ['text' => 'About Us', 'url' => 'about-us', 'target' => '_self', 'menu_items' => '#', 'icon' => 'fas fa-info-circle', 'type' => 'link', 'class' => null, 'parent_id' => 0, 'sort' => 4],
        ['text' => 'Contact', 'url' => 'contact', 'target' => '_self', 'menu_items' => '#', 'icon' => 'fas fa-envelope', 'type' => 'link', 'class' => null, 'parent_id' => 0, 'sort' => 5],
    ];
    foreach ($newMenus as $m) {
        $m['created_at'] = $now;
        $m['updated_at'] = $now;
        DB::table('menus')->insert($m);
    }
    echo "CLEAN HEADER MENUS INSTALLED.\\n";

    // 4. Update Footer Translations with full policy links
    $w1 = '<h3 class=\"text-primary font-weight-bolder\">LinkeFly</h3><p>LinkeFly provides 150+ fast, secure, and 100% free online web tools for developers, designers, content creators, and marketers. Boost your digital productivity with zero installation.</p>';
    $w2 = '<h3 class=\"text-primary font-weight-bolder\">Popular Tools</h3><ul class=\"flex-column ms-n3 nav\"><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Text to Slug\" href=\"/text-to-slug\">Text to Slug</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"QR Code Generator\" href=\"/qr-code-generator\">QR Code Generator</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Word Counter\" href=\"/word-counter\">Word Counter</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Case Converter\" href=\"/case-converter\">Case Converter</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Password Generator\" href=\"/password-generator\">Password Generator</a></li></ul>';
    $w3 = '<h3 class=\"text-primary font-weight-bolder\">Developer Tools</h3><ul class=\"flex-column ms-n3 nav\"><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"JSON Formatter\" href=\"/json-formatter\">JSON Formatter</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"HTML Minifier\" href=\"/html-minifier\">HTML Minifier</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"CSS Minifier\" href=\"/css-minifier\">CSS Minifier</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Base64 Encode\" href=\"/base64-encode\">Base64 Encode</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"MD5 Generator\" href=\"/md5-generator\">MD5 Generator</a></li></ul>';
    $w4 = '<h3 class=\"text-primary font-weight-bolder\">Image & Media</h3><ul class=\"flex-column ms-n3 nav\"><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Image Resizer\" href=\"/image-resizer\">Image Resizer</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Image Converter\" href=\"/image-converter\">Image Converter</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"PNG to WebP\" href=\"/png-to-webp\">PNG to WebP</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"WebP to PNG\" href=\"/webp-to-png\">WebP to PNG</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"ICO Converter\" href=\"/ico-converter\">ICO Converter</a></li></ul>';
    $w5 = '<h3 class=\"text-primary font-weight-bolder\">Company & Legal</h3><ul class=\"flex-column ms-n3 nav\"><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"About Us\" href=\"/about-us\">About Us</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Privacy Policy\" href=\"/privacy-policy\">Privacy Policy</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Terms of Service\" href=\"/terms-of-service\">Terms of Service</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Disclaimer\" href=\"/disclaimer\">Disclaimer</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Contact Us\" href=\"/contact\">Contact Us</a></li><li class=\"nav-item\"><a class=\"nav-link ps-0\" title=\"Report Issue\" href=\"/report\">Report Issue</a></li></ul>';
    $bottom = '<p>Copyright &copy; %year% <a title=\"LinkeFly\" href=\"https://linkefly.xyz/\" class=\"fw-bold text-primary\">LinkeFly</a>. All rights reserved. Fast, secure, and free online web tools.</p>';

    DB::table('footer_translations')->update([
        'widget1' => $w1,
        'widget2' => $w2,
        'widget3' => $w3,
        'widget4' => $w4,
        'widget5' => $w5,
        'bottom_text' => $bottom,
        'updated_at' => $now,
    ]);
    echo "FOOTER TRANSLATIONS UPDATED WITH POLICY LINKS.\\n";

    try {
        Artisan::call('cache:clear');
        Artisan::call('view:clear');
        echo "CACHES CLEARED.\\n";
    } catch (\\Throwable $t) {
        echo "CACHE CLEAR NOTE: " . $t->getMessage() . "\\n";
    }

    echo "ALL POLICY PAGES, MENUS, AND LEGAL LINKS DEPLOYED SUCCESSFULLY!\\n";

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
            ftp.delete("policy_pages_temp.json")
        except Exception:
            pass
        ftp.quit()

    print("--- OUTPUT ---")
    print(output)

if __name__ == "__main__":
    main()
