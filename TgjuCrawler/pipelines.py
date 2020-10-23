# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a  single interface
from itemadapter import ItemAdapter

import pymongo


class TgjucrawlerPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn["price_col"]
        self.sekee_collection = db["sekee_price"]
        self.dollar_collection = db["dollar_price"]
        self.geram18_collection = db["geram18_price"]

    def process_item(self, item, spider):
        if spider.name in ['sekee', 'last_sekee']:
            self.sekee_collection.update_one(dict(item), upsert=True)
            return item
        if spider.name in ['geram18', 'last_geram18']:
            self.geram18_collection.update_one(dict(item), upsert=True)
            return item
        if spider.name in ['dollar', 'last_dollar']:
            self.dollar_collection.update_one(dict(item), upsert=True)
            return item
