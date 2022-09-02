# Define here the models for your scraped items
# stored scraped data in items.py
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotestutorialItem(scrapy.Item):
    # define the fields for your item here like:
     title  = scrapy.Field()
     author = scrapy.Field()
     tag    = scrapy.Field()


