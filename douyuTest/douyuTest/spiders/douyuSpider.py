#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractor import LinkExtractor as sle
# from douyuTest.douyuTest.items import DouyutestItem
from douyuTest.items import *


class DouyuSpider(Spider):
    name = 'douyutest'
    allowed_domains = ["douyu.com"]
    start_urls = [
        "http://www.douyu.com/directory/all"
    ]

    rules = [
        Rule(sle(allow="http://www.douyu.com/directory/all"),callback="parse_1",follow=True),
    ]
    def parse_1(self,reponse):
        selector = Selector(reponse)
        items = []
        room = selector.css('#anchor-info')[0]
        item = DouyutestItem()
        # item = {}
        item['room_name'] = room.xpath('/div[2]/div[1]/h1/text()').extract_first()
        item['room_visitor'] = room.xpath('/div[2]/div[3]/ul/li[2]/div/div[2]/a/text()').extract_first()
        item['room_owner'] = room.xpath('/div[2]/div[3]/ul/li[1]/div/a/text()').extract_first()
        item['room_popularity'] = room.xpath('/div[2]/div[2]/dl/dd/a[2]/text()').extract_first()
        items.append(item)
            # yield  item
            # print repr(item).decode("unicode-escape") + '\n'
        return items
