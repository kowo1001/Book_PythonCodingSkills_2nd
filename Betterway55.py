from collections import deque
from threading import Lock

class MyQueue:
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()
        
from threading import Thread
import time

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

def run(self):
    while True:
        self.polled_count += 1
        try:
            item = self.in_queue.get()
        except IndexError:
            time.sleep(0.01) # 할 일이 없음
        else:
            result = self.func(item)
            self.out_queue.put(result)
            self.work_done += 1

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()

done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]


from queue import Queue

my_queue = Queue()
def consumer():
    print('소비자 대기')
    my_queue.get() # 다음에 보여줄 put()이 실행된 다음에 실행된다
    print('소비자 완료')
    
thread = Thread(target=consumer)
thread.start()

print('생산자 데이터 추가')
my_queue.put(object()) # 앞에서 본 get()이 실행되기 전에 실행된다
print('생산자 완료')
thread.join()



        

