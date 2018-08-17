import threading
import time

def sleeper(n, name):
    print(f"hi {name}, i'm sleep")
    time.sleep(n)
    print(f"{name} i'm get up")

t = threading.Thread(target=sleeper, name="thread1", args=(2, 'Thread1'))

thread_list = list()

start = time.time()

for i in range(5):
    t = threading.Thread(target=sleeper, name=f"thread{i}", args=(5, f"Thread{i}"))

    thread_list.append(t)
    t.start()
    print(f"{t.name}")

for t in thread_list:
    t.join()

end = time.time()

print(f'all thread done, time: {end - start}')