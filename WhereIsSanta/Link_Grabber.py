#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

html = requests.get('http://10.10.121.212/static/index.html')

soup = BeautifulSoup(html.text, "html.parser")

links = soup.find_all('a')

for link in links:
    print(link)
