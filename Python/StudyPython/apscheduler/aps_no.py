# coding=utf-8
"""
Demonstrates how to use the background scheduler
to schedule a job that execute on 3 second intervals
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print 'Tick! The time is: %s' % datetime.now()


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'date', run_date='2017-12-02 00:29:00')
    scheduler.start()
    print 'Press Ctrl+(0) to exit'.format('Break' if os.name == 'nt' else 'C')

    try:
        # This is here to sumulate application activity (which keeps the main thread alive)
        while True:
            time.sleep(2)
            print 'sleep!'
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done is possible
        scheduler.shutdown()
        print 'Exit The Job!'
