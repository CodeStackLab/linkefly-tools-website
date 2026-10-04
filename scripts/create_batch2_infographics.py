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

# Post 11: Percent-Encoding Reserved Characters (RFC 3986)
def make_infographic_11():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "RFC 3986 PERCENT-ENCODING REFERENCE TABLE", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Reserved characters requiring percent-encoding in URL query strings and paths", font=get_font(17), fill="#94a3b8")

    items = [
        ("Space ' '", "%20 or '+'", "Path segments use %20; query strings frequently accept '+' as delimiter", "#38bdf8"),
        ("Slash '/'", "%2F", "Used as path delimiter; must be encoded when inside parameter values", "#34d399"),
        ("Question Mark '?'", "%3F", "Marks query string boundary; unencoded instances break URL parsing", "#fbbf24"),
        ("Ampersand '&'", "%26", "Key-value pair separator; unencoded instances inject unintended params", "#f87171"),
        ("Equal Sign '='", "%3D", "Parameter key/value assignment operator; encode in user inputs", "#a78bfa"),
        ("Hash '#' & Colon ':'", "%23 / %3A", "Fragment identifier and protocol/port delimiter characters", "#f43f5e"),
    ]

    y = 115
    for char, code, desc, col in items:
        draw_rounded_rect(d, (50, y, 910, y + 60), 12, "#1e293b", col, 1)
        d.text((75, y + 10), char, font=get_font(17, True), fill="#f8fafc")
        d.text((310, y + 10), code, font=get_font(17, True), fill=col)
        d.text((450, y + 12), desc, font=get_font(14), fill="#cbd5e1")
        y += 68

    img.save(OUTPUT_DIR / "post11-inline-percent-encoding.png")
    print("Created post11-inline-percent-encoding.png")

# Post 12: Wireframing Content Hierarchy
def make_infographic_12():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "UI WIREFRAME CONTENT HIERARCHY & PLACEHOLDER FLOW", font=get_font(26, True), fill="#818cf8")
    d.text((50, 72), "Balancing visual layout fidelity with realistic typographic volume", font=get_font(17), fill="#94a3b8")

    stages = [
        ("Phase 1: Low-Fidelity Wireframes", "Lorem Ipsum Dummy Text", "Prevents stakeholders from debating copy before UX grid is approved", "#38bdf8"),
        ("Phase 2: Component Stress Testing", "Variable Character Counts", "Ensures cards, buttons & badges do not break with 10 vs 150 characters", "#a855f7"),
        ("Phase 3: High-Fidelity Interactive Mockup", "Realistic Draft Copy", "Tests reading flow, call-to-action visibility, and visual line wrap", "#34d399"),
        ("Phase 4: Production Release", "Final Validated Copy & SEO Metadata", "Live copy aligned with keyword targeting and accessibility standards", "#22c55e"),
    ]

    y = 120
    for phase, tactic, desc, col in stages:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), phase, font=get_font(17, True), fill=col)
        d.text((450, y + 14), tactic, font=get_font(16, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#94a3b8")
        y += 92

    img.save(OUTPUT_DIR / "post12-inline-wireframe-hierarchy.png")
    print("Created post12-inline-wireframe-hierarchy.png")

# Post 13: IPv4 vs IPv6 Architecture
def make_infographic_13():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "INTERNET PROTOCOL COMPARISON: IPv4 VS IPv6", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Architectural shift from exhausted 32-bit addresses to 128-bit hexadecimal space", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 125, 465, 485), 16, "#1e293b", "#f59e0b", 2)
    d.text((75, 145), "IPv4 (RFC 791 - 1981)", font=get_font(18, True), fill="#fbbf24")
    d.text((75, 190), "• Address Length: 32 bits (4 bytes)", font=get_font(16), fill="#f8fafc")
    d.text((75, 230), "• Address Space: 4.29 Billion (~4.3 x 10^9)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 270), "• Format: Dotted Decimal (192.168.1.1)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 310), "• Header Size: 20-60 bytes (variable)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 350), "• NAT Required: Yes (Carrier-Grade NAT)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 400), "Status: Globally Exhausted (IANA 2011)", font=get_font(15, True), fill="#f87171")

    draw_rounded_rect(d, (495, 125, 910, 485), 16, "#1e293b", "#38bdf8", 2)
    d.text((520, 145), "IPv6 (RFC 8200 - 2017)", font=get_font(18, True), fill="#38bdf8")
    d.text((520, 190), "• Address Length: 128 bits (16 bytes)", font=get_font(16), fill="#f8fafc")
    d.text((520, 230), "• Address Space: 340 Undecillion (3.4 x 10^38)", font=get_font(15), fill="#cbd5e1")
    d.text((520, 270), "• Format: 8 Hex Heptads (2001:db8::1)", font=get_font(15), fill="#cbd5e1")
    d.text((520, 310), "• Header Size: Fixed 40 bytes (fast routing)", font=get_font(15), fill="#cbd5e1")
    d.text((520, 350), "• NAT Required: No (End-to-end direct)", font=get_font(15), fill="#cbd5e1")
    d.text((520, 400), "Status: Native Standard on 5G & Cloud", font=get_font(15, True), fill="#4ade80")

    img.save(OUTPUT_DIR / "post13-inline-ipv4-vs-ipv6.png")
    print("Created post13-inline-ipv4-vs-ipv6.png")

# Post 14: Color Spaces: HEX vs RGB vs HSL
def make_infographic_14():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "DIGITAL COLOR MODELS: HEX VS RGB VS HSL", font=get_font(26, True), fill="#ec4899")
    d.text((50, 72), "Understanding which color model to select for CSS styling, design systems & canvas", font=get_font(17), fill="#94a3b8")

    models = [
        ("HEX (#3B82F6)", "Compact & Universally Supported", "6-character hexadecimal notation ideal for static CSS declarations & design tokens", "#38bdf8"),
        ("RGB / RGBA (rgb(59, 130, 246))", "Hardware Native Channels", "Direct representation of Red, Green, Blue monitor subpixels with 0-255 depth", "#34d399"),
        ("HSL / HSLA (hsl(217, 91%, 60%))", "Human-Intuitive Design", "Hue (0-360), Saturation %, Lightness %; simplifies dynamic dark/light themes", "#fbbf24"),
        ("OKLCH (oklch(0.62 0.19 259))", "Perceptually Uniform Modern Standard", "Wide color gamut (P3) with predictable brightness across varying hues", "#a855f7"),
    ]

    y = 120
    for name, trait, desc, col in models:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), name, font=get_font(17, True), fill=col)
        d.text((480, y + 14), trait, font=get_font(16, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 90

    img.save(OUTPUT_DIR / "post14-inline-color-spaces.png")
    print("Created post14-inline-color-spaces.png")

# Post 15: Text Sanitization Pipeline
def make_infographic_15():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "DATA SANITIZATION & DELIMITER PIPELINE", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "Step-by-step transformation from unstructured raw copy to SQL/CSV-ready lists", font=get_font(17), fill="#94a3b8")

    stages = [
        ("Step 1: Trim Leading/Trailing Whitespace", "Regex: /^\\s+|\\s+$/g", "Strips accidental copy-paste padding around entries", "#38bdf8"),
        ("Step 2: Normalize Multi-Line Breaks", "Regex: /\\r?\\n+/g", "Collapses inconsistent Windows (\\r\\n) and Unix (\\n) line feeds", "#34d399"),
        ("Step 3: Strip Punctuation & Quotes", "Regex: /[\\\"'`;]/g", "Eliminates syntax-breaking characters prior to database ingestion", "#fbbf24"),
        ("Step 4: Delimiter Formatting (Comma / Pipe)", "Join: array.join(', ')", "Generates structured IN (...) SQL clauses or clean CSV columns", "#a855f7"),
        ("Step 5: Deduplication & Case Normalization", "Set: [...new Set(arr)]", "Removes duplicate records and unifies case sensitivity", "#ec4899"),
    ]

    y = 115
    for title, code, desc, col in stages:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill="#f8fafc")
        d.text((520, y + 12), code, font=get_font(15, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(14), fill="#94a3b8")
        y += 76

    img.save(OUTPUT_DIR / "post15-inline-regex-cleaning-pipeline.png")
    print("Created post15-inline-regex-cleaning-pipeline.png")

# Post 16: SRT vs VTT Subtitles
def make_infographic_16():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "SUBTITLE FORMATS: SUBRIP (.SRT) VS WEBVTT (.VTT)", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Comparing legacy broadcast formats with modern HTML5 web media standards", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 125, 465, 485), 16, "#1e293b", "#3b82f6", 2)
    d.text((75, 145), "SubRip Subtitles (.SRT)", font=get_font(18, True), fill="#60a5fa")
    d.text((75, 190), "• Header: None (starts with index '1')", font=get_font(15), fill="#f8fafc")
    d.text((75, 230), "• Timestamp Format: 00:01:23,456", font=get_font(15), fill="#cbd5e1")
    d.text((75, 270), "• Millisecond Delimiter: Comma (,)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 310), "• Styling Support: Basic HTML tags (<i>, <b>)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 350), "• Positioning: None (default bottom center)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 400), "Best For: YouTube, VLC, Premiere, Final Cut", font=get_font(15, True), fill="#93c5fd")

    draw_rounded_rect(d, (495, 125, 910, 485), 16, "#1e293b", "#10b981", 2)
    d.text((520, 145), "WebVTT (.VTT - W3C Standard)", font=get_font(18, True), fill="#34d399")
    d.text((520, 190), "• Header: Mandatory 'WEBVTT' line", font=get_font(15), fill="#f8fafc")
    d.text((520, 230), "• Timestamp Format: 00:01:23.456", font=get_font(15), fill="#cbd5e1")
    d.text((520, 270), "• Millisecond Delimiter: Period (.)", font=get_font(15), fill="#cbd5e1")
    d.text((520, 310), "• Styling Support: Full CSS ::cue pseudo-class", font=get_font(15), fill="#cbd5e1")
    d.text((520, 350), "• Positioning: line:0% position:50% align:left", font=get_font(15), fill="#cbd5e1")
    d.text((520, 400), "Best For: HTML5 <track>, Safari, Chrome, HLS", font=get_font(15, True), fill="#86efac")

    img.save(OUTPUT_DIR / "post16-inline-srt-vs-vtt.png")
    print("Created post16-inline-srt-vs-vtt.png")

# Post 17: YouTube Thumbnail Anatomy
def make_infographic_17():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "HIGH-CTR YOUTUBE THUMBNAIL BLUEPRINT", font=get_font(26, True), fill="#f43f5e")
    d.text((50, 72), "Structural elements that drive click-through rate across mobile & desktop feeds", font=get_font(17), fill="#94a3b8")

    points = [
        ("1. Resolution: 1280 x 720 (16:9)", "Maintains retina sharpness on smart TVs while staying under 2 MB limit", "#38bdf8"),
        ("2. Right-Bottom Safe Zone", "Leave bottom-right 20% clear of critical text (covered by duration timestamp)", "#f43f5e"),
        ("3. High Emotional Facial Contrast", "Expressive eyes & faces increase viewer engagement by up to 38%", "#34d399"),
        ("4. Maximum 3-4 Bold Words", "Must be instantly legible on small 320px mobile screens without squinting", "#fbbf24"),
        ("5. Complementary Color Contrast", "High contrast background separation prevents graphic from blending into feed", "#a855f7"),
    ]

    y = 115
    for title, desc, col in points:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(17, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78

    img.save(OUTPUT_DIR / "post17-inline-thumbnail-anatomy.png")
    print("Created post17-inline-thumbnail-anatomy.png")

# Post 18: ASCII & Binary Byte Representation
def make_infographic_18():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "8-BIT BINARY REGISTER & ASCII TRANSLATION", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "How 8 binary bits (base-2) combine to represent characters and memory states", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 115, 910, 235), 14, "#1e293b", "#38bdf8", 2)
    d.text((75, 130), "Character 'A' -> Decimal 65 -> Binary: 01000001", font=get_font(18, True), fill="#38bdf8")
    d.text((75, 165), "Bit Position Values:   [128] [64] [32] [16] [8]  [4]  [2]  [1]", font=get_font(16, True), fill="#cbd5e1")
    d.text((75, 195), "Bit Active (0/1):        0    1    0    0   0   0    0    1  = (64 + 1 = 65)", font=get_font(16, True), fill="#4ade80")

    draw_rounded_rect(d, (50, 255, 910, 375), 14, "#1e293b", "#a855f7", 2)
    d.text((75, 270), "Character 'B' -> Decimal 66 -> Binary: 01000010", font=get_font(18, True), fill="#c084fc")
    d.text((75, 305), "Bit Position Values:   [128] [64] [32] [16] [8]  [4]  [2]  [1]", font=get_font(16, True), fill="#cbd5e1")
    d.text((75, 335), "Bit Active (0/1):        0    1    0    0   0   0    1    0  = (64 + 2 = 66)", font=get_font(16, True), fill="#4ade80")

    draw_rounded_rect(d, (50, 395, 910, 485), 14, "#1e293b", "#10b981", 1)
    d.text((75, 415), "Rule: 1 Byte = 8 Bits = 256 Permutations (0 to 255)", font=get_font(17, True), fill="#34d399")
    d.text((75, 445), "UTF-8 dynamically chains 1 to 4 bytes to encode all 149,000+ international Unicode glyphs", font=get_font(15), fill="#cbd5e1")

    img.save(OUTPUT_DIR / "post18-inline-ascii-binary-table.png")
    print("Created post18-inline-ascii-binary-table.png")

# Post 19: Markup vs Margin
def make_infographic_19():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "PROFIT METRICS: MARKUP PERCENTAGE VS PROFIT MARGIN", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "The critical arithmetic difference between cost-based and revenue-based formulas", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 125, 465, 485), 16, "#1e293b", "#3b82f6", 2)
    d.text((75, 145), "MARKUP (Cost-Based)", font=get_font(18, True), fill="#60a5fa")
    d.text((75, 190), "Formula:", font=get_font(16, True), fill="#f8fafc")
    d.text((75, 220), "((Selling Price - Cost) / Cost) x 100", font=get_font(15, True), fill="#93c5fd")
    d.text((75, 270), "Example: Buy for $50, Sell for $100", font=get_font(16), fill="#cbd5e1")
    d.text((75, 305), "Profit: $50 / Cost $50 = 100% Markup", font=get_font(16, True), fill="#4ade80")
    d.text((75, 360), "Use: Setting retail price from manufacturer cost", font=get_font(14), fill="#94a3b8")

    draw_rounded_rect(d, (495, 125, 910, 485), 16, "#1e293b", "#10b981", 2)
    d.text((520, 145), "MARGIN (Revenue-Based)", font=get_font(18, True), fill="#34d399")
    d.text((520, 190), "Formula:", font=get_font(16, True), fill="#f8fafc")
    d.text((520, 220), "((Selling Price - Cost) / Revenue) x 100", font=get_font(15, True), fill="#86efac")
    d.text((520, 270), "Example: Buy for $50, Sell for $100", font=get_font(16), fill="#cbd5e1")
    d.text((520, 305), "Profit: $50 / Revenue $100 = 50% Margin", font=get_font(16, True), fill="#38bdf8")
    d.text((520, 360), "Use: Financial reporting & net income analysis", font=get_font(14), fill="#94a3b8")

    img.save(OUTPUT_DIR / "post19-inline-markup-vs-margin.png")
    print("Created post19-inline-markup-vs-margin.png")

# Post 20: Amortization Curve
def make_infographic_20():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "30-YEAR FIXED LOAN AMORTIZATION DYNAMICS", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "How monthly payments shift from interest-heavy to principal reduction over time", font=get_font(17), fill="#94a3b8")

    stages = [
        ("Years 1 – 5: Front-Loaded Interest", "75% Interest / 25% Principal", "Lenders collect financing charges upfront; minimal equity accumulation", "#ef4444"),
        ("Years 6 – 15: The Transition Period", "50% Interest / 50% Principal", "Monthly principal payment steadily overtakes interest deduction", "#f59e0b"),
        ("Years 16 – 25: Accelerated Equity", "25% Interest / 75% Principal", "Each payment rapidly reduces outstanding debt balance", "#3b82f6"),
        ("Years 26 – 30: Final Payoff Stage", "5% Interest / 95% Principal", "Virtually 100% of each dollar directly extinguishes the loan note", "#22c55e"),
    ]

    y = 120
    for period, ratio, desc, col in stages:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), period, font=get_font(17, True), fill=col)
        d.text((450, y + 14), ratio, font=get_font(16, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92

    img.save(OUTPUT_DIR / "post20-inline-amortization-curve.png")
    print("Created post20-inline-amortization-curve.png")

# Post 21: GST Inclusive vs Exclusive
def make_infographic_21():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "SALES TAX / GST: EXCLUSIVE VS INCLUSIVE FORMULAS", font=get_font(26, True), fill="#fbbf24")
    d.text((50, 72), "Accurate mathematical steps to add or strip value-added tax from invoices", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 125, 465, 485), 16, "#1e293b", "#3b82f6", 2)
    d.text((75, 145), "ADDING TAX (Tax Exclusive)", font=get_font(18, True), fill="#60a5fa")
    d.text((75, 190), "Formula:", font=get_font(16, True), fill="#f8fafc")
    d.text((75, 220), "Total = Net Price x (1 + Tax Rate / 100)", font=get_font(15, True), fill="#93c5fd")
    d.text((75, 270), "Example ($100 at 18% GST):", font=get_font(16), fill="#cbd5e1")
    d.text((75, 305), "$100 x 1.18 = $118.00 Total", font=get_font(16, True), fill="#4ade80")
    d.text((75, 360), "Use: B2B wholesale pricing, contractor hourly quotes", font=get_font(14), fill="#94a3b8")

    draw_rounded_rect(d, (495, 125, 910, 485), 16, "#1e293b", "#fbbf24", 2)
    d.text((520, 145), "REVERSING TAX (Tax Inclusive)", font=get_font(18, True), fill="#fbbf24")
    d.text((520, 190), "Formula:", font=get_font(16, True), fill="#f8fafc")
    d.text((520, 220), "Net = Gross / (1 + Tax Rate / 100)", font=get_font(15, True), fill="#fde68a")
    d.text((520, 270), "Example ($118 inclusive of 18% GST):", font=get_font(16), fill="#cbd5e1")
    d.text((520, 305), "$118 / 1.18 = $100 Net ($18 GST)", font=get_font(16, True), fill="#38bdf8")
    d.text((520, 360), "Use: B2C retail checkout, accounting tax reconciliation", font=get_font(14), fill="#94a3b8")

    img.save(OUTPUT_DIR / "post21-inline-tax-calculation-flow.png")
    print("Created post21-inline-tax-calculation-flow.png")

# Post 22: Metric vs Imperial Factors
def make_infographic_22():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "EXACT METRIC TO IMPERIAL CONVERSION MULTIPLIERS", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "International standard conversion constants defined by treaty and BIPM standards", font=get_font(17), fill="#94a3b8")

    factors = [
        ("Length: 1 Inch", "= Exactly 25.4 Millimeters", "Defined by 1959 International Yard and Pound Agreement", "#38bdf8"),
        ("Length: 1 Meter", "= 3.28084 Feet (39.3701 Inches)", "Standard SI base unit for international engineering and science", "#34d399"),
        ("Mass: 1 Kilogram", "= 2.20462 Pounds (Avoirdupois)", "Based on Planck constant (6.62607015 x 10^-34 kg*m^2*s^-1)", "#fbbf24"),
        ("Volume: 1 US Gallon", "= 3.78541 Liters (231 cu inches)", "Distinct from UK Imperial gallon (which equals 4.54609 Liters)", "#ec4899"),
        ("Temperature: Celsius to Fahr", "F = (C x 9/5) + 32", "Water freezes at 0 C / 32 F and boils at 100 C / 212 F", "#a855f7"),
    ]

    y = 115
    for unit, factor, note, col in factors:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), unit, font=get_font(16, True), fill=col)
        d.text((320, y + 12), factor, font=get_font(16, True), fill="#f8fafc")
        d.text((75, y + 38), note, font=get_font(14), fill="#94a3b8")
        y += 78

    img.save(OUTPUT_DIR / "post22-inline-metric-imperial-factors.png")
    print("Created post22-inline-metric-imperial-factors.png")

# Post 23: Number to Words & Roman Numerals
def make_infographic_23():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "ROMAN NUMERAL SYSTEM RULES & ARITHMETIC LOGIC", font=get_font(26, True), fill="#f59e0b")
    d.text((50, 72), "Subtractive notation rules, additive values, and legal check drafting formatting", font=get_font(17), fill="#94a3b8")

    rules = [
        ("Primary Symbols", "I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000", "#38bdf8"),
        ("Additive Rule", "Symbols written left-to-right in descending value add together (XVI = 10+5+1 = 16)", "#34d399"),
        ("Subtractive Rule", "A smaller numeral placed before a larger subtracts (IV = 4, IX = 9, XL = 40, XC = 90)", "#fbbf24"),
        ("Repetition Limit", "Never repeat a symbol more than 3 consecutive times (Use IV for 4, never IIII)", "#f43f5e"),
        ("Banking Word Formatting", "'One Thousand Two Hundred Fifty and 00/100 Dollars' prevents check tampering", "#a855f7"),
    ]

    y = 115
    for title, desc, col in rules:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78

    img.save(OUTPUT_DIR / "post23-inline-numeral-rules.png")
    print("Created post23-inline-numeral-rules.png")

# Post 24: Data Serialization Matrix
def make_infographic_24():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "DATA SERIALIZATION: CSV VS XML VS JSON", font=get_font(26, True), fill="#60a5fa")
    d.text((50, 72), "Benchmarking data interchange structures across storage, parsing speed and hierarchy", font=get_font(17), fill="#94a3b8")

    formats = [
        ("CSV (Tabular / Flat)", "Compact & Spreadsheet-Native", "Extremely fast streaming; cannot represent nested objects or arrays", "#38bdf8"),
        ("JSON (RFC 8259)", "Modern Web Standard", "Lightweight tree structure; native parsing in all modern programming languages", "#34d399"),
        ("XML (W3C Markup)", "Heavy & Strictly Schematized", "Supports XSD schemas & namespaces; significant verbosity overhead", "#f43f5e"),
        ("Parquet / Arrow", "Columnar Analytical Storage", "Optimized for BigQuery & Pandas; 80% smaller than raw CSV with Snappy", "#a855f7"),
    ]

    y = 120
    for name, trait, desc, col in formats:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), name, font=get_font(17, True), fill=col)
        d.text((450, y + 14), trait, font=get_font(16, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92

    img.save(OUTPUT_DIR / "post24-inline-data-serialization-matrix.png")
    print("Created post24-inline-data-serialization-matrix.png")

# Post 25: Website Legal Compliance
def make_infographic_25():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "MANDATORY WEBSITE LEGAL COMPLIANCE PILLARS", font=get_font(26, True), fill="#a855f7")
    d.text((50, 72), "Essential regulatory disclosures required for Google AdSense and global privacy laws", font=get_font(17), fill="#94a3b8")

    pillars = [
        ("1. Privacy Policy (GDPR / CCPA / COPPA)", "Must disclose cookie tracking, 3rd party ad networks & user data retention", "#38bdf8"),
        ("2. Terms of Service (ToS)", "Governs acceptable usage, limitation of liability, intellectual property & arbitration", "#34d399"),
        ("3. Cookie Consent Banner", "Requires explicit opt-in for analytical and marketing trackers in EU/UK jurisdictions", "#fbbf24"),
        ("4. Disclaimer & DMCA Notice", "Shields site owners from financial liability regarding informational tool results", "#f43f5e"),
        ("5. Verified Contact & Impressum", "Provides real corporate email/address to satisfy consumer protection mandates", "#a855f7"),
    ]

    y = 115
    for title, desc, col in pillars:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78

    img.save(OUTPUT_DIR / "post25-inline-legal-requirements.png")
    print("Created post25-inline-legal-requirements.png")

# Post 26: UUID v4 Architecture
def make_infographic_26():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "UUID VERSION 4 (128-BIT) ANATOMY & STRUCTURE", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Cryptographically generated identifiers: 5.3 x 10^36 unique addresses", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 115, 910, 220), 14, "#1e293b", "#38bdf8", 2)
    d.text((75, 130), "Standard Format: 8 - 4 - 4 - 4 - 12 Hexadecimal Digits (36 chars total)", font=get_font(17, True), fill="#38bdf8")
    d.text((75, 165), "Example: f47ac10b - 58cc - 4372 - a567 - 0e02b2c3d479", font=get_font(19, True), fill="#4ade80")

    draw_rounded_rect(d, (50, 240, 465, 485), 14, "#1e293b", "#fbbf24", 2)
    d.text((75, 260), "UUID v4 Benefits", font=get_font(18, True), fill="#fbbf24")
    d.text((75, 300), "• Globally Unique (No central DB coordinator)", font=get_font(15), fill="#f8fafc")
    d.text((75, 340), "• Secure against ID enumeration attacks", font=get_font(15), fill="#cbd5e1")
    d.text((75, 380), "• Client-side generation in offline mobile apps", font=get_font(15), fill="#cbd5e1")
    d.text((75, 420), "• Frictionless distributed database sharding", font=get_font(15), fill="#cbd5e1")

    draw_rounded_rect(d, (495, 240, 910, 485), 14, "#1e293b", "#f43f5e", 2)
    d.text((520, 260), "Sequential Int vs UUID Tradeoff", font=get_font(18, True), fill="#f87171")
    d.text((520, 300), "• Auto-Increment Int: 4-8 bytes (Fast B-Tree index)", font=get_font(15), fill="#f8fafc")
    d.text((520, 340), "• Sequential Risk: Leaks order counts to rivals", font=get_font(15), fill="#cbd5e1")
    d.text((520, 380), "• UUID v4: 16 raw bytes (Random index page splits)", font=get_font(15), fill="#cbd5e1")
    d.text((520, 420), "• Modern Fix: UUID v7 (Time-ordered 128-bit keys)", font=get_font(15, True), fill="#86efac")

    img.save(OUTPUT_DIR / "post26-inline-uuid-architecture.png")
    print("Created post26-inline-uuid-architecture.png")

# Post 27: UTM Hierarchy
def make_infographic_27():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "GA4 UTM CAMPAIGN PARAMETER TAXONOMY", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "Standardizing marketing attribution tracking to prevent split analytics data", font=get_font(17), fill="#94a3b8")

    params = [
        ("utm_source (Mandatory)", "google / newsletter / facebook", "Identifies the platform or site sending the traffic", "#38bdf8"),
        ("utm_medium (Mandatory)", "cpc / email / organic_social / banner", "Identifies the high-level marketing channel category", "#34d399"),
        ("utm_campaign (Mandatory)", "spring_sale / product_launch_2026", "Identifies the specific promotional campaign or objective", "#fbbf24"),
        ("utm_content (Optional)", "cta_top_button vs text_link_footer", "A/B testing variant: identifies which specific link was clicked", "#a855f7"),
        ("utm_term (Optional)", "best_seo_tools / json_formatter", "Identifies paid search keywords or audience segment tags", "#ec4899"),
    ]

    y = 115
    for tag, example, desc, col in params:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), tag, font=get_font(16, True), fill=col)
        d.text((360, y + 12), example, font=get_font(15, True), fill="#f8fafc")
        d.text((75, y + 38), desc, font=get_font(14), fill="#cbd5e1")
        y += 78

    img.save(OUTPUT_DIR / "post27-inline-utm-hierarchy.png")
    print("Created post27-inline-utm-hierarchy.png")

# Post 28: Aspect Ratio Standards
def make_infographic_28():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "STANDARD WEB & SOCIAL ASPECT RATIO MATRIX", font=get_font(26, True), fill="#ec4899")
    d.text((50, 72), "Key dimensions and resolution targets for responsive multi-platform delivery", font=get_font(17), fill="#94a3b8")

    ratios = [
        ("16:9 Landscape (1920x1080 / 1280x720)", "Desktop Hero, YouTube, Open Graph", "Universal widescreen format across monitors, laptops, and TV screens", "#38bdf8"),
        ("1:1 Square (1080x1080 / 600x600)", "Instagram Feed, Product Catalog, Avatars", "Optimal for e-commerce thumbnail grids and balanced square layouts", "#34d399"),
        ("4:3 Standard (1200x900 / 800x600)", "Tablet Displays, Classical Photography", "Compact horizontal framing frequently used in digital publication cards", "#fbbf24"),
        ("9:16 Vertical (1080x1920)", "TikTok, Instagram Reels, YouTube Shorts", "Full-bleed mobile screen immersion optimized for single-hand scrolling", "#a855f7"),
    ]

    y = 120
    for title, use, desc, col in ratios:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), title, font=get_font(17, True), fill=col)
        d.text((520, y + 14), use, font=get_font(15, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92

    img.save(OUTPUT_DIR / "post28-inline-aspect-ratio-standards.png")
    print("Created post28-inline-aspect-ratio-standards.png")

# Post 29: Favicon Multi-Resolution Standards
def make_infographic_29():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "COMPLETE MULTI-DEVICE FAVICON & APP ICON SUITE", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Required asset sizes to cover desktop browser tabs, iOS home screens & Android PWAs", font=get_font(17), fill="#94a3b8")

    icons = [
        ("favicon.ico (Multi-Layer 16x16 & 32x32)", "Legacy Desktop Browser Tabs", "Backward-compatible container loaded automatically by all desktop browsers", "#38bdf8"),
        ("favicon.svg (Vector SVG)", "Modern Crisp Retina Tabs", "Scales infinitely with dark-mode prefers-color-scheme media query support", "#34d399"),
        ("apple-touch-icon.png (180x180)", "iOS Safari Home Screen Bookmarks", "Crisp high-DPI icon when users save web apps to iPhone & iPad home screens", "#fbbf24"),
        ("android-chrome-192x192.png", "Android PWA Splash & Launcher", "Standard web app launcher icon defined in webmanifest JSON specification", "#a855f7"),
        ("android-chrome-512x512.png", "High-Resolution PWA App Store", "Maximum resolution asset for Progressive Web App installations", "#ec4899"),
    ]

    y = 115
    for title, role, desc, col in icons:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((520, y + 12), role, font=get_font(15, True), fill="#f8fafc")
        d.text((75, y + 38), desc, font=get_font(14), fill="#cbd5e1")
        y += 78

    img.save(OUTPUT_DIR / "post29-inline-favicon-matrix.png")
    print("Created post29-inline-favicon-matrix.png")

# Post 30: TDEE Energy Breakdown
def make_infographic_30():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "TOTAL DAILY ENERGY EXPENDITURE (TDEE) PILLARS", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "The 4 biological components that dictate daily calorie burn and metabolic rate", font=get_font(17), fill="#94a3b8")

    components = [
        ("1. Basal Metabolic Rate (BMR): ~60% - 70%", "Base energy burned at total rest to keep organs, brain and lungs functioning", "#38bdf8"),
        ("2. Non-Exercise Activity Thermogenesis (NEAT): ~15%", "Spontaneous movement: walking, typing, fidgeting, posture maintenance", "#34d399"),
        ("3. Thermic Effect of Food (TEF): ~10%", "Metabolic energy required to digest, absorb and assimilate dietary macronutrients", "#fbbf24"),
        ("4. Exercise Activity (EAT): ~5% - 10%", "Structured athletic workouts, resistance training, running, and cycling", "#ec4899"),
    ]

    y = 120
    for name, desc, col in components:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), name, font=get_font(17, True), fill=col)
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92

    img.save(OUTPUT_DIR / "post30-inline-tdee-energy-expenditure.png")
    print("Created post30-inline-tdee-energy-expenditure.png")

if __name__ == "__main__":
    make_infographic_11()
    make_infographic_12()
    make_infographic_13()
    make_infographic_14()
    make_infographic_15()
    make_infographic_16()
    make_infographic_17()
    make_infographic_18()
    make_infographic_19()
    make_infographic_20()
    make_infographic_21()
    make_infographic_22()
    make_infographic_23()
    make_infographic_24()
    make_infographic_25()
    make_infographic_26()
    make_infographic_27()
    make_infographic_28()
    make_infographic_29()
    make_infographic_30()
    print("ALL 20 NEW INLINE INFOGRAPHICS (POSTS 11-30) CREATED SUCCESSFULLY!")
