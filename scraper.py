from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
import ssl

cate_name = "yourbrand"
baseUrl = "https://www.yourbrand.kr/"
crawl_num = 50
context = ssl._create_unverified_context()

url = baseUrl + cate_name
html = urlopen(url, context=context)
soup = bs(html, "html.parser")
img = soup.find_all(class_="_org_img")
n = 1
for i in img:
    print(n)
    imgUrl = i["data-src"]
    with urlopen(imgUrl, context=context) as f:
        with open(
            "./images/" + cate_name + str(n) + ".jpg", "wb"
        ) as h:  # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
    if n > crawl_num:
        break


print("Image Crawling is done.")
