from apscheduler.schedulers.background import BackgroundScheduler # apscheduler package
from . import email


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(email.job, 'interval', minutes=1)
    scheduler.start()