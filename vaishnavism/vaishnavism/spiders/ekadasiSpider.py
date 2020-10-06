import re
import scrapy
from ..items import EkadasiItem


class EkadasiSpider(scrapy.Spider):

    name = "ekadasi_spider"
    
    start_urls = [
        "https://www.drikpanchang.com/vrats/ekadashidates.html?year=2020" 
    ]


    def parse(self, response):
        
        event_card = response.selector.css("div.dpEventCard")

        for event in event_card:

            date = event.css("div.dpEventDateTitle::text").get().split(",")
            month, _ = date[0].split()
            year = date[1].lstrip()
            day = date[2].lstrip()
            name = event.css("div.dpEventCardInfoTitle::text").get()
            starts = re.findall("\d+:\d+", event.css("div::text")[-4].get())
            ends = re.findall("\d+:\d+", event.css("div::text")[-2].get())

            ekadashi_item = EkadasiItem(
                month = month,
                year = year,
                day = day,
                name = name,
                starts = starts,
                ends = ends
            )

            yield ekadashi_item
