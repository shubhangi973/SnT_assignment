import threading
import time

start_time = time.time()
global stop
def loop():
    i=0
    while (stop):
        print(i)
        i=i+1
 
stop = 1
thread = threading.Thread(target = loop)
thread.start()
time.sleep(1)
stop = 0
thread.join()
print('Terminated')
print("%s second(s)" % (time.time() - start_time))
