import pandas as pd
from sqlalchemy import create_engine
from util.scrawl import *
import os

def repay():
    engine = create_engine('mysql+pymysql://root:gkd123,.@47.101.44.55:3306/Houseprice?charset=utf8', encoding='utf-8')
    df = pd.read_sql('select * from infodata', engine)
    cc = 0
    for index, row in df.iterrows():
        cc += 1
        if cc < 14668:
            continue
        print(cc)
        url = row['url'].replace('xiangqing', 'xiangce')
        html = getHTML(url)
        count = 0
        while True:
            count += 1
            try:
                type = html.xpath('/html/body/div[2]/div[1]/div/div[{0}]/h4/a/text()'.format(count))[0].split('（')[0]
                pics = html.xpath('/html/body/div[2]/div[1]/div/div[{0}]/ul/li/a/img/@src'.format(count))
            except:
                break
            if 'VR' not in type:
                with open('test.txt', 'a+', encoding='utf-8') as f:
                    for pic in pics:
                        f.write(str(cc) + ',' + row['url'] + ',' + type + ',' + pic + '\n')
            else:
                continue


def clean():
    count = 0
    with open('test.txt', 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
    for item in data:
        pic = item.split('https://ke-image.ljcdn.com/')[-1].split('!')[0]
        num = item.split(',')[0]
        url = item.split(',')[1]
        type_ = item.split(',')[2]
        with open(os.getcwd() + '/tosql.sql', 'a+', encoding='utf-8') as t:
            t.write("INSERT INTO `loupan_pic` VALUES ('{0}','{1}','{2}','{3}');".format(num, url, type_, pic))
            t.write('\n')
            count += 1
            print(count)
        pass

if __name__ == '__main__':
    # repay()
    clean()

