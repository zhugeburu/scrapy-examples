#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle


from netease.items import *
from misc.log import *
from misc.spider import CommonSpider

class neteaseSpider(CommonSpider):
      name = "njupt"
    allowed_domains = ["njupt.edu.cn"]
    start_urls = [
        "http://news.njupt.edu.cn/s/222/t/1100/p/1/c/6866/i/1/list.htm",
        ]

    def parse(self, response):
        news_page_num = 14
        page_num = 386
        if response.status == 200:
            for i in range(2,page_num+1):
                for j in range(1,news_page_num+1):
                    item = neteaseItems()
                    item['news_url'],item['news_title'],item['news_date'] = response.xpath(
                    "//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/font/text()"
                    "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//td[@class='postTime']/text()"
                    "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/@href").extract()

                    yield item

                next_page_url = "http://news.njupt.edu.cn/s/222/t/1100/p/1/c/6866/i/"+str(i)+"/list.htm"
                yield scrapy.Request(next_page_url,callback=self.parse_news)

    def parse_news(self, response):
        news_page_num = 14
        if response.status == 200:
            for j in range(1,news_page_num+1):
                item = NjuptItem()
                item['news_url'],item['news_title'],item['news_date'] = response.xpath(
                "//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/font/text()"
                "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//td[@class='postTime']/text()"
                "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/@href").extract()
                yield item
