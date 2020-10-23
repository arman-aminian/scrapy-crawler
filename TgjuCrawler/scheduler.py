from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from TgjuCrawler.spiders import (tgju_dollar_spider, tgju_last_18geram_spider, tgju_last_dollar_spider,
                                 tgju_last_sekee_spider, tgju_sekee, tgju_18geram_spider)
from decouple import config


_ONE_DAY_IN_SECONDS = 60 * 60
target_spiders = [tgju_last_sekee_spider.TGJUSpider, tgju_last_dollar_spider.TGJUSpider,
                  tgju_last_18geram_spider.TGJUSpider]
before_spiders = [tgju_sekee.TGJUSpider, tgju_dollar_spider.TGJUSpider, tgju_18geram_spider.TGJUSpider]


def crawl_job(targets):
    print('started crawling')
    runner = CrawlerRunner(get_project_settings())
    for spid in targets:
        runner.crawl(spid)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run(0)
    print('done crawling')


TIMEZONE = config('TIMEZONE', default='Asia/Tehran', cast=str)
SCHEDULE_HOUR = config('SCHEDULE_HOUR', default=3, cast=int)
SCHEDULE_MINUTE = config('SCHEDULE_MINUTE', default=10, cast=int)

crawl_job(before_spiders)
sched = BlockingScheduler(timezone=TIMEZONE)
sched.add_job(crawl_job, 'cron', hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE, args=[target_spiders])

if __name__ == '__main__':
    try:
        sched.start()
    except KeyboardInterrupt:
        pass
