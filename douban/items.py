# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieLink(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    rank = scrapy.Field()
    star = scrapy.Field()
    people = scrapy.Field()
    description = scrapy.Field()
