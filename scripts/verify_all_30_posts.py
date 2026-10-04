#!/usr/bin/env python3
import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def check_url(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            return resp.status, content
    except urllib.error.HTTPError as e:
        return e.code, str(e)
    except Exception as e:
        return 0, str(e)

slugs_batch2 = [
    "url-encode-decode-rfc-3986-guide",
    "lorem-ipsum-ui-ux-prototyping-guide",
    "understanding-ip-addresses-ipv4-ipv6-guide",
    "web-color-models-hex-rgb-hsl-guide",
    "text-sanitization-line-breaks-commas-guide",
    "srt-vs-vtt-subtitles-video-seo-guide",
    "youtube-thumbnail-optimization-guide",
    "binary-code-demystified-ascii-guide",
    "percentage-math-markups-margins-guide",
    "loan-amortization-apr-debt-payoff-guide",
    "sales-tax-gst-calculation-guide",
    "metric-vs-imperial-unit-conversion-guide",
    "number-to-words-roman-numerals-guide",
    "data-format-migrations-csv-xml-json-guide",
    "website-legal-compliance-terms-privacy-guide",
    "uuid-guid-architecture-database-keys-guide",
    "utm-tracking-parameters-ga4-attribution-guide",
    "responsive-image-cropping-resizing-guide",
    "complete-favicon-ico-multi-resolution-guide",
    "tdee-calorie-metabolic-math-guide"
]

print("=== VERIFYING POSTS 11 TO 30 ===")
all_ok = True
for slug in slugs_batch2:
    url = f"https://linkefly.xyz/blog/{slug}"
    status, body = check_url(url)
    if status == 200:
        # Check inline images
        imgs = re.findall(r'<img[^>]+src="([^">]+assets/img/blog/[^">]+)"', body)
        # Check author
        has_author = "LinkeFly" in body
        has_avatar = "avatar.png" in body or "avatar.jpg" in body
        has_faq = "faqAccordion" in body or "Frequently Asked Questions" in body
        print(f"OK [200]: {slug} | Inline imgs: {len(imgs)} | Author: {has_author} | FAQ: {has_faq}")
    else:
        print(f"FAILED [{status}]: {url}")
        all_ok = False

print("\n=== CHECKING HOMEPAGE FOR POST LEAKS / NO-THUMB ICONS ===")
h_status, h_body = check_url("https://linkefly.xyz/")
no_thumb_count = h_body.count("no-thumb.svg")
print(f"Homepage HTTP Status: {h_status}")
print(f"Homepage 'no-thumb.svg' count: {no_thumb_count}")

print("\n=== CHECKING BLOG INDEX PAGE ===")
b_status, b_body = check_url("https://linkefly.xyz/blog")
post_cards = len(re.findall(r'/blog/[a-zA-Z0-9\-]+', b_body))
print(f"Blog Index HTTP Status: {b_status}")
print(f"Blog Index Post links found: {post_cards}")

if all_ok and no_thumb_count == 0:
    print("\nALL CHECKS PASSED WITH FLYING COLORS!")
else:
    print("\nSOME CHECKS FAILED!")
