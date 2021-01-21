import logging as log
import threading

from apscheduler.schedulers.background import BackgroundScheduler

from bot import TwitchBot
from scheduler import SchedulerConfig
from tasks import data_mapper

try:
    sched = BackgroundScheduler(
        job_stores=SchedulerConfig.SCHEDULER_JOBSTORES,
        job_defaults=SchedulerConfig.SCHEDULER_JOB_DEFAULTS,
        executors=SchedulerConfig.SCHEDULER_EXECUTORS,
    )

    sched.start()
    threading.Thread(
        target=sched.add_job(
            data_mapper,
            trigger="interval",
            seconds=10,
            id="job_periodic",
            replace_existing=True,
        )
    ).start()

    bot = TwitchBot()
    threading.Thread(target=bot.run()).start()
except:
    print("Error: unable to start thread")
