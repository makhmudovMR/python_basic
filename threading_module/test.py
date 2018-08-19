import threading
import time

class MyThread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name


    def run(self):
        for i in range(10):
            print(self.name + str(i))
            time.sleep(2)


t1 = MyThread("Jhon")
t2 = MyThread("Will")
t3 = MyThread("Frank")


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

for i in range(10):
    print("Maga" + str(i))
    time.sleep(2)

