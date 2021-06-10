#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import timedelta

from celery import Celery


app = Celery("demo")

app.conf.update(
    broker_url="redis://redis:6379/0",
    result_backend="redis://redis:6379/1",
    imports="celery_test.tasks",
    timezone='Asia/Shanghai',
    task_compression="gzip",
    result_compression="gzip",
    result_expires=timedelta(days=1).seconds,
    task_time_limit=timedelta(hours=1).seconds,
    task_soft_time_limit=timedelta(minutes=30).seconds,
    worker_prefetch_multiplier=1,
    worker_max_memory_per_child=1200,  # 12MB
    worker_send_task_events=True,
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
