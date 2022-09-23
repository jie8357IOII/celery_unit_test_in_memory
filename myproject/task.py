import celery
from celery import shared_task

class MyTask(celery.Task):
    def before_start(self, task_id, args, kwargs):
        print(f'{task_id} started: {args} {kwargs}')

    def on_success(self, retval, task_id, args, kwargs):
        print(f"{task_id} succeeded: {retval}, {args}, {kwargs}")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f"{task_id} failed: {exc}, {args}, {kwargs}, {einfo}")

@shared_task(base=MyTask)
def add(x, y):
    return x + y
