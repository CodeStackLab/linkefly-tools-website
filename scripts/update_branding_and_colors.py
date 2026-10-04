#!/usr/bin/env python3
import json
import ftplib
import io
from pathlib import Path
from run_remote_php import run_php

CONFIG_FILE = Path(__file__).parent / ".ftp_config.json"

def main():
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)

    # 1. Upload admin_avatar.png
    print("Uploading admin_avatar.png...")
    ftp = ftplib.FTP()
    ftp.connect(cfg["host"], cfg["port"], timeout=30)
    ftp.login(cfg["username"], cfg["password"])
    ftp.cwd("assets/img")
    with open("admin_avatar.png", "rb") as f:
        ftp.storbinary("STOR avatar.png", f)
    with open("admin_avatar.png", "rb") as f:
        ftp.storbinary("STOR avatar.jpg", f)
    ftp.quit()
    print("Uploaded avatar.png and avatar.jpg successfully.")

    # 2. Update Database: users, generals, sidebars, page_categories
    php_code = """
    // Update admin user
    DB::table('users')->where('id', 1)->update([
        'avatar' => 'https://linkefly.xyz/assets/img/avatar.png',
        'fullname' => 'LinkeFly Editorial Team',
        'position' => 'Lead Developer & Tech Editor',
        'bio' => 'Official LinkeFly engineering and editorial team. Dedicated to building fast, secure, and 100% free online utilities and publishing in-depth guides for web developers, designers, and digital marketers.',
        'updated_at' => now(),
    ]);
    echo "USER PROFILE UPDATED.\\n";

    // Update generals colors
    DB::table('generals')->where('id', 1)->update([
        'gradient_first_color' => '#1e1b4b',
        'gradient_second_color' => '#2563eb',
        'solid_color' => '#2563eb',
        'main_color' => '#2563eb',
        'heading_background' => 'bg-indigo',
        'related_tools_background' => 'bg-indigo',
        'updated_at' => now(),
    ]);
    echo "GENERALS COLORS UPDATED.\\n";

    // Update sidebars
    DB::table('sidebars')->where('id', 1)->update([
        'post_background' => 'bg-indigo',
        'tool_background' => 'bg-indigo',
        'updated_at' => now(),
    ]);
    echo "SIDEBARS UPDATED.\\n";

    // Update page_categories
    DB::table('page_categories')->update([
        'background' => 'bg-indigo',
        'updated_at' => now(),
    ]);
    echo "PAGE CATEGORIES UPDATED.\\n";

    // Append custom modern styling
    $customCss = '
/* Modern LinkeFly Color Palette & Tool Styling */
.category-box {
    background: linear-gradient(135deg, #1e1b4b 0%, #2563eb 100%) !important;
    border-radius: 8px 8px 0 0 !important;
    color: #ffffff !important;
    padding: 1rem 1.25rem !important;
}
.category-box h3 a {
    color: #ffffff !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em;
}
.category-box span {
    color: rgba(255, 255, 255, 0.85) !important;
    font-size: 0.9rem !important;
}
.item-box {
    transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
    border: 1px solid rgba(226, 232, 240, 0.9) !important;
    border-radius: 10px !important;
    background: #ffffff !important;
}
.item-box:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 22px -5px rgba(37, 99, 235, 0.15), 0 4px 6px -2px rgba(37, 99, 235, 0.06) !important;
    border-color: #3b82f6 !important;
}
.item-box .fw-medium {
    color: #1e293b !important;
    font-weight: 600 !important;
    transition: color 0.18s ease !important;
}
.item-box:hover .fw-medium {
    color: #2563eb !important;
}
.theme-dark .item-box {
    background: #1e293b !important;
    border-color: #334155 !important;
}
.theme-dark .item-box .fw-medium {
    color: #f1f5f9 !important;
}
.theme-dark .item-box:hover {
    border-color: #60a5fa !important;
    box-shadow: 0 10px 25px -5px rgba(96, 165, 250, 0.2) !important;
}
.theme-dark .item-box:hover .fw-medium {
    color: #60a5fa !important;
}
.btn-primary {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
    border-color: #2563eb !important;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
}
.btn-primary:hover {
    background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%) !important;
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35) !important;
}
';

    $ltrPath = __DIR__ . '/assets/css/custom.ltr.css';
    $rtlPath = __DIR__ . '/assets/css/custom.rtl.css';
    
    // Check if already appended
    $currLtr = file_get_contents($ltrPath);
    if (strpos($currLtr, '/* Modern LinkeFly Color Palette & Tool Styling */') === false) {
        file_put_contents($ltrPath, $currLtr . "\n" . $customCss);
        echo "APPENDED CSS TO custom.ltr.css\\n";
    }
    if (file_exists($rtlPath)) {
        $currRtl = file_get_contents($rtlPath);
        if (strpos($currRtl, '/* Modern LinkeFly Color Palette & Tool Styling */') === false) {
            file_put_contents($rtlPath, $currRtl . "\n" . $customCss);
            echo "APPENDED CSS TO custom.rtl.css\\n";
        }
    }

    try {
        Artisan::call('cache:clear');
        Artisan::call('view:clear');
        echo "CACHES CLEARED.\\n";
    } catch (\Throwable $t) {
        echo "CACHE NOTE: " . $t->getMessage() . "\\n";
    }
    """

    res = run_php(php_code)
    print("--- RESULT ---")
    print(res)

if __name__ == "__main__":
    main()
