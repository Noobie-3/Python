from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
url = "https://www.tesla.com/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

img = soup.find_all("img")

print(page)
for c in img:
    ImgSrc = c.get("img")
    if ImgSrc != None:
        print(url + "/" + ImgSrc)
        urlretrieve(url, ImgSrc, ImgSrc.replace("/", ""))