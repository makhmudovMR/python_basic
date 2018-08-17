import threading
import time

class MyThread(threading.Thread):

    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args


    def run(self):
        print(f"{self.number} has started")
        self.func(*self.args)
        print(f"{self.number} has finished")


def double(number, cycle):
    for i in range(cycle):
        number += number
    print(number)


threads_list = list()

for i in range(50):
    t = MyThread(number=i+1, func=double, args=[i, 3])
    t.start()
    threads_list.append(t)

for t in threads_list:
    t.join()