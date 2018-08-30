from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os

base_url = "http://www.zixuekaoshi.net/"

html = urlopen(base_url).read().decode("gb2312", 'ignore')
soup = BeautifulSoup(html, features='lxml')

qq_menu_bg = soup.find("div", {"class":'qq_menu_bg'})
links = qq_menu_bg.find_all('a')
base_urls = []
for item in links:
    base_urls.append(item["href"])
    
base_urls = base_urls[1:]

url_collection = []
for i, url in enumerate(base_urls):
    html1 = urlopen(url).read().decode("gb2312", 'ignore')
    soup1 = BeautifulSoup(html1, features='lxml')
    pages_w_bg = soup1.find("div", {"class":'pages w_bg'})
    links1 = pages_w_bg.find_all('a')
    for item in links1:
        url_collection.append(item["href"])
        
url_collection = list(set(url_collection))
url_collection.remove("#")


all_urls = []
for i, url in enumerate(url_collection):
    html2 = urlopen(url).read().decode("gb2312", 'ignore')
    soup2 = BeautifulSoup(html2, features='lxml')
    class_name = soup2.find("div", {"class":'qq_list w_bg'})
    links2 = class_name.find_all('a')
    for item in links2:
        all_urls.append(item["href"])


all_urls = list(set(all_urls))
all_url = [all_urls[:1000], all_urls[1000:2000], all_urls[2000:3000], all_urls[3000:4000], all_urls[4000:]]

texts = [[] for i in range(5)]
remove_index = []
for k, all_urls in enumerate(all_url):
    for i, url in enumerate(all_urls):
        print(i)
        print(url)
        html3 = urlopen(url).read().decode("gb2312", 'ignore')
        soup3 = BeautifulSoup(html3, features='lxml')
        content = soup3.find("div", {"class":'qq_nr_zw w_bg'})
        if content != None:
            text = content.find_all('p')
            for j, item in enumerate(text):
                if j > 2:
                    texts[k].append(item.get_text())
        else:
            remove_index.append(i)
            print("url of index " + str(i) + " should be removed!")
        print(i)
        if i == 5:
        	break


temp = []
for item in texts:
    temp += item

r = re.compile(r"(第一篇|第二篇|第三篇|上一篇|下一篇|>>)")
for item in temp:
    if re.findall(r, item) != []:
        temp.remove(item)

for item in temp:
    if item == '\n':
        temp.remove(item)

for item in temp:
    if item == '\r':
        temp.remove(item)

for item in temp:
    if item == ' ':
        temp.remove(item)

for item in temp:
    if item == '  ':
        temp.remove(item)

while '' in temp:
    temp.remove('')

essay = '\n'.join(temp)


if not os.path.exists("../data"):
	os.makedirs("../data")

with open("../data/essay2.txt", 'w', encoding='utf-8') as f:
    f.write(essay)