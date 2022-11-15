from urllib.parse import urljoin

import lxml.html
import requests

base_url = 'https://songs.travisbriggs.com/'
resp = requests.get(base_url)

tree = lxml.html.fromstring(resp.text)
audios = tree.cssselect('audio')
urls = [urljoin(base_url, a.attrib['src']) for a in audios]

for url in urls:
  print(url)
