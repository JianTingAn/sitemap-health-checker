import argparse
import csv
import json
import re
from collections import Counter

BOT_RE = re.compile(r"(baiduspider|googlebot|bingbot|sogou|yisou|360spider)", re.I)

def load_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def demo_rows():
    return [
        {"url":"https://example.com/", "status":"200", "user_agent":"Mozilla/5.0 (compatible; Baiduspider/2.0)", "ms":"180"},
        {"url":"https://example.com/old", "status":"301", "user_agent":"Mozilla/5.0 (compatible; Baiduspider/2.0)", "ms":"420"},
        {"url":"https://example.com/missing", "status":"404", "user_agent":"Mozilla/5.0 (compatible; Googlebot/2.1)", "ms":"90"},
    ]

def analyze(rows):
    statuses = Counter(str(r.get("status", "unknown")) for r in rows)
    bots = Counter("search-bot" if BOT_RE.search(r.get("user_agent", "")) else "other" for r in rows)
    slow = [r for r in rows if float(r.get("ms", 0) or 0) >= 1000]
    return {"total": len(rows), "statuses": dict(statuses), "bot_classes": dict(bots), "slow_requests": len(slow), "urls": sorted({r.get("url", "") for r in rows if r.get("url")})}

def main():
    ap = argparse.ArgumentParser(description="Analyze crawler observability CSV data")
    ap.add_argument("--input", help="CSV with url,status,user_agent,ms columns")
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if not args.input and not args.demo:
        ap.error("use --input FILE or --demo")
    result = analyze(demo_rows() if args.demo else load_rows(args.input))
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else f"requests: {result['total']}\nstatuses: {result['statuses']}\nbot_classes: {result['bot_classes']}\nslow_requests: {result['slow_requests']}")

if __name__ == "__main__":
    main()
