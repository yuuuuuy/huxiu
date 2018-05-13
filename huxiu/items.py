# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuxiuItem(scrapy.Item):
    title = scrapy.Field()   # 标题
    link = scrapy.Field()    # 链接
    desc = scrapy.Field()    # 简述
    post_time = scrapy.Field()    # 发布时间

