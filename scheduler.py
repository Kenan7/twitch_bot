from os import environ

from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore


class SchedulerConfig:
    REDIS_HOST = environ["REDIS_HOST"]
    REDIS_PORT = 6333

    SCHEDULER_JOBSTORES = {
        "default": RedisJobStore(host=REDIS_HOST, port=REDIS_PORT)
    }
    SCHEDULER_EXECUTORS = {
        "default": ThreadPoolExecutor(20),
        "processpool": ProcessPoolExecutor(5),
    }
    SCHEDULER_JOB_DEFAULTS = {
        "coalesce": False,
        "max_instances": 5,
        "misfire_grace_time": 10,
    }

    SCHEDULER_API_ENABLED = True
