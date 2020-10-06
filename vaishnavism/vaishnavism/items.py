# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EkadasiItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    day = scrapy.Field()
    month = scrapy.Field()
    starts = scrapy.Field()
    ends = scrapy.Field()


class IskconEventItem(scrapy.Item):
    name = scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()
    year = scrapy.Field()
