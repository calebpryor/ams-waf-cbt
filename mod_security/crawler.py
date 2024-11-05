import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
import argparse

def normalize_url(base, url):
    joined_url = urljoin(base, url)
    parsed_url = urlparse(joined_url)
    path_parts = parsed_url.path.split('/')
    if path_parts:
        filename = path_parts[-1]
        if '.' in filename:
            extension = filename.split('.')[-1]
            path_parts[-1] = f"normalized.{extension}"
        else:
            path_parts[-1] = "normalized"
    normalized_path = '/'.join(path_parts)
    normalized_url = urlunparse(parsed_url._replace(path=normalized_path))
    return normalized_url

def crawl_website(base_url):
    visited = set()
    to_visit = [base_url]
    css_files = []
    js_files = []
    image_files = []
    json_files = []

    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            original_url = urljoin(base_url, link['href'])
            parsed_url = urlparse(original_url)
            if parsed_url.netloc == urlparse(base_url).netloc:
                to_visit.append(original_url)

        for css in soup.find_all('link', rel='stylesheet'):
            css_url = normalize_url(base_url, css['href'])
            css_files.append(css_url)

        for script in soup.find_all('script', src=True):
            js_url = normalize_url(base_url, script['src'])
            js_files.append(js_url)

        for img in soup.find_all('img', src=True):
            img_url = normalize_url(base_url, img['src'])
            image_files.append(img_url)

        for link in soup.find_all('a', href=True):
            if link['href'].endswith('.json'):
                json_url = normalize_url(base_url, link['href'])
                json_files.append(json_url)

    return visited, css_files, js_files, image_files, json_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl a website and collect URLs of CSS, JS, image, and JSON files.")
    parser.add_argument('base_url', type=str, help='The base URL of the website to crawl')
    args = parser.parse_args()

    base_url = args.base_url
    urls, css_files, js_files, image_files, json_files = crawl_website(base_url)
    
    if not urls:
        print("No pages found.")
        exit()
    print("Visited Pages:")
    for url in urls:
        print(url)
    
    if css_files:
        print("\nCSS Files:")
        for css in css_files:
            print(css)

    if js_files:
        print("\nJS Files:")
        for js in js_files:
            print(js)
    
    if image_files:
        print("\nImage Files:")
        for img in image_files:
            print(img)
    
    if json_files:
        print("\nJSON Files:")
        for json in json_files:
            print(json)