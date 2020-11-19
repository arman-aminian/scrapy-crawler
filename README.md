# scrapy-crawler
A Scrapy crawler for https://www.tgju.org <br>
Records will be stored using mongodb<br>
Records will be updated daily<br>
## Customization
You can customize the update time in .env :<br>
**TIMEZONE='Asia/Tehran'**<br>
**SCHEDULE_HOUR=23**<br>
**SCHEDULE_MINUTE=30**<br>

## How to run
pip3 install -r requirements.txt<br>
python3 -m TgjuCrawler.scheduler
