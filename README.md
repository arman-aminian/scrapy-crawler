# scrapy-crawler
A Scrapy crawler for https://www.tgju.org fetching records daily and stores them in MongoDB database.

## Customization
You can customize the fetch time by changing the values in __.env__ :<br>
```
TIMEZONE='Asia/Tehran'
SCHEDULE_HOUR=23
SCHEDULE_MINUTE=30
```
## How to run
```
pip3 install -r requirements.txt<br>
python3 -m TgjuCrawler.scheduler
```
