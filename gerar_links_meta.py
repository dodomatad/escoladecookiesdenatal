import urllib.parse

keywords = [
    "delivery de cookies",
    "cookies ifood",
    "cookies renda extra",
    "delivery de doces em casa",
    "vender cookies",
    "cookies lucrativos",
    "doces no ifood",
    "renda extra doces"
]

print("=== URLS PARAMETRIZADAS META AD LIBRARY ===")
for kw in keywords:
    q = urllib.parse.quote(f'"{kw}"')
    url = f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&media_type=video&search_type=keyword_exact_phrase&q={q}"
    print(f"[{kw}]: {url}")
