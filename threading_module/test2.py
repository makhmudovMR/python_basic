import threading
import time
from queue import Queue

q = Queue()

class MyThread(threading.Thread):

    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q


    def run(self):
        while True:
            print(self.q.get())


for i in range(4):
    q.put(i)

t1 = MyThread("Well", q)
t2 = MyThread("Lamar", q)
t3 = MyThread("Nisan", q)
t4 = MyThread("David", q)

t1.start()
t2.start()
t3.start()
t4.start()