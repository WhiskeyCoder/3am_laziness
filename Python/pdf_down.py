import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.parse import urlparse

url = 'https://YOUR_WEBSITE_ADDRESS_GOES_HERE/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.60 Safari/537.36'
}

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a', href=True)
    domain = urlparse(url).netloc
    folder_name = domain.replace(".", "_")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for link in links:
        if link['href'].endswith('.pdf'):
            pdf_url = link['href']
            print(pdf_url)
            pdf_filename = os.path.basename(pdf_url)
            pdf_path = os.path.join(folder_name, pdf_filename)
            try:
                urllib.request.urlretrieve(pdf_url, pdf_path)
                print(f"Downloaded: {pdf_path}")
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print(f"HTTP Error 404: {pdf_url} not found")
                else:
                    print(f"HTTP Error {e.code}: {e.reason} - {pdf_url}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
