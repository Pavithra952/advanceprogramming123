from threading import Thread
from queue import queue
import time
class producer():
    def __init__(self):
        self.q=Queue()
    def produce(self):
        for i range(1,6):
            print('item produced',i)
            self.q.put(i)
            time.sleep(1)
class Consumer():
    def __init__(self,prod):
        for i in range(1,6):
            print('item recievd',self.prod.q.get(i))
p=Producer()
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
print(t1.isDaemon())
t1.daemon=True
t1.start()
t1.join
t2.start()



