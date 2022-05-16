from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api
from news_api.views import home


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_api, 'interval', minutes=5)
    scheduler.start() 