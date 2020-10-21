from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from TgjuCrawler.spiders import tgju_spider
from decouple import config


def crawl_job():
    print('started crawling')
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(tgju_spider.TGJUSpider)
    d.addBoth(lambda _: reactor.stop())
    print('done crawling')
    reactor.run(0)


TIMEZONE = config('TIMEZONE', default='Asia/Tehran', cast=str)
SCHEDULE_HOUR = config('SCHEDULE_HOUR', default=3, cast=int)
SCHEDULE_MINUTE = config('SCHEDULE_MINUTE', default=10, cast=int)

sched = BlockingScheduler(timezone=TIMEZONE)
sched.add_job(crawl_job, 'cron', hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE)

try:
    sched.start()
except KeyboardInterrupt:
    pass
