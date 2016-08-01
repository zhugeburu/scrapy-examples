# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
from collections import OrderedDict
import json


class NeteasePipeline(object):
    def __init__(self):
        self.file = open('njupt.txt',mode='wb')
    def process_item(self, item, spider):
        self.file.write(item['title'].encode("GBK"))
        self.file.write("\n")
        self.file.write(item['url'].encode("GBK"))
        self.file.write("\n")
        return item
