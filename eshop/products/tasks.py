from celery import task
from celery.task.base import periodic_task, PeriodicTask
from celery.schedules import crontab
from django.core.mail import send_mail


@task
def send_order(email, order):
    send_mail(
        'Order',
        '{} order {}'.format(email.encode('utf-8'), order.encode('utf-8')),
        'eshop@example.org',
        ['admin@example.org']
    )


# @periodic_task(run_every=10.)
@periodic_task(run_every=crontab(minute='*', hour='*'))
def hello():
    print "hello"


class MyPeriodicTask(PeriodicTask):
    def __init__(self):
        pass

    run_every = 10.

    def run(self):
        print "my periodic task"
