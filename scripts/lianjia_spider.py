# encoding:utf-8
from lxml import etree
from api.house.models import House
import json, requests, random, time, threading
from queue import Queue


class Base(threading.Thread):
    index_page_url = "https://sz.lianjia.com/zufang/pg{page}rt200600000001rp1rp2rp3/#contentList"
    detail_page_url = 'https://sz.lianjia.com{detail_url}?nav=0'
    pro = ['122.152.196.126', '114.215.174.227', '119.185.30.75']
    head = {
        'user-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
    }
    def send_http_get(self, url):
        response = requests.get(url, proxies={'http': random.choice(self.pro)}, headers=self.head)
        return response


class Producer(Base):  # 生产者
    def __init__(self, *args, **kwargs):
        self.index_queue = kwargs.pop('index_queue')
        self.detail_queue = kwargs.pop('detail_queue')
        super(Producer, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            if self.index_queue.empty():
                break
            url = self.index_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = self.send_http_get(url)
        html = etree.HTML(response.text)
        # 详情界面
        detail_urls = html.xpath('//a[@class="content__list--item--aside"]//@href')
        for url in detail_urls:
            self.detail_queue.put(self.detail_page_url.format(detail_url=url))


class Consumer(Base):
    def __init__(self, *args, **kwargs):
        self.index_queue = kwargs.pop('index_queue')
        self.detail_queue = kwargs.pop('detail_queue')
        super(Consumer, self).__init__(*args, **kwargs)
    def run(self):
        while True:
            if self.detail_queue.empty() and self.index_queue.empty():
                break
            url = self.detail_queue.get()
            self.parse_detail_page(url)

    def lxml_parse(self, target, regular, index):
        try:
            result = target.xpath(regular)[index]
        except Exception as e:
            result = ""
        return result

    def parse_detail_page(self, url):
        try:
            response = self.send_http_get(url)
            html = etree.HTML(response.text)
            content = html.xpath("//div[@class='content clear w1150']")[0]
            title = content.xpath("//p[@class='content__title']/text()")[0]
            view_count = content.xpath('//i[@class="hide"]/text()')[0]
            imgs = content.xpath('//div[@class="content__article__slide__item"]/img//@data-src')
            facilities = content.xpath("//ul[@class='content__article__info2']/li//text()")[1:]
            # upload_time = content.xpath("//div[@class='content__subtitle']//text()")[2]
            rent_type, house_type, area, direction = [x for x in content.xpath("//p[@class='content__article__table']//"
                                                                               "text()") if not x.startswith("\n")]
            desc = self.lxml_parse(content, '//p[@data-el="houseComment"]//@data-desc', 0)
            price = content.xpath("//p[@class='global__list--subtitle oneline']/span/text()")[0]
            House.objects.create(
                title=title, price=price, desc=desc, area=area, address=title, imgs=
                json.dumps(imgs), apartment=rent_type, diraction=direction, publisher_id=1, view_count=view_count,
                facilities=json.dumps(facilities)
            )
        except Exception as e:
            print(e)


def run():
    start = time.time()
    tsk = []
    index_queue = Queue(1000)
    detail_queue = Queue(1000)
    for x in range(10):
        # 存储页面信息
        url = Base.index_page_url
        index_queue.put(url.format(page=x))

    for x in range(5):
        t = Producer(index_queue=index_queue, detail_queue=detail_queue)
        t.start()
        tsk.append(t)

    for x in range(5):
        t = Consumer(index_queue=index_queue, detail_queue=detail_queue)
        t.start()
        tsk.append(t)

    # 终止运行，统计时间
    for t in tsk:
        t.join()
    #
    end = time.time()
    print('耗时：%0.002fs' % (end - start))

# python manage.py runscript lianjia_spider
