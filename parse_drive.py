import re
from bs4 import BeautifulSoup

with open('gdrive_folder.html', 'r', encoding='utf-8', errors='ignore') as fp:
    c = fp.read()

soup = BeautifulSoup(c, 'html.parser')
print("Title:", soup.title.string if soup.title else "No title")

# Look for file items in GDrive JSON blobs
# GDrive embeds file data in js / data attributes
files = re.findall(r'\[\"([a-zA-Z0-9_\-\. ]+\.(?:mp4|mov|jpg|jpeg|png|mp3|wav|m4a|pdf))\"', c, re.I)
print("Files found regex 1:", set(files))

# Find file names in general
names = re.findall(r'"([0-9a-zA-Z_\-\. ]{3,50}\.(?:mp4|mov|jpg|jpeg|png|mp3|wav))"', c, re.I)
print("Files found regex 2:", set(names))

# Print any meta tags
for meta in soup.find_all('meta'):
    if meta.get('property') or meta.get('name'):
        print(f"Meta: {meta.get('property') or meta.get('name')} -> {meta.get('content')}")
