<<<<<<< HEAD
from lxml import etree
import requests,random

pro = ['122.152.196.126', '114.215.174.227', '119.185.30.75']
head = {
    'user-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
}


response = requests.get('https://cd.lianjia.com/zufang/CD2289829356526108672.html?nav=0',
                        proxies={'http': random.choice(pro)}, headers=head)
html = etree.HTML(response.text)
content = html.xpath("//div[@class='content clear w1150']")[0]
title = content.xpath("//p[@class='content__title']/text()")[0]
view_count = content.xpath('//i[@class="hide"]/text()')[0]
imgs = content.xpath('//div[@class="content__article__slide__item"]/img//@data-src')
facilities = content.xpath("//ul[@class='content__article__info2']/li//text()")[1:]





=======
import re

REGION = (
    ('0', '不限'), ('1', '罗湖区'), ('2', '福田区'), ('3', '南山区'), ('4', '龙岗区'), ('5', '盐田区'),
    ('6', '宝安区'), ('7', '光明新区'), ('8', '坪山新区'), ('9', '龙华新区'), ('10', '大鹏新区'),)

regions = [r[1] for r in REGION]
com = r'%s'%regions
text = re.findall(com,'坪山新区')
print(''.join(text))
>>>>>>> c77d35942959f03a1c81eb0afec347e857314f2d
