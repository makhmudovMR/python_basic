import threading
import time

def sleeper(n, name):
    print(f"hi {name}")
    time.sleep(n)
    print('yeh')

t = threading.Thread(target=sleeper, name="thread1",args=(3,"jhon"))
t.start()
# t.join()

print('Main thread')