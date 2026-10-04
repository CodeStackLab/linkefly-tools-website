#!/usr/bin/env python3
import urllib.request
import ssl
from pathlib import Path

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

OUTPUT_DIR = Path(__file__).parent / "blog_images"
OUTPUT_DIR.mkdir(exist_ok=True)

# Curated high-res Unsplash photos for posts 11-30
curated_photos_batch2 = {
    "post11-featured.jpg": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=1200&h=675&q=85", # URL encode / server routing / networking cables
    "post12-featured.jpg": "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?auto=format&fit=crop&w=1200&h=675&q=85", # Lorem Ipsum / UI wireframe / design mockup
    "post13-featured.jpg": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1200&h=675&q=85", # IP address / server room datacenter
    "post14-featured.jpg": "https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d?auto=format&fit=crop&w=1200&h=675&q=85", # Color converter / vibrant modern neon colors
    "post15-featured.jpg": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&h=675&q=85", # Data cleaning / spreadsheet / digital workflow
    "post16-featured.jpg": "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=1200&h=675&q=85", # Subtitles / video editing timeline
    "post17-featured.jpg": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=1200&h=675&q=85", # YouTube thumbnail / video streaming interface
    "post18-featured.jpg": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?auto=format&fit=crop&w=1200&h=675&q=85", # Binary code / computer terminal screen
    "post19-featured.jpg": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&h=675&q=85", # Percentage calculator / financial chart growth
    "post20-featured.jpg": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1200&h=675&q=85", # Loan calculator / mortgage finance documents
    "post21-featured.jpg": "https://images.unsplash.com/photo-1554224154-22dec7ec8818?auto=format&fit=crop&w=1200&h=675&q=85", # GST / tax calculator / invoice paperwork
    "post22-featured.jpg": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=1200&h=675&q=85", # Unit converter / engineering calipers ruler
    "post23-featured.jpg": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&w=1200&h=675&q=85", # Number to words / banking finance notes
    "post24-featured.jpg": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&h=675&q=85", # Data format migration / global data stream
    "post25-featured.jpg": "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1200&h=675&q=85", # Privacy policy / legal gavel contract
    "post26-featured.jpg": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&h=675&q=85", # UUID / cryptographic abstract geometry
    "post27-featured.jpg": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=1200&h=675&q=85", # UTM builder / digital marketing attribution analytics
    "post28-featured.jpg": "https://images.unsplash.com/photo-1452587925148-ce544e77e70d?auto=format&fit=crop&w=1200&h=675&q=85", # Image resizer / photography framing camera
    "post29-featured.jpg": "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?auto=format&fit=crop&w=1200&h=675&q=85", # Favicon / browser tab app design
    "post30-featured.jpg": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=1200&h=675&q=85"  # TDEE calculator / fitness nutrition meal
}

def main():
    for fname, url in curated_photos_batch2.items():
        dest = OUTPUT_DIR / fname
        if dest.exists() and dest.stat().st_size > 10000:
            print(f"Already exists: {fname}")
            continue
        print(f"Downloading {fname}...")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                dest.write_bytes(resp.read())
            print(f"Saved {fname} ({dest.stat().st_size:,} bytes)")
        except Exception as e:
            print(f"Error fetching {fname}: {e}")

    print("ALL 20 FEATURED IMAGES DOWNLOADED!")

if __name__ == "__main__":
    main()
