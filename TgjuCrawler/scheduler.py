import os

from apscheduler.schedulers.blocking import BlockingScheduler

from decouple import config

_ONE_DAY_IN_SECONDS = 60 * 60

crawl_command = 'scrapy crawl {}'


def before_start():
    os.system(crawl_command.format('sekee'))
    os.system(crawl_command.format('dollar'))
    os.system(crawl_command.format('geram18'))


def crawl_job():
    os.system(crawl_command.format('last_sekee'))
    os.system(crawl_command.format('last_dollar'))
    os.system(crawl_command.format('last_geram18'))


TIMEZONE = config('TIMEZONE', default='Asia/Tehran', cast=str)
SCHEDULE_HOUR = config('SCHEDULE_HOUR', default=3, cast=int)
SCHEDULE_MINUTE = config('SCHEDULE_MINUTE', default=10, cast=int)


sched = BlockingScheduler(timezone=TIMEZONE)
sched.add_job(crawl_job, 'cron', hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE)

if __name__ == '__main__':
    try:
        before_start()
        sched.start()
    except KeyboardInterrupt:
        pass
