import requests
from util.headers import *
from lxml import etree
from item import loupan
import threadpool
from time import sleep
from util.scrawl import getHTML


def get_page(url):
    url = 'https://' + url
    # rsp = requests.get(url, headers=create_headers(url), timeout=3)
    html = getHTML(url)
    count = 1
    while html.xpath('/html/body/section[2]/div/a[{0}]/text()'.format(count)) != []:
        count += 1
    page = count - 1
    return page
    pass


def get_region(url):
    regions_py = {}
    url = 'https://' + url
    # rsp = requests.get(url, headers=create_headers(url), timeout=3)
    # html = etree.HTML(rsp.text)
    html = getHTML(url)
    py = html.xpath('/html/body/div[4]/div[2]/ul/li/@data-district-spell')
    regions = html.xpath('/html/body/div[4]/div[2]/ul/li/text()')
    for i in range(len(py)):
        regions_py[py[i]] = regions[i]
    print("共有{0}个区".format(len(py)))
    return regions, regions_py


def get_outer(url, page, lp):
    url = url + '/pg' + str(page)
    # rsp = requests.get(url, headers=create_headers(url), timeout=3)
    # html = etree.HTML(rsp.text)
    html = getHTML(url)
    jud_xpath = '/html/body/div[5]/ul[2]/li[{0}]/text()'
    lps = []
    for i in range(1,11):
        try:
            if html.xpath(jud_xpath.format(i))[0] == '猜你喜欢':
                break
        except:
            break
        lp.xiaoqu = str(html.xpath('/html/body/div[5]/ul[2]/li[{0}]/div/div[1]/a/text()'.format(i))[0])
        temp = html.xpath('/html/body/div[5]/ul[2]/li[{0}]/div/div[4]/div[1]/span/text()'.format(i))
        try:
            lp.price = temp[0] + ' ' + temp[1].split('\xa0')[1]
        except:
            lp.price = ''
        try:
            lp.total = str(html.xpath('/html/body/div[5]/ul[2]/li[{0}]/div/div[4]/div[2]/text()'.format(i))[0])
        except:
            lp.total = ''
        lp.url = url.split('/loupan')[0] + html.xpath('/html/body/div[5]/ul[2]/li[{0}]/div/div[1]/a/@href'.format(i))[0]
        lps.append(get_inner(lp))
    save(lps)


def get_inner(lp):
    # 详情url
    xqurl = lp.url + 'xiangqing/'
    # rsp = requests.get(xqurl, headers=create_headers(xqurl), timeout=3)
    # html = etree.HTML(rsp.text)
    html = getHTML(xqurl)

    ## 基本信息
    # 物业类型
    try:
        lp.propertyType = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[1]/li[1]/span[2]/text()"))
    except:
        lp.propertyType = ''
    # 参考价格
    try:
        # loupan.referencePrice = getInfo1(res.xpath("/html/body/div[2]/div[1]/ul[1]/li[2]/span[2]/span/text()")).split(' ')[1].split('元/平')[0]
        lp.referencePrice = \
        getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[1]/li[2]/span[2]/span/text()")).split(' ')[1]

    except:
        lp.referencePrice = ''

    if lp.referencePrice.find('套') > 0:
        try:
            lp.referencePrice = str(lp.referencePrice.split(' ')[1].split('万/套')[0])
        except:
            try:
                lp.referencePrice = str(float(lp.referencePrice.split('万/套')[0]))
            except:
                lp.referencePrice = ''

    # 面积
    try:
        lp.area = getArea(lp.url)
    except:
        lp.area = ''

    # 项目特色
    try:
        lp.projectFeatures = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[1]/li[3]/span[2]/text()"))
    except:
        lp.projectFeatures = ''

    #  区域位置 todo
    try:
        lp.regionallocation = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[1]/li[4]/span[2]/text()")) + \
                                  getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[1]/li[4]/span[2]/a/text()"))

        if not lp.regionallocation:
            lp.regionallocation = "暂无信息"
    except:
        lp.regionallocation = ''
    # 楼盘地址
    try:
        lp.propertyaddress = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[1]/li[5]/span[2]/text()"))
    except:
        lp.propertyaddress = ''

    # 售楼处地址
    try:
        lp.salesOfficeAddress = getInfo1(
            html.xpath("/html/body/div[2]/div[1]/ul[1]/li[6]/span[2]/text()"))
    except:
        lp.salesOfficeAddress = ''
    # 开发商
    try:
        lp.developer = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[1]/li[7]/span[2]/text()"))
    except:
        lp.developer = ''

    ## 规划信息
    # 建筑类型
    try:
        lp.buildingType = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[3]/li[1]/span[2]/text()"))
    except:
        lp.buildingType = ''
    # 绿化率
    try:
        lp.landscapingRatio = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[3]/li[2]/span[2]/text()"))
    except:
        lp.landscapingRatio = ''

    # 占地面积
    try:
        lp.siteArea = getInfo2(html.xpath("/html/body/div[2]/div[1]/ul[3]/li[3]/span[2]/text()"))
    except:
        lp.siteArea = ''

    # 容积率
    try:
        lp.floorAreaRatio = getInfo2(html.xpath("/html/body/div[2]/div[1]/ul[3]/li[4]/span[2]/text()"))
    except:
        lp.floorAreaRatio = ''

    # 建筑面积
    try:
        lp.buildingArea = getInfo2(html.xpath("/html/body/div[2]/div[1]/ul[3]/li[5]/span[2]/text()"))
    except:
        lp.buildingArea = ''

    # 产权年限
    try:
        lp.yearofpropertyRights = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[3]/li[8]/span[2]/text()"))
    except:
        lp.yearofpropertyRights = ''
    # 规划户数
    try:
        lp.numPlan = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[3]/li[7]/span[2]/text()"))
    except:
        lp.numPlan = ''
    # 楼盘户型
    # lp.designType = res.xpath("").extract()

    ## 配套信息
    # 物业公司
    try:
        lp.propertyCompany = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[4]/li[1]/span[2]/text()"))
    except:
        lp.propertyCompany = ''
    # 车位配比
    try:
        lp.parkingRatio = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[4]/li[2]/span[2]/text()"))
    except:
        lp.parkingRatio = ''

    # 物业费
    try:
        lp.propertycosts = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[4]/li[3]/span[2]/text()"))
    except:
        lp.propertycosts = ''
    # 供暖方式
    try:
        lp.heatingMethod = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[4]/li[4]/span[2]/text()"))
    except:
        lp.heatingMethod = ''
    # 供水方式
    try:
        lp.waterSupplyMethod = getInfo1(
            html.xpath("/html/body/div[2]/div[1]/ul[4]/li[5]/span[2]/text()"))
    except:
        lp.waterSupplyMethod = ''
    # 供电方式
    try:
        lp.powerSupply = getInfo1(html.xpath("/html/body/div[2]/div[1]/ul[4]/li[6]/span[2]/text()"))
    except:
        lp.powerSupply = ''
    # 车位
    try:
        lp.parkingSpace = getInfo2(html.xpath("/html/body/div[2]/div[1]/ul[4]/li[7]/span[2]/text()"))
    except:
        lp.parkingSpace = ''

    # 周边
    # try:
    #     temp_xpath = '//*[@id="around_txt"]/div[{0}]/span'
    #     temp_xpath2 = '//*[@id="around_txt"]/div[{0}]/@data-value'
    #     for i in range(1,7):
    #         if html.xpath(temp_xpath.format(i) + '/text()') != []:
    #             lp.nearby += html.xpath(temp_xpath2.format(i)) + ':' + html.xpath(temp_xpath.format(i)) + '\n'
    # except:
    #     lp.nearby = ''

    ## 图片
    xcurl = lp.url + 'xiangce/'
    # rsp = requests.get(xcurl, headers=create_headers(xcurl), timeout=3)
    # html = etree.HTML(rsp.text)
    html = getHTML(xcurl)
    try:
        pics = html.xpath('/html/body/div[2]/div[1]/div/div/ul/li/a/img/@src')
        for pic in pics:
            lp.date +=  str(pic).split('!')[0]
        # lp.date = '"' + lp.date + '"'
    except:
        lp.date = ''
    return lp

def save(lps):
    print('save')
    with open('test.txt','a+',encoding='utf-8') as f:
        for i in lps:
            f.write(i.text() + '\n')



def start(i):
    info = i.split(',')
    regions, regions_py = get_region(info[0])
    for region in regions_py.keys():
        pages = get_page(info[0] + '/' + region)
        lp = loupan.LouPan(info[1], regions_py[region])
        for page in range(pages):
            get_outer('https://' + info[0] + '/' + region, page, lp)


def getInfo1(i):
    return i[0].strip().replace(',','，').strip('\n')


def getInfo2(i):
    return i[0].split("\n")[1].strip().replace(',','，')

def getArea(url):
    # rsp = requests.get(url, headers=create_headers(url), timeout=3)
    # html = etree.HTML(rsp.text)

    html = getHTML(url)
    try:
        area = html.xpath("/html/body/div[2]/div[7]/div/div[2]/div[1]/ul/li[1]/ul/li[2]/p[2]/span[1]/text()")
        sum = 0
        for i in area:
            sum += float(i.split(' ')[1].split('m²')[0])
        return str(sum / len(area))
    except:
        return ''


if __name__ == '__main__':
    with open('city_url.txt', 'r', encoding='utf-8') as f:
        city_url = f.read().split('\n')
    pool = threadpool.ThreadPool(10)
    my_requests = threadpool.makeRequests(start, city_url)
    [pool.putRequest(req) for req in my_requests]
    pool.wait()
    pool.dismissWorkers(10, do_join=False)
    # for i in city_url:
    #     start(i)