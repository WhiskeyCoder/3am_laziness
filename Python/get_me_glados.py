import os
import requests
from bs4 import BeautifulSoup
import urllib

url = "https://theportalwiki.com/wiki/GLaDOS_voice_lines_(Portal)"
if not os.path.exists("files"):
    os.makedirs("files")

response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
download_links = soup.find_all('a', text='Download', href=True)
for link in download_links:
    file_url = link['href']
    filename = file_url.split('/')[-1]
    filepath = os.path.join("audio_files", filename)
    try:
        urllib.request.urlretrieve(file_url, filepath)
        print(f"File '{filename}' downloaded successfully.")
    except Exception as e:
        print(f"Failed to download file from {file_url}. Error: {str(e)}")
