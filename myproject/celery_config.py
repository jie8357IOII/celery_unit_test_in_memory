from celery import Celery

# app = Celery('celerytest', backend='cache+memory://', broker='memory://',)
app = Celery('celerytest',)
