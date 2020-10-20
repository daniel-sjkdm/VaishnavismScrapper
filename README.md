# Vaishnavism Scrapper

This project is a web scrapper made with python and the module _scrapy_ to fecth import dates from the Vaishnavism like:

+ Iskcon events
+ Ekadasi dates (by country, since the fasting time is different and Mexico is the default one)

Until now, this are the kind of events fetched but I'd like to grow this project.

When the data is fetched it's automatically inserted to a Postgresql database hosted at Heroku.

This project is the data recolection tool that's used by another repository, see: https://github.com/daniel-sjkdm/VaishnavismNotifyTBot.


## Run the scrapper

1. Create virtualenv
  ```
  $ python3 -m venv venv 
  ```

2. Install dependencies
  ```
  $ pip install -r requirements.txt
  ```
  
 3. Run any of the following scrappers:
  ```
  $ scrapy crawl <spider> > ekadsi.json
  ```
  * Where spider is: ekadasi_spider or iskcon_events_spider
  
  
 The output files produced can be found at vaishnavism/vaishnavism/data.
 
 
 
