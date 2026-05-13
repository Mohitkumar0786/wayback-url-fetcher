import requests
import json
import re
from urllib.parse import urlparse

def sanitize_filename(url):
    """
    Create safe filename from URL
    """
    parsed = urlparse(url)

    domain = parsed.netloc if parsed.netloc else parsed.path

    filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', domain)

    return f"{filename}_wayback_urls.txt"


def fetch_wayback_urls(domain):
    """
    Fetch all archived URLs including subdomains
    """

    api_url = (
        "https://web.archive.org/cdx/search/cdx"
        f"?url=*.{domain}/*"
        "&output=json"
        "&fl=original,mimetype,statuscode,timestamp"
        "&collapse=urlkey"
        "&filter=statuscode:200"
    )

    try:
        response = requests.get(api_url, timeout=600)

        if response.status_code != 200:
            print(f"[!] Failed with status code: {response.status_code}")
            return []

        data = response.json()

        if len(data) <= 1:
            return []

        results = []

        # Skip header row
        for row in data[1:]:
            try:
                results.append({
                    "url": row[0],
                    "mimetype": row[1],
                    "status": row[2],
                    "timestamp": row[3]
                })
            except:
                continue

        return results

    except Exception as e:
        print(f"[!] Error: {e}")
        return []


def save_results(filename, results):

    unique_urls = set()

    with open(filename, "w", encoding="utf-8") as f:

        f.write("Wayback Machine Archived URLs\n")
        f.write("=" * 80 + "\n\n")

        for item in results:

            url = item["url"]

            if url in unique_urls:
                continue

            unique_urls.add(url)

            f.write(f"URL       : {url}\n")
            f.write("-" * 80 + "\n")

    print(f"\n[+] Saved {len(unique_urls)} unique URLs to {filename}")


def extract_domain(input_url):
    """
    Extract clean domain
    """

    if not input_url.startswith("http"):
        input_url = "https://" + input_url

    parsed = urlparse(input_url)

    domain = parsed.netloc

    # Remove www.
    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def main():

    target = input("Enter target domain: ").strip()

    domain = extract_domain(target)

    print(f"\n[*] Searching Internet Archive for:")
    print(f"    - Main domain")
    print(f"    - All subdomains")
    print(f"    - Historical archived URLs\n")

    results = fetch_wayback_urls(domain)

    if not results:
        print("[!] No archived URLs found.")
        return

    filename = sanitize_filename(domain)

    save_results(filename, results)


if __name__ == "__main__":
    main()
