import threading
import time


def sleeper(n, name):
    print(f"hi {name}, i'm sleep")
    time.sleep(n)
    print(f"{name} i'm get up")

start = time.time()

for i in range(5):
    sleeper(2, str(i))

end = time.time()

print(end-start)