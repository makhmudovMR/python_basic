import threading
import time


class ClockThread(threading.Thread):

    def __init__(self,interval):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval

    def run(self):
        print("The time is %s" % time.ctime())
        time.sleep(self.interval)


t = ClockThread(2)
b = ClockThread(4)
t.start()
b.start()