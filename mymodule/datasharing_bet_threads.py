import time
from threading import Thread
from queue import Queue
class Producer():
    def __init__(self):
        self.q=Queue()
    def produce(self):
        for i in range(1,6):
            print('item produced',i)
            self.q.put(i)
            time.sleep(1)
class Consumer():
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        for i in range(1,6):
            print('item received',self.prod.q.get(i))
p=Producer()
c=Consumer(p)



