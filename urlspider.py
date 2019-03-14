import requests
from util.headers import *
from lxml import etree


def geturl():
    url = 'https://su.fang.ke.com/loupan'
    rsp = requests.get(url, headers=create_headers(url), timeout=3)
    html = etree.HTML(rsp.text)
    city_url = html.xpath('/html/body/div[2]/div[3]/div/ul/li/div/a/@href')
    city_name = html.xpath('/html/body/div[2]/div[3]/div/ul/li/div/a/text()')
    # dic = {}
    with open('city_url.txt', 'a+', encoding='utf-8') as f:
        for i in range(len(city_url)):
            f.write(city_url[i].split('//')[1] + ',' + city_name[i] + '\n')


if __name__ == '__main__':
    geturl()