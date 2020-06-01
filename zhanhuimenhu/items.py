# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhanhuimenhuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    # print(title, interest, startData, endData)

    title = scrapy.Field()
    interest = scrapy.Field()
    startData = scrapy.Field()
    endData = scrapy.Field()
    organize = scrapy.Field()
    release_platform = scrapy.Field()
    contact = scrapy.Field()
    content = scrapy.Field()



