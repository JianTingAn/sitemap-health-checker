# sitemap-health-checker

This is an independent open-source project in the Baidu Crawler Open Source series. It focuses on real crawler observability, including access-log analysis, Sitemap and robots.txt checks, HTTP status monitoring, canonical validation, response performance, and content-change detection.

## Detailed introduction

The tool is designed for site owners, developers, and SEO operations teams who need reproducible evidence about how a site is being accessed. It analyzes local CSV or JSON-derived data and produces machine-readable results. The User-Agent classifier is only a log label; it does not prove that a request came from official search-engine infrastructure.

This project does not forge search-engine identity, generate fake spider traffic, manipulate rankings, bypass access controls, or promise indexing results. Use low request rates, respect robots.txt, and monitor only sites and data you are permitted to inspect.

## Features

- Offline demo mode with deterministic sample data
- CSV input with url,status,user_agent,ms columns
- Status-code aggregation and slow-request count
- Search-bot User-Agent classification
- JSON output for scheduled jobs and dashboards
- No cloud service, credential, or third-party dependency required

## Quick start

Requires Python 3.10 or newer:

`powershell
python tool.py --demo
python tool.py --demo --json
python tool.py --input sample.csv --json
`

## CSV format

`csv
url,status,user_agent,ms
https://example.com/,200,Mozilla/5.0 (compatible; Baiduspider/2.0),180
`

## Result interpretation

- statuses: counts by HTTP status. Review 4xx, 5xx, and unexpected redirects.
- ot_classes: a User-Agent classification only, not an authenticity verification.
- slow_requests: responses taking at least 1000 milliseconds.

## Contact

Website: https://jta.mobi  
QQ group: 1039545483

## License

MIT License
