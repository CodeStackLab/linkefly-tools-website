#!/usr/bin/env python3
import urllib.request
import ssl
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

OUTPUT_DIR = Path(__file__).parent / "blog_images"
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Post 1 & 2 from Gemini artifacts
gemini_post1 = Path("/Users/akeel/.gemini/antigravity/brain/b4509a58-104a-451d-9391-6b836abcaa44/seo_url_slugs_1791090855331.jpg")
gemini_post2 = Path("/Users/akeel/.gemini/antigravity/brain/b4509a58-104a-451d-9391-6b836abcaa44/custom_qr_codes_1791090876481.jpg")

if gemini_post1.exists():
    shutil.copy(gemini_post1, OUTPUT_DIR / "post1-featured.jpg")
    print("Copied post1-featured.jpg")

if gemini_post2.exists():
    shutil.copy(gemini_post2, OUTPUT_DIR / "post2-featured.jpg")
    print("Copied post2-featured.jpg")

# Unsplash high-res curated tech photos for posts 3-10
curated_photos = {
    "post3-featured.jpg": "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=1200&h=675&q=85", # writing, word count, notebook, typewriter
    "post4-featured.jpg": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&h=675&q=85", # code minification, html css code screen
    "post5-featured.jpg": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&h=675&q=85", # matrix, binary, base64 data encoding
    "post6-featured.jpg": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&h=675&q=85", # json analytics, dashboard, api debugging
    "post7-featured.jpg": "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=1200&h=675&q=85", # webp vs png image compression, visual media
    "post8-featured.jpg": "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&h=675&q=85", # cyber security, lock, password protection
    "post9-featured.jpg": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&h=675&q=85", # programmer laptop, casing conventions, code
    "post10-featured.jpg": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=1200&h=675&q=85" # credit card terminal, stripe paypal fee calculator
}

for fname, url in curated_photos.items():
    dest = OUTPUT_DIR / fname
    print(f"Downloading {fname}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            dest.write_bytes(resp.read())
        print(f"Saved {fname} ({dest.stat().st_size} bytes)")
    except Exception as e:
        print(f"Error fetching {fname}: {e}")

print("All featured images ready in", OUTPUT_DIR)
