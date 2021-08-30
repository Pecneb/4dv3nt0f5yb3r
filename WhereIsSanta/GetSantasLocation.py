from bs4 import BeautifulSoup
import requests

for api_key in range(1,100,2):
    html = requests.get(f"http://10.10.250.186:80/api/{api_key}")
    print(f"api_key = {api_key}")
    print(html.text)
    if "Error. Key not valid!" not in html.text:
        break
