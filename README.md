# Wayback URL Fetcher

**Professional Python CLI tool** that queries the Internet Archive CDX API to retrieve **comprehensive archived URL inventories** for any target domain, including all subdomains.

## ✨ Key Features

- **Complete Coverage** - Main domain + **all subdomains**
- **Production Filtering** - HTTP 200 status code only
- **Automatic Deduplication** - Zero duplicate URLs  
- **Clean Output** - `<domain>_wayback_urls.txt` format
- **URL Normalization** - Handles `www.` + various formats
- **Enterprise-grade** - 10min timeout + robust error handling

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python wayback_url_fetcher.py
```

**Input**: `example.com`  
**Output**: `example.com_wayback_urls.txt`

## 📊 Professional Use Cases
🔍 OSINT investigations
🔬 Historical web research
🛡️ Security reconnaissance
📈 SEO historical audits
🏛️ Digital preservation
📊 Competitor analysis
