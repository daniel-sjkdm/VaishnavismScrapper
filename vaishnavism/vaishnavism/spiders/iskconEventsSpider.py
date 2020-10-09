import scrapy
from ..items import IskconEventItem
from .helpers import MONTH_2_NUMBER, DAY_2_NUMBER


class iskconCalendarSpider(scrapy.Spider):
   
    name = "iskcon_events_spider"

    start_urls = [
        "https://www.drikpanchang.com/iskcon/iskcon-event-calendar.html"
    ]

    def parse(self, response):
        
        events = response.selector.css("div.dpEventInfo")
        
        for event in events:
            name = event.css("div.dpEventName::text").get()
            date = event.css("div.dpEventGregDate::text").get()
            date = [ datefield.lstrip() for datefield in date.split(",") ]
            month, day = date[0].split()
            year = date[1]

            month = MONTH_2_NUMBER[month]

            event_date = f"{year}-{month}-{day}"
            description = ""

            event_item = IskconEventItem(
                name = name,
                description = description,
                event_date = event_date
            )
            yield event_item