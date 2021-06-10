from typing import Optional
import time

from fastapi import FastAPI

from celery_test.schema import Mandelbrot
from celery_test.tasks import mandelbrot

app = FastAPI(docs_url="/")


@app.post("/create_task", summary="创建任务")
def create_task(param: Mandelbrot):
    task_id = str(int(time.time() * 1000))
    result = mandelbrot.apply_async(task_id=task_id, kwargs=param.dict())

    return {"task_id": result.id}
