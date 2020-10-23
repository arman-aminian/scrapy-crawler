import os

from apscheduler.schedulers.blocking import BlockingScheduler

from decouple import config

_ONE_DAY_IN_SECONDS = 60 * 60

crawl_command = 'scrapy crawl {}'

before_start_targets = ['sekee', 'dollar', 'geram18']
on_targets = ['last_sekee', 'last_dollar', 'last_geram18']


def crawl_job(targets):
    for i in targets:
        os.system(crawl_command.format(i))


TIMEZONE = config('TIMEZONE', default='Asia/Tehran', cast=str)
SCHEDULE_HOUR = config('SCHEDULE_HOUR', default=3, cast=int)
SCHEDULE_MINUTE = config('SCHEDULE_MINUTE', default=10, cast=int)


sched = BlockingScheduler(timezone=TIMEZONE)
sched.add_job(crawl_job, 'cron', hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE, args=[on_targets])

if __name__ == '__main__':
    try:
        crawl_job(before_start_targets)
        sched.start()
    except KeyboardInterrupt:
        pass
