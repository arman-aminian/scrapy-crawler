# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TgjucrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    first = scrapy.Field()
    min = scrapy.Field()
    max = scrapy.Field()
    last = scrapy.Field()
    change_value = scrapy.Field()
    change_percent = scrapy.Field()
    gregorian_date = scrapy.Field()
    solar_date = scrapy.Field()
