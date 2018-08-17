import queue
import threading
import time


def putting_pread(q):
    while True:
        print("start thread")
        time.sleep(5)
        q.put(5)
        print("sup sumthing")


q = queue.Queue()
t = threading.Thread(target=putting_pread, args=(q,), daemon=True)
t.start()


q.put(0)
print(q.get(), "firts item")
print('-----')
print(q.get())
