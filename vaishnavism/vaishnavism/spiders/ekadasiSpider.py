import re
import scrapy
from ..items import EkadasiItem
from .helpers import MONTH_2_NUMBER


class EkadasiSpider(scrapy.Spider):

    name = "ekadasi_spider"
    
    start_urls = [
        "https://www.drikpanchang.com/vrats/ekadashidates.html?geoname-id=3530597"
    ]


    def parse(self, response):
        
        event_card = response.selector.css("div.dpEventCard")

        for event in event_card:

            date = event.css("div.dpEventDateTitle::text").get().split(",")
            month, day = date[0].split()
            year = date[1].strip()
            name = event.css("div.dpEventCardInfoTitle::text").get()
            starts = re.findall("\d\d:\d\d", event.css("div::text")[-4].get())[0]
            ends = re.findall("\d\d:\d\d", event.css("div::text")[-2].get())[0]

            month = MONTH_2_NUMBER[month]

            event_date = f"{year}-{month}-{day}"

            ekadashi_item = EkadasiItem(
                name = name,
                description = "",
                country = "Mexico",
                event_date = event_date,
                starts = starts,
                ends = ends
            )

            yield ekadashi_item