from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

url = str(input("Please enter a link to get all images from the site: "))
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
img = soup.find_all("img")
outfile = open("tags.txt", "w")

for c in img:
    imgSrc = c.get("src")
    outfile.write(imgSrc + "\n\n")
outfile.close()