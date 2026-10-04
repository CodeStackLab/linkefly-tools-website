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

# 11b: Security & Double Encoding
def make_11b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "URL ENCODING SECURITY & ATTACK VECTORS", font=get_font(26, True), fill="#f43f5e")
    d.text((50, 72), "Defending against double-encoding, directory traversal and open redirects", font=get_font(17), fill="#94a3b8")

    risks = [
        ("Directory Traversal", "%2E%2E%2F (../) bypasses basic string filters if decoded multiple times", "#ef4444"),
        ("Double Percent-Encoding", "%2520 -> WAF sees %25 -> App decodes %20 -> Yields forbidden space", "#f59e0b"),
        ("Open Redirect Injection", "%2F%2Fevil.com in return_url redirects users to phishing destinations", "#ec4899"),
        ("Query Parameter Pollution", "foo=1&foo=2 behaves inconsistently across Express, Django, and PHP", "#a855f7"),
        ("Safe Engineering Standard", "Decode exactly ONCE at the application perimeter; validate whitelist after", "#22c55e"),
    ]

    y = 115
    for title, desc, col in risks:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post11-inline-security-encoding-attacks.png")
    print("Created post11-inline-security-encoding-attacks.png")

# 12b: Typography Metrics
def make_12b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "EDITORIAL TYPOGRAPHY READABILITY BENCHMARKS", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Rules of thumb for fluid typography, optimal measure, and vertical rhythm", font=get_font(17), fill="#94a3b8")

    metrics = [
        ("Optimal Measure: 50 – 75 Chars", "max-width: 65ch prevents eye fatigue when scanning long text columns", "#38bdf8"),
        ("Body Line Height: 1.5 – 1.65", "line-height: 1.6 gives text breathing room without disconnecting paragraphs", "#34d399"),
        ("Base Font Size: 16px – 18px", "Ensures effortless legibility across desktop, tablet, and mobile displays", "#fbbf24"),
        ("Paragraph Spacing: 1em – 1.25em", "Clear vertical rhythm between thoughts without requiring indentation", "#a855f7"),
        ("Hierarchy Ratio: 1.25 Major Third", "H1 (2.44rem) -> H2 (1.95rem) -> H3 (1.56rem) -> Body (1rem)", "#22c55e"),
    ]

    y = 115
    for title, desc, col in metrics:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post12-inline-typesetting-readability.png")
    print("Created post12-inline-typesetting-readability.png")

# 13b: IPv6 Subnetting
def make_13b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "IPv6 GLOBAL UNICAST ADDRESS ARCHITECTURE (/64)", font=get_font(26, True), fill="#818cf8")
    d.text((50, 72), "Standard hierarchy dividing routing prefixes, subnets, and host interface IDs", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 120, 910, 240), 14, "#1e293b", "#818cf8", 2)
    d.text((75, 140), "Global Routing Prefix (48 bits) + Subnet ID (16 bits) = /64 Network", font=get_font(17, True), fill="#818cf8")
    d.text((75, 175), "Interface ID (64 bits): Generates 18.4 Quintillion host addresses per single subnet", font=get_font(15), fill="#cbd5e1")
    d.text((75, 205), "Example: 2001:0db8:85a3:0000 : 0000:8a2e:0370:7334", font=get_font(16, True), fill="#4ade80")

    draw_rounded_rect(d, (50, 260, 910, 485), 14, "#1e293b", "#38bdf8", 1)
    d.text((75, 280), "IPv6 Addressing Innovations", font=get_font(17, True), fill="#38bdf8")
    d.text((75, 315), "• SLAAC (Stateless Address Autoconfiguration): Clients configure IPs without DHCP", font=get_font(15), fill="#f8fafc")
    d.text((75, 350), "• Dual-Stack Deployment: Coexistence running IPv4 and IPv6 side-by-side", font=get_font(15), fill="#cbd5e1")
    d.text((75, 385), "• Elimination of Broadcast: Replaced with targeted Multicast traffic", font=get_font(15), fill="#cbd5e1")
    d.text((75, 420), "• Native IPsec Security: Built-in end-to-end cryptographic packet headers", font=get_font(15), fill="#86efac")

    img.save(OUTPUT_DIR / "post13-inline-ipv6-subnetting.png")
    print("Created post13-inline-ipv6-subnetting.png")

# 14b: WCAG Contrast
def make_14b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "WCAG 2.1 COLOR CONTRAST RATIO THRESHOLDS", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "Essential accessibility guidelines for digital legibility and compliance", font=get_font(17), fill="#94a3b8")

    levels = [
        ("Level AA: Normal Body Text", "Minimum 4.5:1 Contrast", "Required for all standard body copy under 18pt (or bold 14pt)", "#22c55e"),
        ("Level AA: Large Headlines & UI", "Minimum 3.0:1 Contrast", "Permitted for headings >= 18pt, bold >= 14pt, and UI borders/icons", "#38bdf8"),
        ("Level AAA: Enhanced Accessibility", "Minimum 7.0:1 Contrast", "Gold standard ensuring legibility for users with low-vision impairments", "#a855f7"),
        ("Failing Ratios (< 3.0:1)", "Unacceptable & Inaccessible", "Causes severe eye strain and fails automated Lighthouse audits", "#ef4444"),
    ]

    y = 120
    for title, rule, desc, col in levels:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), title, font=get_font(17, True), fill=col)
        d.text((500, y + 14), rule, font=get_font(16, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92
    img.save(OUTPUT_DIR / "post14-inline-wcag-contrast-ratios.png")
    print("Created post14-inline-wcag-contrast-ratios.png")

# 15b: CSV Escaping Rules
def make_15b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "RFC 4180 CSV DELIMITER ESCAPING SPECIFICATIONS", font=get_font(26, True), fill="#fbbf24")
    d.text((50, 72), "Rules for formatting data containing commas, quotes, and line breaks", font=get_font(17), fill="#94a3b8")

    rules = [
        ("Rule 1: Field Contains Comma", "Field: Austin, TX  ->  CSV Output: \"Austin, TX\"", "#38bdf8"),
        ("Rule 2: Field Contains Quotes", "Field: 15\" Screen  ->  CSV Output: \"15\"\" Screen\"", "#34d399"),
        ("Rule 3: Field Contains Line Feed", "Field: Line1\\nLine2  ->  CSV Output: \"Line1\\nLine2\"", "#fbbf24"),
        ("Rule 4: Standard Delimiter", "Commas (,) separate fields; CRLF (\\r\\n) terminates records", "#a855f7"),
        ("Rule 5: Null vs Empty String", "Empty field is two adjacent commas (,,) without whitespace", "#22c55e"),
    ]

    y = 115
    for title, desc, col in rules:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post15-inline-csv-escape-rules.png")
    print("Created post15-inline-csv-escape-rules.png")

# 16b: WebVTT Cue Styling
def make_16b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "WEBVTT CSS PSEUDO-ELEMENT (::cue) STYLING", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "How modern web players customize typography, contrast, and positioning", font=get_font(17), fill="#94a3b8")

    props = [
        ("video::cue { color: #ffffff; }", "Overrides default subtitle font color for optimal readability", "#38bdf8"),
        ("video::cue { background: rgba(0,0,0,0.8); }", "Adds semi-transparent letterbox plate to ensure high contrast", "#34d399"),
        ("video::cue { font-size: 1.25rem; }", "Responsive font scaling across smartphone and desktop viewports", "#fbbf24"),
        ("video::cue(b) { color: #fbbf24; }", "Targeted styling for speaker highlights or key emphasis cues", "#a855f7"),
        ("video::cue { text-shadow: 0 2px 4px #000; }", "Guarantees crisp legibility against blinding white video scenes", "#22c55e"),
    ]

    y = 115
    for code, desc, col in props:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), code, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post16-inline-webvtt-cue-styling.png")
    print("Created post16-inline-webvtt-cue-styling.png")

# 17b: Mobile Thumbnail Psychology
def make_17b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "MOBILE FEED PSYCHOLOGY & THE 3-SECOND GLANCE TEST", font=get_font(26, True), fill="#f43f5e")
    d.text((50, 72), "Optimizing viewer retention in rapid touch-scrolling YouTube environments", font=get_font(17), fill="#94a3b8")

    rules = [
        ("1. The 1.5-Inch Screen Reality", "Viewers decide to tap or scroll in under 1.8 seconds on 390px screens", "#ef4444"),
        ("2. Rule of Thirds Placement", "Place high-contrast focal points at grid intersections to guide gaze", "#38bdf8"),
        ("3. Avoid Title Repetition", "Thumbnail text should complement the title, not mechanically duplicate it", "#34d399"),
        ("4. Saturated Background Isolation", "High background/foreground edge contrast prevents visual blending", "#fbbf24"),
        ("5. Dark Mode Compatibility", "Test against both white (#fff) and YouTube Dark Theme (#0f0f0f)", "#a855f7"),
    ]

    y = 115
    for title, desc, col in rules:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post17-inline-mobile-thumbnail-ux.png")
    print("Created post17-inline-mobile-thumbnail-ux.png")

# 18b: Bitwise Operations
def make_18b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "CORE BITWISE OPERATORS & LOGICAL GATES", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Low-level digital arithmetic for high-speed bit flags, cryptography & graphics", font=get_font(17), fill="#94a3b8")

    ops = [
        ("AND (&)", "1 & 1 = 1 (all others 0)", "Bit masking: checks if a specific permission flag bit is set", "#38bdf8"),
        ("OR (|)", "0 | 0 = 0 (all others 1)", "Flag setting: activates a permission or configuration bit", "#34d399"),
        ("XOR (^)", "Different bits = 1, Same = 0", "Cryptography: reversible symmetric encryption cipher primitive", "#fbbf24"),
        ("NOT (~)", "Inverts all bits (0 -> 1, 1 -> 0)", "One's complement bit inversion", "#f43f5e"),
        ("Bit Shift (<< / >>)", "Multiplies or divides by 2^n", "Ultra-fast arithmetic: 5 << 1 = 10 (multiplication by 2)", "#a855f7"),
    ]

    y = 115
    for op, logic, desc, col in ops:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), op, font=get_font(16, True), fill=col)
        d.text((250, y + 12), logic, font=get_font(15, True), fill="#f8fafc")
        d.text((75, y + 38), desc, font=get_font(14), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post18-inline-bitwise-operations.png")
    print("Created post18-inline-bitwise-operations.png")

# 19b: Break-Even Pricing Formula
def make_19b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "BREAK-EVEN UNIT ECONOMICS & PRICING FORMULA", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "Calculating the minimum sales volume required to cover fixed overhead", font=get_font(17), fill="#94a3b8")

    draw_rounded_rect(d, (50, 120, 910, 240), 14, "#1e293b", "#10b981", 2)
    d.text((75, 140), "Break-Even Units = Total Fixed Costs / (Price per Unit - Variable Cost)", font=get_font(18, True), fill="#34d399")
    d.text((75, 175), "Contribution Margin = Price per Unit - Variable Cost (Revenue left to cover overhead)", font=get_font(15), fill="#cbd5e1")
    d.text((75, 205), "Example: $10,000 Overhead / ($100 Price - $40 Cost) = 167 Units to Break Even", font=get_font(16, True), fill="#4ade80")

    draw_rounded_rect(d, (50, 260, 910, 485), 14, "#1e293b", "#38bdf8", 1)
    d.text((75, 280), "Pricing Strategy Rules", font=get_font(17, True), fill="#38bdf8")
    d.text((75, 315), "• Higher Margins = Lower Unit Burden: 70% margins need 60% fewer unit sales", font=get_font(15), fill="#f8fafc")
    d.text((75, 350), "• Price Elasticity: A 10% price increase often boosts net profit by 25%+", font=get_font(15), fill="#cbd5e1")
    d.text((75, 385), "• Factoring Hidden Costs: Always incorporate payment gateway fees & refunds", font=get_font(15), fill="#cbd5e1")
    d.text((75, 420), "• Cash Flow Runway: Track days sales outstanding (DSO) to protect liquidity", font=get_font(15), fill="#86efac")

    img.save(OUTPUT_DIR / "post19-inline-breakeven-pricing-formula.png")
    print("Created post19-inline-breakeven-pricing-formula.png")

# 20b: Extra Principal Savings
def make_20b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "THE COMPOUND EFFECT OF EXTRA PRINCIPAL REPAYMENTS", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "How small additional monthly payments slash loan duration and interest expense", font=get_font(17), fill="#94a3b8")

    scenarios = [
        ("Base 30-Yr Mortgage ($300k @ 6.5%)", "Total Interest: $382,633  |  Term: 360 Months", "Standard minimum monthly payment of $1,896", "#ef4444"),
        ("+$100 / Month Principal", "Interest Saved: $37,840  |  Term: 322 Months (-3.2 Yrs)", "Saves over $37k with minor monthly lifestyle budget adjustment", "#fbbf24"),
        ("+$250 / Month Principal", "Interest Saved: $78,190  |  Term: 280 Months (-6.7 Yrs)", "Cuts almost 7 full years off mortgage debt", "#3b82f6"),
        ("Bi-Weekly Payment Schedule", "Interest Saved: $49,200  |  Term: 312 Months (-4.0 Yrs)", "Yields 13 full payments per year seamlessly", "#22c55e"),
    ]

    y = 120
    for title, stats, desc, col in scenarios:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), title, font=get_font(17, True), fill=col)
        d.text((450, y + 14), stats, font=get_font(15, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92
    img.save(OUTPUT_DIR / "post20-inline-extra-principal-savings.png")
    print("Created post20-inline-extra-principal-savings.png")

# 21b: Input Tax Credit
def make_21b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "INPUT TAX CREDIT (ITC) VALUE-ADDED TAX SUPPLY CHAIN", font=get_font(26, True), fill="#fbbf24")
    d.text((50, 72), "How GST avoids cascading tax-on-tax by netting input tax against output tax", font=get_font(17), fill="#94a3b8")

    steps = [
        ("Stage 1: Manufacturer", "Cost $100 + 18% GST ($18) = $118", "Manufacturer remits $18 tax directly to government", "#38bdf8"),
        ("Stage 2: Wholesaler Adds $50 Value", "Sells at $150 + 18% GST ($27) = $177", "Claims $18 Input Credit; pays government net difference ($9)", "#34d399"),
        ("Stage 3: Retailer Adds $50 Value", "Sells at $200 + 18% GST ($36) = $236", "Claims $27 Input Credit; pays government net difference ($9)", "#fbbf24"),
        ("Final Consumer Purchase", "Pays $236 (Goods $200 + Tax $36)", "Total tax collected by treasury: $18 + $9 + $9 = Exactly $36 (18%)", "#22c55e"),
    ]

    y = 120
    for stage, pricing, desc, col in steps:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), stage, font=get_font(17, True), fill=col)
        d.text((450, y + 14), pricing, font=get_font(15, True), fill="#f8fafc")
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92
    img.save(OUTPUT_DIR / "post21-inline-input-tax-credit.png")
    print("Created post21-inline-input-tax-credit.png")

# 22b: SI Unit Prefixes
def make_22b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "INTERNATIONAL SYSTEM (SI) DECIMAL METRIC PREFIXES", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Exponential scaling factors from microscopic nanometers to terabytes", font=get_font(17), fill="#94a3b8")

    prefixes = [
        ("Tera- (T) : 10^12", "1,000,000,000,000 (Trillion)", "High-capacity server NVMe storage & data centers", "#a855f7"),
        ("Giga- (G) : 10^9", "1,000,000,000 (Billion)", "Processor clock frequencies (GHz) & RAM capacity", "#38bdf8"),
        ("Mega- (M) : 10^6", "1,000,000 (Million)", "Network bandwidth (Mbps) & image megapixel resolutions", "#34d399"),
        ("Kilo- (k) : 10^3", "1,000 (Thousand)", "Distance (kilometer), mass (kilogram), electric power (kW)", "#fbbf24"),
        ("Milli- (m) : 10^-3", "0.001 (Thousandth)", "Millimeter precision measurements & fluid dosages", "#ec4899"),
    ]

    y = 115
    for tag, val, desc, col in prefixes:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), tag, font=get_font(16, True), fill=col)
        d.text((320, y + 12), val, font=get_font(15, True), fill="#f8fafc")
        d.text((75, y + 38), desc, font=get_font(14), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post22-inline-si-unit-prefixes.png")
    print("Created post22-inline-si-unit-prefixes.png")

# 23b: Financial Check Writing Rules
def make_23b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "LEGAL BANKING INSTRUMENT & CHECK DRAFTING RULES", font=get_font(26, True), fill="#f59e0b")
    d.text((50, 72), "Why written words legally supersede numerical figures under Uniform Commercial Code", font=get_font(17), fill="#94a3b8")

    rules = [
        ("UCC Section 3-114 Precedence", "If numerical box ($100.00) conflicts with written line, written words govern", "#38bdf8"),
        ("No Open Margin Space", "Begin words flush to the left boundary; draw trailing line to prevent tampering", "#34d399"),
        ("Fractional Cents Formatting", "Always write cents as 'XX/100' (e.g., 'Fifty Cents and 25/100 Dollars')", "#fbbf24"),
        ("Post-Dating Enforceability", "Banks may process post-dated checks immediately unless written notice is given", "#f43f5e"),
        ("Roman Numerals in Law", "Super Bowl, copyright stamps (MCMLXXXIV), and monarchial statutes", "#a855f7"),
    ]

    y = 115
    for title, desc, col in rules:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post23-inline-financial-check-writing.png")
    print("Created post23-inline-financial-check-writing.png")

# 24b: JSON Schema Validation
def make_24b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "ENTERPRISE JSON SCHEMA STRUCTURAL VALIDATION", font=get_font(26, True), fill="#60a5fa")
    d.text((50, 72), "Enforcing contract integrity and strict type safety across microservice APIs", font=get_font(17), fill="#94a3b8")

    props = [
        ("type: 'object'", "Defines the root container data structure", "#38bdf8"),
        ("required: ['id', 'email']", "Guarantees mission-critical fields cannot be omitted or null", "#34d399"),
        ("properties: { email: { format: 'email' } }", "Enforces RFC 5322 regex validation on input strings", "#fbbf24"),
        ("additionalProperties: false", "Blocks malicious payload injection & unexpected schema contamination", "#f43f5e"),
        ("minimum: 0, maximum: 100", "Enforces strict arithmetic bounding limits on numerical inputs", "#a855f7"),
    ]

    y = 115
    for tag, desc, col in props:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), tag, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post24-inline-json-schema-validation.png")
    print("Created post24-inline-json-schema-validation.png")

# 25b: Cookie Categories
def make_25b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "FOUR MANDATORY COOKIE CONSENT CLASSIFICATIONS", font=get_font(26, True), fill="#a855f7")
    d.text((50, 72), "GDPR and ePrivacy Directive requirements for web trackers and local storage", font=get_font(17), fill="#94a3b8")

    cats = [
        ("Strictly Necessary (Exempt)", "Session tokens, CSRF protection, shopping cart IDs (cannot be disabled)", "#22c55e"),
        ("Performance & Analytics", "Google Analytics 4, Hotjar (measures page load speed and user journeys)", "#38bdf8"),
        ("Functional & Preferences", "Dark/light mode toggle, UI language selection, font size preferences", "#fbbf24"),
        ("Targeting & Marketing", "Google AdSense, Meta Pixel (tracks cross-site browsing for personalized ads)", "#ef4444"),
    ]

    y = 120
    for title, desc, col in cats:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), title, font=get_font(17, True), fill=col)
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92
    img.save(OUTPUT_DIR / "post25-inline-cookie-consent-categories.png")
    print("Created post25-inline-cookie-consent-categories.png")

# 26b: UUID Versions Matrix
def make_26b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "UUID EVOLUTION: VERSION 1 THROUGH VERSION 7", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "Comparing entropy generation methods across RFC 4122 and RFC 9562 specs", font=get_font(17), fill="#94a3b8")

    versions = [
        ("UUID v1 (Timestamp + MAC)", "Time-based; leaks hardware MAC address and creation order", "#ef4444"),
        ("UUID v3 & v5 (Name-Based)", "Deterministic MD5 (v3) or SHA-1 (v5) hash of namespace + name", "#fbbf24"),
        ("UUID v4 (Random Entropy)", "122 bits of pseudo-random entropy; industry standard for general use", "#38bdf8"),
        ("UUID v7 (Time-Ordered Unix)", "Millisecond Unix epoch timestamp prefix + 74 random bits (DB-optimized)", "#22c55e"),
    ]

    y = 120
    for v, desc, col in versions:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), v, font=get_font(17, True), fill=col)
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92
    img.save(OUTPUT_DIR / "post26-inline-uuid-versions-matrix.png")
    print("Created post26-inline-uuid-versions-matrix.png")

# 27b: GA4 Attribution Models
def make_27b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "GOOGLE ANALYTICS 4 (GA4) ATTRIBUTION MODELS", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "Evaluating how marketing channels receive credit for multi-touch conversions", font=get_font(17), fill="#94a3b8")

    models = [
        ("Data-Driven Attribution (Default)", "Uses machine learning to distribute credit based on actual user lift", "#22c55e"),
        ("Last Click Attribution", "Gives 100% of conversion value to the very last link clicked before purchase", "#38bdf8"),
        ("First Click Attribution", "Gives 100% of credit to the original introductory discovery campaign", "#fbbf24"),
        ("Linear Attribution (Sunset in GA4)", "Split credit equally across all touchpoints (retired by Google in 2023)", "#94a3b8"),
    ]

    y = 120
    for name, desc, col in models:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), name, font=get_font(17, True), fill=col)
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92
    img.save(OUTPUT_DIR / "post27-inline-ga4-attribution-models.png")
    print("Created post27-inline-ga4-attribution-models.png")

# 28b: Responsive Picture & Srcset
def make_28b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "HTML5 RESPONSIVE IMAGING (<picture> & srcset)", font=get_font(26, True), fill="#ec4899")
    d.text((50, 72), "Serving device-tailored resolutions to cut mobile data usage and boost LCP", font=get_font(17), fill="#94a3b8")

    specs = [
        ("<source srcset='hero.avif' type='image/avif'>", "Delivers ultra-compact AVIF format to cutting-edge browsers", "#38bdf8"),
        ("<source srcset='hero.webp' type='image/webp'>", "Fallback modern standard supported by 97%+ of global web users", "#34d399"),
        ("<img src='hero.jpg' loading='lazy'>", "Graceful legacy fallback with native lazy-loading enabled", "#fbbf24"),
        ("sizes='(max-width: 768px) 100vw, 1200px'", "Instructs browser which image size to allocate before DOM parses", "#a855f7"),
        ("fetchpriority='high' on Hero Image", "Bypasses download queue delays to optimize Largest Contentful Paint (LCP)", "#22c55e"),
    ]

    y = 115
    for code, desc, col in specs:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), code, font=get_font(15, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(14), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post28-inline-responsive-picture-srcset.png")
    print("Created post28-inline-responsive-picture-srcset.png")

# 29b: Browser Tab Rendering
def make_29b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "MODERN BROWSER TAB FAVICON BEHAVIOR", font=get_font(26, True), fill="#38bdf8")
    d.text((50, 72), "How Chrome, Safari, and Firefox select and render brand icons", font=get_font(17), fill="#94a3b8")

    facts = [
        ("SVG Vector Priority", "Browsers pick <link rel='icon' type='image/svg+xml'> first if present", "#38bdf8"),
        ("Dark Mode Adaptation", "SVG media queries (@media prefers-color-scheme: dark) switch colors dynamically", "#34d399"),
        ("Windows Pinned Taskbar", "Windows Explorer extracts 32x32 or 48x48 bitmap layers directly from .ico", "#fbbf24"),
        ("Safari Pinned Tabs", "Safari requires monochromatic SVG with mask-icon rel and color attribute", "#a855f7"),
        ("Aggressive Caching", "Browsers cache favicons indefinitely; use ?v=2 query strings to bust cache", "#22c55e"),
    ]

    y = 115
    for title, desc, col in facts:
        draw_rounded_rect(d, (50, y, 910, y + 68), 12, "#1e293b", col, 1)
        d.text((75, y + 12), title, font=get_font(16, True), fill=col)
        d.text((75, y + 38), desc, font=get_font(15), fill="#cbd5e1")
        y += 78
    img.save(OUTPUT_DIR / "post29-inline-browser-tab-rendering.png")
    print("Created post29-inline-browser-tab-rendering.png")

# 30b: Macronutrient Energy Density
def make_30b():
    img = Image.new("RGB", (960, 540), "#0f172a")
    d = ImageDraw.Draw(img)
    d.text((50, 35), "MACRONUTRIENT CALORIC DENSITY & METABOLIC VALUES", font=get_font(26, True), fill="#10b981")
    d.text((50, 72), "Atwater system energy values per gram of dietary protein, fat, and carbohydrates", font=get_font(17), fill="#94a3b8")

    macros = [
        ("Protein: 4.0 Calories / Gram", "High Thermic Effect (20-30% TEF); essential for lean muscle protein synthesis", "#38bdf8"),
        ("Carbohydrates: 4.0 Calories / Gram", "Moderate Thermic Effect (5-10% TEF); primary energy substrate for glycogen", "#34d399"),
        ("Dietary Fats: 9.0 Calories / Gram", "Low Thermic Effect (0-3% TEF); dense energy storage & hormone production", "#fbbf24"),
        ("Alcohol: 7.0 Calories / Gram", "Toxic byproduct; pauses lipid oxidation until metabolized by the liver", "#ef4444"),
    ]

    y = 120
    for name, desc, col in macros:
        draw_rounded_rect(d, (50, y, 910, y + 78), 14, "#1e293b", col, 2)
        d.text((75, y + 14), name, font=get_font(17, True), fill=col)
        d.text((75, y + 44), desc, font=get_font(15), fill="#cbd5e1")
        y += 92
    img.save(OUTPUT_DIR / "post30-inline-macronutrient-energy-density.png")
    print("Created post30-inline-macronutrient-energy-density.png")

if __name__ == "__main__":
    make_11b()
    make_12b()
    make_13b()
    make_14b()
    make_15b()
    make_16b()
    make_17b()
    make_18b()
    make_19b()
    make_20b()
    make_21b()
    make_22b()
    make_23b()
    make_24b()
    make_25b()
    make_26b()
    make_27b()
    make_28b()
    make_29b()
    make_30b()
    print("ALL 20 SECOND INLINE INFOGRAPHICS CREATED!")
