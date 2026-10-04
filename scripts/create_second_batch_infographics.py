#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = Path(__file__).parent / "blog_images"
OUTPUT_DIR.mkdir(exist_ok=True)

FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"
if not os.path.exists(FONT_PATH):
    FONT_PATH = "/Library/Fonts/Arial.ttf"

def get_font(size, bold=False):
    index = 1 if bold else 0
    try:
        return ImageFont.truetype(FONT_PATH, size, index=index)
    except:
        return ImageFont.load_default()

def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

# 1. Post 1: Slug Audit Checklist
def make_infographic_1_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "THE 7-POINT SEO URL SLUG AUDIT CHECKLIST", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Essential validation rules before publishing any page or article", font=get_font(17), fill="#94a3b8")

    items = [
        ("1. Primary Keyword in First 3 Words", "Ensures maximum topical weight in search algorithms", "#22c55e"),
        ("2. Standard Hyphens (Never Underscores)", "Search crawlers interpret hyphens as clean word breaks", "#3b82f6"),
        ("3. All Stop Words Eliminated", "Strips filler words like 'the', 'in', 'and', 'with', 'a'", "#a855f7"),
        ("4. Strictly Lowercase Characters", "Prevents duplicate content issues on case-sensitive servers", "#f59e0b"),
        ("5. Length Under 60 Characters", "Prevents truncation in desktop and mobile search engine snippets", "#ec4899"),
        ("6. No Dates or Ephemeral Numbers", "Ensures evergreen content relevance year after year", "#06b6d4"),
    ]

    y = 115
    for title, desc, col in items:
        draw_rounded_rect(d, (50, y, 910, y + 60), 12, "#1e293b", col, 1)
        d.text((75, y + 10), title, font=get_font(17, True), fill="#f8fafc")
        d.text((450, y + 10), desc, font=get_font(15), fill="#94a3b8")
        y += 68

    img.save(OUTPUT_DIR / "post1-inline-slug-checklist.png")
    print("Created post1-inline-slug-checklist.png")

# 2. Post 2: QR Matrix Anatomy
def make_infographic_2_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "ANATOMY OF A 2D QR CODE MATRIX", font=get_font(26, True), fill="#818cf8")
    d.text((50, 72), "Core structural elements that enable 360-degree high-speed scanning", font=get_font(17), fill="#94a3b8")

    parts = [
        ("Position Detection Patterns", "3 square nested targets at corners that tell cameras the orientation & angle", "#38bdf8"),
        ("Alignment Patterns", "Smaller squares that correct for distortion when scanned on curved surfaces", "#34d399"),
        ("Timing Patterns", "Alternating black & white tracks that define the coordinate grid size", "#fbbf24"),
        ("Format & Version Information", "Stores error correction level (L/M/Q/H) and masking pattern rules", "#f43f5e"),
        ("Quiet Zone Padding", "Mandatory blank 4-module border ensuring clean separation from surroundings", "#a78bfa"),
    ]

    y = 115
    for title, desc, col in parts:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(17, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78

    img.save(OUTPUT_DIR / "post2-inline-qr-anatomy.png")
    print("Created post2-inline-qr-anatomy.png")

# 3. Post 3: Readability Scores
def make_infographic_3_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "CONTENT READABILITY & ENGAGEMENT METRICS", font=get_font(26, True), fill="#fb923c")
    d.text((50, 72), "Key readability benchmarks that correlate with lower bounce rates", font=get_font(17), fill="#94a3b8")

    scores = [
        ("Flesch Reading Ease: 60 - 70", "Plain English: easily understood by 13- to 15-year-old students", "#10b981"),
        ("Average Sentence Length: 14 - 18 Words", "Maximizes comprehension without overwhelming reader attention span", "#3b82f6"),
        ("Paragraph Length: 2 - 4 Sentences", "Creates white space on mobile screens, facilitating rapid scanning", "#8b5cf6"),
        ("Passive Voice: Under 10%", "Active voice drives engagement and compelling calls-to-action", "#f59e0b"),
        ("Subheading Frequency: Every 250 Words", "Enables skimmable navigation and reinforces topical semantic hierarchy", "#ec4899"),
    ]

    y = 115
    for title, desc, col in scores:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(17, True), fill="#f8fafc")
        d.text((75, y + 38), desc, font=get_font(15), fill="#94a3b8")
        y += 78

    img.save(OUTPUT_DIR / "post3-inline-readability-scores.png")
    print("Created post3-inline-readability-scores.png")

# 4. Post 4: Network Waterfall
def make_infographic_4_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "NETWORK WATERFALL: UNMINIFIED VS MINIFIED ASSETS", font=get_font(26, True), fill="#2dd4bf")
    d.text((50, 72), "Comparing TCP packet transmission and main-thread parsing latency", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 125, 910, 290), 16, "#1e293b", "#ef4444", 2)
    d.text((75, 145), "Unminified Bundle (Multiple Round-Trips): 380 KB", font=get_font(18, True), fill="#f87171")
    d.text((75, 180), "• TCP Slow Start requires 7 round-trips to deliver initial stylesheets", font=get_font(15), fill="#cbd5e1")
    d.text((75, 210), "• JavaScript engine spends 420ms parsing redundant whitespace and comments", font=get_font(15), fill="#cbd5e1")
    d.text((75, 240), "• Render-blocking delay pushes First Contentful Paint to 2.4 seconds", font=get_font(15), fill="#fca5a5")

    draw_rounded_rect(d, (50, 320, 910, 485), 16, "#1e293b", "#22c55e", 2)
    d.text((75, 340), "Minified + Compressed Bundle (Single Congestion Window): 88 KB", font=get_font(18, True), fill="#4ade80")
    d.text((75, 375), "• Fits completely inside initial 10-packet TCP congestion window (14.6 KB segments)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 405), "• Main thread execution drops to 65ms, eliminating Total Blocking Time (TBT)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 435), "• First Contentful Paint (FCP) achieves sub-second rendering at 0.7s", font=get_font(15), fill="#86efac")

    img.save(OUTPUT_DIR / "post4-inline-waterfall-comparison.png")
    print("Created post4-inline-waterfall-comparison.png")

# 5. Post 5: Base64 Decision Matrix
def make_infographic_5_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "BASE64 DECISION MATRIX: INLINE URI VS EXTERNAL CDN", font=get_font(26, True), fill="#60a5fa")
    d.text((50, 72), "Engineers' framework for determining when Base64 is advantageous", font=get_font(17), fill="#94a3b8")

    rules = [
        ("Asset Size < 2 KB (Icons, Micro-SVGs)", "INLINE BASE64", "Saves extra HTTP DNS & handshake overhead", "#22c55e"),
        ("Single-File Packaging (HTML Emails)", "INLINE BASE64", "Ensures email clients display graphics reliably", "#22c55e"),
        ("Hero / Photographic Images (> 50 KB)", "EXTERNAL CDN", "Base64 bloats payload by 33% and hurts caching", "#ef4444"),
        ("Frequently Updated Dynamic Assets", "EXTERNAL CDN", "Inlining forces full stylesheet re-downloads on change", "#ef4444"),
        ("Font Files / Web Typography", "EXTERNAL CDN", "Fonts delay critical rendering path if embedded in CSS", "#f59e0b"),
    ]

    y = 115
    for condition, verdict, reason, col in rules:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), condition, font=get_font(16, True), fill="#f8fafc")
        d.text((520, y + 12), verdict, font=get_font(16, True), fill=col)
        d.text((75, y + 38), reason, font=get_font(14), fill="#94a3b8")
        y += 78

    img.save(OUTPUT_DIR / "post5-inline-base64-usecase-matrix.png")
    print("Created post5-inline-base64-usecase-matrix.png")

# 6. Post 6: JSON vs XML vs YAML
def make_infographic_6_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "DATA INTERCHANGE COMPARISON: JSON VS XML VS YAML", font=get_font(26, True), fill="#f59e0b")
    d.text((50, 72), "Evaluating payload efficiency, parse latency, and schema validation", font=get_font(17), fill="#94a3b8")

    formats = [
        ("JSON (RFC 8259)", "1.0x (Standard Baseline)", "Native browser parsing via JSON.parse(); dominant in REST APIs", "#3b82f6"),
        ("XML (Extensible Markup)", "1.6x – 2.2x Larger", "Heavy opening/closing tags; complex XPath/DOM parsing overhead", "#ef4444"),
        ("YAML (Human-Friendly)", "0.9x – 1.0x Compact", "Indentation-sensitive; slower parsing, primarily used in DevOps configs", "#10b981"),
        ("Protocol Buffers (Protobuf)", "0.4x – 0.6x Binary", "Ultra-compact binary serialization; requires schema compilation", "#a855f7"),
    ]

    y = 120
    for name, size, desc, col in formats:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), name, font=get_font(18, True), fill=col)
        d.text((420, y + 14), size, font=get_font(17, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 90

    img.save(OUTPUT_DIR / "post6-inline-json-vs-xml-yaml.png")
    print("Created post6-inline-json-vs-xml-yaml.png")

# 7. Post 7: Image Compression Curves
def make_infographic_7_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "IMAGE QUALITY VS FILE SIZE COMPRESSION CURVE", font=get_font(26, True), fill="#ec4899")
    d.text((50, 72), "Finding the optimal quality threshold for web performance", font=get_font(17), fill="#94a3b8")

    qualities = [
        ("Quality 100% (Uncompressed)", "File Size: 1.2 MB", "Visually indistinguishable from 85%, but 10x payload penalty", "#ef4444"),
        ("Quality 80% – 85% (Optimal Web Standard)", "File Size: 140 KB (-88%)", "Sweet spot: pristine visual fidelity with minimal byte weight", "#22c55e"),
        ("Quality 60% – 70% (High Compression)", "File Size: 75 KB (-94%)", "Ideal for mobile thumbnails and low-bandwidth connections", "#3b82f6"),
        ("Quality < 50% (Aggressive)", "File Size: 35 KB (-97%)", "Visible compression artifacts, banding, and blurry details", "#f59e0b"),
    ]

    y = 115
    for title, size, desc, col in qualities:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), title, font=get_font(17, True), fill=col)
        d.text((620, y + 14), size, font=get_font(16, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 90

    img.save(OUTPUT_DIR / "post7-inline-compression-curves.png")
    print("Created post7-inline-compression-curves.png")

# 8. Post 8: Hashing vs Encryption
def make_infographic_8_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "CRYPTOGRAPHIC HASHING VS ENCRYPTION", font=get_font(26, True), fill="#a855f7")
    d.text((50, 72), "Understanding the fundamental distinction between one-way and two-way cryptography", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 125, 465, 485), 16, "#1e293b", "#a855f7", 2)
    d.text((75, 145), "ONE-WAY HASHING (MD5, SHA)", font=get_font(18, True), fill="#c084fc")
    d.text((75, 190), "• Process: Strictly One-Way", font=get_font(16), fill="#f8fafc")
    d.text((75, 230), "• Output: Fixed-length digest", font=get_font(16), fill="#cbd5e1")
    d.text((75, 270), "• Reversible: Mathematically impossible", font=get_font(16), fill="#cbd5e1")
    d.text((75, 310), "• Key Required: No private key used", font=get_font(16), fill="#cbd5e1")
    d.text((75, 360), "Use Cases: Checksums, integrity verification, data indexing", font=get_font(15, True), fill="#a855f7")

    draw_rounded_rect(d, (495, 125, 910, 485), 16, "#1e293b", "#38bdf8", 2)
    d.text((520, 145), "TWO-WAY ENCRYPTION (AES, RSA)", font=get_font(18, True), fill="#38bdf8")
    d.text((520, 190), "• Process: Two-Way (Encrypt / Decrypt)", font=get_font(16), fill="#f8fafc")
    d.text((520, 230), "• Output: Variable ciphertext", font=get_font(16), fill="#cbd5e1")
    d.text((520, 270), "• Reversible: Yes, with secret key", font=get_font(16), fill="#cbd5e1")
    d.text((520, 310), "• Key Required: Symmetric or Asymmetric key", font=get_font(16), fill="#cbd5e1")
    d.text((520, 360), "Use Cases: SSL/TLS, database encryption, secure messaging", font=get_font(15, True), fill="#38bdf8")

    img.save(OUTPUT_DIR / "post8-inline-hashing-vs-encryption.png")
    print("Created post8-inline-hashing-vs-encryption.png")

# 9. Post 9: Casing Transformation Pipeline
def make_infographic_9_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "FULL-STACK CASING TRANSFORMATION PIPELINE", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "How naming conventions evolve across each layer of modern web architecture", font=get_font(17), fill="#94a3b8")

    steps = [
        ("1. Browser URL (kebab-case)", "https://linkefly.xyz/user-profile-settings", "#fb923c"),
        ("2. React / Vue Component (PascalCase)", "<UserProfileSettings user={userData} />", "#a855f7"),
        ("3. JavaScript State / Props (camelCase)", "const userProfileData = { firstName: 'Alice' };", "#38bdf8"),
        ("4. REST / GraphQL API Payload (camelCase)", "{ \"userProfileData\": { \"status\": \"active\" } }", "#34d399"),
        ("5. Relational Database (snake_case)", "SELECT * FROM user_profile_settings WHERE id = 1;", "#f59e0b"),
    ]

    y = 115
    for title, example, col in steps:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), example, font=get_font(15), fill="#f8fafc")
        y += 78

    img.save(OUTPUT_DIR / "post9-inline-casing-pipeline.png")
    print("Created post9-inline-casing-pipeline.png")

# 10. Post 10: Margin Impact Curve
def make_infographic_10_b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "TRANSACTION FEE DRAG ON GROSS PROFIT MARGINS", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "Effective merchant deduction percentage by Average Order Value (AOV)", font=get_font(17), fill="#94a3b8")

    brackets = [
        ("$3.00 Micro-Transaction", "Fee: $0.39  ->  Effective Drag: 13.0%", "CRITICAL RISK: Fixed fee consumes huge margin share", "#ef4444"),
        ("$10.00 Digital Download", "Fee: $0.59  ->  Effective Drag: 5.9%", "MODERATE DRAG: Encourage bundles to raise order value", "#f59e0b"),
        ("$50.00 E-Commerce Basket", "Fee: $1.75  ->  Effective Drag: 3.5%", "HEALTHY: Fixed fee drag diminishes significantly", "#3b82f6"),
        ("$200.00 SaaS Annual Plan", "Fee: $6.10  ->  Effective Drag: 3.05%", "OPTIMAL: Processing cost approaches raw interchange rate", "#22c55e"),
    ]

    y = 120
    for name, stat, desc, col in brackets:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), name, font=get_font(17, True), fill=col)
        d.text((450, y + 14), stat, font=get_font(16, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 90

    img.save(OUTPUT_DIR / "post10-inline-margin-impact.png")
    print("Created post10-inline-margin-impact.png")

if __name__ == "__main__":
    make_infographic_1_b()
    make_infographic_2_b()
    make_infographic_3_b()
    make_infographic_4_b()
    make_infographic_5_b()
    make_infographic_6_b()
    make_infographic_7_b()
    make_infographic_8_b()
    make_infographic_9_b()
    make_infographic_10_b()
    print("ALL 10 NEW INLINE INFOGRAPHICS CREATED SUCCESSFULLY!")
