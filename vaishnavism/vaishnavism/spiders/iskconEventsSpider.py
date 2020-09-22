import scrapy
from ..items import IskconEventItem



class iskconCalendarSpider(scrapy.Spider):
   
    name = "iskcon_calendar"

    start_urls = [
        "https://www.drikpanchang.com/iskcon/iskcon-event-calendar.html"
    ]

    def parse(self, response):
        
        events = response.selector.css("div.dpEventInfo")
        
        for event in events:
            name = event.css("div.dpEventName::text").get()
            date = event.css("div.dpEventGregDate::text").get()
            event_item = IskconEventItem(
                name = name,
                date = date
            )
            yield event_item