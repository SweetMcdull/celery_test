#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from celery.utils.log import get_task_logger

from celery_test import celery_app

logger = get_task_logger(__name__)


@celery_app.task(bind=True, name='mandelbrot')
def mandelbrot(self, *, n_max, some_threshold, nx, ny):
    task_id = self.request.id
    logger.info(f"任务:{task_id}开始...")
    xs = np.linspace(-2, 1, nx)
    ys = np.linspace(-1.5, 1.5, ny)
    mandelbrot_set = np.zeros((len(xs), len(ys)))
    for i in range(len(xs)):
        for k in range(len(ys)):
            x = xs[i]
            y = ys[k]
            c = x + 1j * y
            z = c
            is_inside = 1
            for j in range(n_max):
                z = z ** 2 + c
                if abs(z) >= some_threshold:
                    is_inside = 0
                    break
            mandelbrot_set[i, k] = is_inside

    result = mandelbrot_set.tolist()
    return result
