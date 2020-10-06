# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter
from .database import Vaishnadb 
from .database import VaishnadbPG


class VaishnavismPipeline:
    
    db = Vaishnadb()

    def process_item(self, item, spider):
        if spider.name == "ekadasi_spider":
            name = item["name"]
            day = item["day"]
            month = item["month"]
            year = item["year"]
            start = item["starts"][0]
            end = item["starts"][0]
            self.db.addEkadasiItem(name, day, month, year, start, end)        

        elif spider.name == "iskcon_calendar":
            name = item["name"]
            month = item["month"]
            day = item["day"]
            year = item["year"]
            self.db.addIskconEventItem(name, month, day, year)



class VaishnavismPipelinePG:

    db = VaishnadbPG()

    def process_item(self, item, spider):
        if spider.name == "ekadasi_spider":
            name = item["name"]
            day = item["day"]
            month = item["month"]
            year = item["year"]
            starts = item["starts"][0]
            ends = item["starts"][0]
            self.db.addEkadasiItem(name, day, month, year, starts, ends)        

        elif spider.name == "iskcon_calendar":
            name = item["name"]
            month = item["month"]
            day = item["day"]
            year = item["year"]
            self.db.addIskconEventItem(name, month, day, year)



