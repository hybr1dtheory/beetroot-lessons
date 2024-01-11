from os import path
import requests as rq
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Beetroot"
resp = rq.get(url)

# response object return false if status_code >= 400
if resp:
    enc = resp.encoding
    with open("robots.html", "w", encoding=enc) as page:
        page.write(resp.text)
else:
    print(f"The request return error: {resp.status_code}")

if path.isfile("robots.html"):
    text: str
    with open("robots.html", 'r', encoding='utf-8') as fr:
        soup = BeautifulSoup(fr, features="html.parser")
        text = soup.get_text()
# replace extra newline characters from text
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")

    with open("robots.txt", 'w', encoding='utf-8') as fw:
        fw.write(text)
else:
    print("file robots.html was not found")
