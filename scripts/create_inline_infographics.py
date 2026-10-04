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

# Post 1: Slug Anatomy
def make_infographic_1():
    img = Image.new("RGB", (960, 540), "#0f172a") # Slate 900
    d = ImageDraw.Draw(img)
    # Header
    d.text((50, 40), "URL SLUG ANATOMY & STRUCTURE", font=get_font(28, True), fill="#38bdf8")
    d.text((50, 78), "Comparing unoptimized dynamic URLs vs SEO-friendly slugs", font=get_font(18), fill="#94a3b8")
    
    # Box 1: Bad URL
    draw_rounded_rect(d, (50, 130, 910, 250), 16, "#1e293b", "#ef4444", 2)
    d.text((75, 150), "BAD: Dynamic Query URL", font=get_font(18, True), fill="#ef4444")
    d.text((75, 185), "https://example.com/index.php?p=8923&cat=12&ref=tw_feed&sid=9a8d2", font=get_font(20), fill="#f87171")
    d.text((75, 220), "• Poor readability  • No keywords  • Low click-through rate  • Crawl ambiguity", font=get_font(15), fill="#cbd5e1")

    # Box 2: Good URL
    draw_rounded_rect(d, (50, 280, 910, 400), 16, "#1e293b", "#22c55e", 2)
    d.text((75, 300), "GOOD: Clean SEO-Optimized Slug", font=get_font(18, True), fill="#22c55e")
    d.text((75, 335), "https://linkefly.xyz/blog/how-to-create-seo-friendly-url-slugs", font=get_font(20, True), fill="#4ade80")
    d.text((75, 370), "• Primary keyword included  • Hyphen-separated  • Clean hierarchy  • 100% Human-readable", font=get_font(15), fill="#cbd5e1")

    # Footer note
    draw_rounded_rect(d, (50, 430, 910, 490), 12, "#334155")
    d.text((75, 448), "Pro Tip: Keep slugs between 3 to 5 words for maximum SERP visibility and social sharing.", font=get_font(16, True), fill="#38bdf8")
    
    img.save(OUTPUT_DIR / "post1-inline-slug-structure.png")
    print("Created post1-inline-slug-structure.png")

# Post 2: QR Error Correction
def make_infographic_2():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "QR CODE ERROR CORRECTION LEVELS (ECC)", font=get_font(28, True), fill="#818cf8")
    d.text((50, 78), "How much damage or occlusion a QR code can sustain and still scan", font=get_font(18), fill="#94a3b8")

    levels = [
        ("Level L (Low)", "~7% Recovery", "Best for simple text & high data density on clean screens", "#38bdf8"),
        ("Level M (Medium)", "~15% Recovery", "Standard default for websites, marketing URLs, & packaging", "#34d399"),
        ("Level Q (Quartile)", "~25% Recovery", "Great for outdoor posters, flyers, and retail product tags", "#fbbf24"),
        ("Level H (High)", "~30% Recovery", "Essential when embedding custom logos or in industrial environments", "#f87171"),
    ]

    y = 130
    for name, rec, desc, col in levels:
        draw_rounded_rect(d, (50, y, 910, y + 75), 14, "#1e293b", col, 2)
        d.text((75, y + 16), name, font=get_font(18, True), fill=col)
        d.text((320, y + 16), rec, font=get_font(18, True), fill="#f1f5f9")
        d.text((75, y + 44), desc, font=get_font(15), fill="#94a3b8")
        y += 88

    img.save(OUTPUT_DIR / "post2-inline-qr-error-levels.png")
    print("Created post2-inline-qr-error-levels.png")

# Post 3: Word Count Guide
def make_infographic_3():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "OPTIMAL WORD & CHARACTER COUNT MATRIX", font=get_font(28, True), fill="#fb923c")
    d.text((50, 78), "Recommended character & word lengths across search and social platforms", font=get_font(18), fill="#94a3b8")

    rows = [
        ("SEO Meta Title", "50 – 60 Chars", "Prevents SERP truncation on desktop and mobile", "#f43f5e"),
        ("SEO Meta Description", "150 – 160 Chars", "Maximizes CTR without being clipped by Google snippets", "#ec4899"),
        ("Long-Form SEO Article", "1,800 – 2,500 Words", "Highest correlation with Page 1 Google ranking positions", "#8b5cf6"),
        ("Social Post (LinkedIn)", "100 – 200 Words", "Highest engagement rate before the 'see more' cutoff", "#3b82f6"),
        ("Email Newsletter", "200 – 400 Words", "Optimal for skim reading and above-the-fold call to action", "#10b981"),
    ]

    y = 125
    for title, length, desc, col in rows:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 14), title, font=get_font(17, True), fill="#f8fafc")
        d.text((360, y + 14), length, font=get_font(17, True), fill=col)
        d.text((75, y + 40), desc, font=get_font(14), fill="#94a3b8")
        y += 78

    img.save(OUTPUT_DIR / "post3-inline-word-count-table.png")
    print("Created post3-inline-word-count-table.png")

# Post 4: Minification Performance
def make_infographic_4():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "CODE MINIFICATION BENCHMARK", font=get_font(28, True), fill="#2dd4bf")
    d.text((50, 78), "Real-world web performance impact of minifying HTML & CSS", font=get_font(18), fill="#94a3b8")

    # Column 1: Unminified
    draw_rounded_rect(d, (50, 130, 460, 480), 16, "#1e293b", "#ef4444", 2)
    d.text((80, 155), "UNMINIFIED CODE", font=get_font(20, True), fill="#ef4444")
    d.text((80, 205), "Bundle Size: 245 KB", font=get_font(18), fill="#f8fafc")
    d.text((80, 250), "LCP (Largest Contentful Paint): 2.8s", font=get_font(16), fill="#cbd5e1")
    d.text((80, 295), "Total Requests Payload: 480 KB", font=get_font(16), fill="#cbd5e1")
    d.text((80, 340), "Google Lighthouse Score: 71 / 100", font=get_font(16), fill="#f87171")
    d.text((80, 410), "Status: POOR CWV RATING", font=get_font(16, True), fill="#ef4444")

    # Column 2: Minified
    draw_rounded_rect(d, (500, 130, 910, 480), 16, "#1e293b", "#22c55e", 2)
    d.text((530, 155), "MINIFIED WITH LINKEFLY", font=get_font(20, True), fill="#22c55e")
    d.text((530, 205), "Bundle Size: 92 KB (-62%)", font=get_font(18, True), fill="#4ade80")
    d.text((530, 250), "LCP (Largest Contentful Paint): 0.9s", font=get_font(16), fill="#cbd5e1")
    d.text((530, 295), "Total Requests Payload: 195 KB", font=get_font(16), fill="#cbd5e1")
    d.text((530, 340), "Google Lighthouse Score: 98 / 100", font=get_font(16), fill="#4ade80")
    d.text((530, 410), "Status: EXCELLENT PASSING SCORE", font=get_font(16, True), fill="#22c55e")

    img.save(OUTPUT_DIR / "post4-inline-minification-speed.png")
    print("Created post4-inline-minification-speed.png")

# Post 5: Base64 Flowchart
def make_infographic_5():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "HOW BASE64 ENCODING WORKS (3 BYTES TO 4 CHARS)", font=get_font(26, True), fill="#60a5fa")
    d.text((50, 78), "Binary bit manipulation converting raw data to printable ASCII", font=get_font(18), fill="#94a3b8")

    steps = [
        ("Step 1: Input Text / Bytes", "Text: 'Man'  ->  Binary: [ 01001101 ]  [ 01100001 ]  [ 01101110 ] (24 Bits)", "#38bdf8"),
        ("Step 2: Split into 6-Bit Chunks", "6-Bit Groups: [ 010011 ]  [ 010110 ]  [ 000101 ]  [ 101110 ]", "#818cf8"),
        ("Step 3: Convert to Decimals", "Decimal Values: [ 19 ]  [ 22 ]  [ 5 ]  [ 46 ]", "#a78bfa"),
        ("Step 4: Base64 Table Lookup", "Resulting ASCII String: 'TWFu' (4 characters, safe for JSON and URLs)", "#34d399")
    ]

    y = 125
    for title, desc, col in steps:
        draw_rounded_rect(d, (50, y, 910, y + 80), 14, "#1e293b", col, 2)
        d.text((75, y + 16), title, font=get_font(18, True), fill=col)
        d.text((75, y + 46), desc, font=get_font(16), fill="#e2e8f0")
        y += 94

    img.save(OUTPUT_DIR / "post5-inline-base64-process.png")
    print("Created post5-inline-base64-process.png")

# Post 6: JSON Rules
def make_infographic_6():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "JSON FORMATTING: TOP 4 SYNTAX PITFALLS", font=get_font(28, True), fill="#f59e0b")
    d.text((50, 78), "Common errors that cause JSON.parse() exceptions in APIs", font=get_font(18), fill="#94a3b8")

    mistakes = [
        ("Trailing Commas", "INVALID: {\"id\": 1, \"name\": \"User\",}", "VALID: {\"id\": 1, \"name\": \"User\"}", "#ef4444"),
        ("Single Quotes", "INVALID: {'status': 'active'}", "VALID: {\"status\": \"active\"} (Double quotes only)", "#f97316"),
        ("Unquoted Object Keys", "INVALID: {age: 28, verified: true}", "VALID: {\"age\": 28, \"verified\": true}", "#eab308"),
        ("Undefined Values", "INVALID: {\"token\": undefined}", "VALID: {\"token\": null} (Must use null)", "#06b6d4")
    ]

    y = 125
    for title, inv, val, col in mistakes:
        draw_rounded_rect(d, (50, y, 910, y + 80), 14, "#1e293b", col, 1)
        d.text((75, y + 14), title, font=get_font(18, True), fill=col)
        d.text((75, y + 44), inv, font=get_font(15), fill="#f87171")
        d.text((490, y + 44), val, font=get_font(15, True), fill="#4ade80")
        y += 92

    img.save(OUTPUT_DIR / "post6-inline-json-structure.png")
    print("Created post6-inline-json-structure.png")

# Post 7: WebP vs PNG vs JPG
def make_infographic_7():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "IMAGE FORMAT COMPARISON MATRIX", font=get_font(28, True), fill="#ec4899")
    d.text((50, 78), "Choosing between WebP, PNG, and JPG for modern websites", font=get_font(18), fill="#94a3b8")

    cols = [
        ("WebP (Modern Standard)", "File Size: 25-35% smaller than JPG\nSupports: Alpha Transparency & Animation\nBest for: All modern web applications & hero banners\nBrowser Support: 97%+ worldwide", "#10b981"),
        ("PNG (Lossless Quality)", "File Size: Largest among formats\nSupports: Crisp 24-bit alpha transparency\nBest for: Logos, UI icons, screenshots, vector art\nBrowser Support: 100% universal", "#3b82f6"),
        ("JPG / JPEG (Standard)", "File Size: Moderate with lossy compression\nSupports: No transparency or animation\nBest for: High-detail photography and legacy support\nBrowser Support: 100% universal", "#f59e0b")
    ]

    x = 50
    for name, text, col in cols:
        draw_rounded_rect(d, (x, 130, x + 270, 490), 16, "#1e293b", col, 2)
        d.text((x + 15, 150), name, font=get_font(16, True), fill=col)
        lines = text.split("\n")
        ly = 210
        for l in lines:
            d.text((x + 15, ly), l, font=get_font(14), fill="#e2e8f0")
            ly += 55
        x += 300

    img.save(OUTPUT_DIR / "post7-inline-format-matrix.png")
    print("Created post7-inline-format-matrix.png")

# Post 8: Password Cracking Time
def make_infographic_8():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "PASSWORD ENTROPY & BRUTE-FORCE CRACK TIME", font=get_font(28, True), fill="#a855f7")
    d.text((50, 78), "Time required for GPU clusters to crack password combinations", font=get_font(18), fill="#94a3b8")

    rows = [
        ("8 Characters (Numbers only)", "Instant (0.01 seconds)", "UNSAFE", "#ef4444"),
        ("8 Characters (Upper + Lowercase)", "22 Minutes", "WEAK", "#f97316"),
        ("10 Characters (Letters + Numbers)", "7 Months", "MODERATE", "#eab308"),
        ("12 Characters (Letters, Numbers, Symbols)", "34,000 Years", "STRONG", "#22c55e"),
        ("16 Characters (Fully Complex)", "1 Trillion Years", "MAXIMUM SECURITY", "#06b6d4")
    ]

    y = 125
    for name, time_str, rating, col in rows:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 14), name, font=get_font(17, True), fill="#f8fafc")
        d.text((510, y + 14), time_str, font=get_font(17, True), fill=col)
        d.text((750, y + 14), rating, font=get_font(15, True), fill=col)
        y += 76

    img.save(OUTPUT_DIR / "post8-inline-password-crack-time.png")
    print("Created post8-inline-password-crack-time.png")

# Post 9: Casing Cheat Sheet
def make_infographic_9():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "PROGRAMMING CASING STANDARDS CHEAT SHEET", font=get_font(28, True), fill="#38bdf8")
    d.text((50, 78), "Standard naming conventions by programming language and role", font=get_font(18), fill="#94a3b8")

    cases = [
        ("camelCase", "userProfileData", "JavaScript variables, TypeScript methods, Java fields", "#38bdf8"),
        ("PascalCase", "UserProfileController", "Classes in C#, Java, PHP, React components", "#a855f7"),
        ("snake_case", "user_profile_data", "Python variables, SQL table columns, Ruby methods", "#34d399"),
        ("kebab-case", "user-profile-data", "URL slugs, CSS class selectors, HTML attributes", "#fb923c"),
    ]

    y = 130
    for name, ex, use, col in cases:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 16), name, font=get_font(18, True), fill=col)
        d.text((260, y + 16), ex, font=get_font(18, True), fill="#f8fafc")
        d.text((75, y + 46), use, font=get_font(15), fill="#94a3b8")
        y += 90

    img.save(OUTPUT_DIR / "post9-inline-casing-cheat-sheet.png")
    print("Created post9-inline-casing-cheat-sheet.png")

# Post 10: Gateway Fees
def make_infographic_10():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 40), "PAYMENT GATEWAY FEE BREAKDOWN: STRIPE & PAYPAL", font=get_font(28, True), fill="#10b981")
    d.text((50, 78), "Understanding how processing fees affect your merchant revenue", font=get_font(18), fill="#94a3b8")

    draw_rounded_rect(d, (50, 130, 910, 240), 16, "#1e293b", "#3b82f6", 2)
    d.text((75, 150), "Standard Domestic Rate: 2.9% + $0.30 per transaction", font=get_font(20, True), fill="#38bdf8")
    d.text((75, 190), "On a $100.00 customer order: Fee is $2.90 + $0.30 = $3.20  ->  Net Payout: $96.80", font=get_font(17), fill="#e2e8f0")

    draw_rounded_rect(d, (50, 260, 910, 370), 16, "#1e293b", "#f59e0b", 2)
    d.text((75, 280), "International / Cross-Border Rate: 3.9% + $0.30 + 1% Currency Conversion", font=get_font(20, True), fill="#fbbf24")
    d.text((75, 320), "On a $100.00 international order: Total deductions reach $5.20  ->  Net Payout: $94.80", font=get_font(17), fill="#e2e8f0")

    draw_rounded_rect(d, (50, 390, 910, 490), 14, "#334155")
    d.text((75, 415), "Tip: Use LinkeFly's Stripe & PayPal Fee Calculators to reverse-calculate prices", font=get_font(17, True), fill="#34d399")
    d.text((75, 445), "To receive exactly $100.00 in your bank account, you must charge the buyer $103.30.", font=get_font(16), fill="#cbd5e1")

    img.save(OUTPUT_DIR / "post10-inline-gateway-fees.png")
    print("Created post10-inline-gateway-fees.png")

if __name__ == "__main__":
    make_infographic_1()
    make_infographic_2()
    make_infographic_3()
    make_infographic_4()
    make_infographic_5()
    make_infographic_6()
    make_infographic_7()
    make_infographic_8()
    make_infographic_9()
    make_infographic_10()
    print("ALL 10 INLINE INFOGRAPHICS CREATED!")
