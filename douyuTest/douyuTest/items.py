# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item,Field

class DouyutestItem(Item):
    # url = Field()
    room_name = Field()
    room_visitor = Field()
    room_owner = Field()
    room_popularity = Field()
