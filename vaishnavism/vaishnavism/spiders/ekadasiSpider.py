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

            date = event.css("div.dpEventDateTitle::text").get()
            name = event.css("div.dpEventCardInfoTitle::text").get()
            start = re.findall("\d+:\d+", event.css("div::text")[-4].get())
            end = re.findall("\d+:\d+", event.css("div::text")[-2].get())

            ekadashi_item = EkadasiItem(
                date=date,
                name=name,
                start=start,
                end=end
            )

            yield ekadashi_item