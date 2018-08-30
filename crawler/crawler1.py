from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

base_url = "http://www.eduxiao.com/"

html = urlopen(base_url).read().decode("gb2312", 'ignore')
soup = BeautifulSoup(html, features='lxml')


navmet = soup.find("div", {"class":'navmet'})
links = navmet.find_all('a')
base_urls = []
for item in links:
    base_urls.append(item["href"])
    
base_urls = base_urls[:-1]


url_collection = []
for url in base_urls:
    html1 = urlopen(url).read().decode("gb2312", 'ignore')
    soup1 = BeautifulSoup(html1, features='lxml')

    pagelist = soup1.find("ul", {"class":'pagelist'})
    links1 = pagelist.find_all('a')
    for item in links1:
        url_collection.append(url+item["href"])
        
url_collection += base_urls
url_collection = list(set(url_collection))


all_urls = []
for url in url_collection:
    html2 = urlopen(url).read().decode("gb2312", 'ignore')
    soup2 = BeautifulSoup(html2, features='lxml')
    listbox = soup2.find("div", {"class":'listbox'})
    links2 = listbox.find_all('a')
    for item in links2:
        all_urls.append(item["href"])

all_urls = list(set(all_urls))


texts = []
remove_index = []
for i, url in enumerate(all_urls):
    print(i)
    print(url)
    html3 = urlopen(url).read().decode("gb2312", 'ignore')
    soup3 = BeautifulSoup(html3, features='lxml')
    content = soup3.find("div", {"class":'content'})
    if content != None:
        text = content.find_all('p')
        for item in text:
            texts.append(item.get_text())
    else:
        remove_index.append(i)
        print("url of index " + str(i) + " should be removed!")
    if i % 500 == 0:
        essay = '\n'.join(texts)
        with open("./essay2.txt", 'w', encoding='utf-8') as f:
            f.write(essay)
    print(i)

essay = '\n'.join(texts)

if not os.path.exists("../data"):
	os.makedirs("../data")

with open("../data/essay1.txt", 'w', encoding='utf-8') as f:
    f.write(essay)