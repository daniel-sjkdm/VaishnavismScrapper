import os
from itemadapter import ItemAdapter
from .database import Vaishnadb
from .settings import DEBUG

if DEBUG:
    from dotenv import load_dotenv
    load_dotenv()


class VaishnavismPipeline:
    
    dbname = os.getenv('PGDATABASE', None)
    host = os.getenv('PGHOST', None)
    port = os.getenv('PGPORT', None)
    user = os.getenv('PGUSER', None)
    password = os.getenv('PGPASSWORD', None)    

    db = Vaishnadb(dbname, host, port, user, password)


    def process_item(self, item, spider):

        if spider.name == "ekadasi_spider":

            name = item["name"]
            description = item["description"]
            country = item["country"]
            event_date = item["event_date"]
            starts = item["starts"]
            ends = item["ends"]
            
            ekadasi_id = self.db.add_ekadasi(name, description, return_id=True)[0]
            self.db.add_ekadasi_date(ekadasi_id, country, event_date, starts, ends)

        elif spider.name == "iskcon_events_spider":

            name = item["name"]
            description = item["description"]
            event_date = item["event_date"]
            self.db.add_iskcon_event(name, description, event_date)