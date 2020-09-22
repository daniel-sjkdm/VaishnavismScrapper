# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .database import Vaishnadb 


class VaishnavismPipeline:
    
    db = Vaishnadb()

    def process_item(self, item, spider):
        if spider.name == "ekadasi_spider":
            name = item["name"]
            day = item["day"]
            month = item["month"]
            year = item["year"]
            start = item["start"][0]
            end = item["start"][0]
            self.db.addEkadasiItem(name, day, month, year, start, end)        

        elif spider.name == "iskcon_calendar":
            name = item["name"]
            month = item["month"]
            day = item["day"]
            year = item["year"]
            self.db.addIskconEventItem(name, month, day, year)
