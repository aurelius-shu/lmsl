from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print(f'process to write: {os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'put {value} to queue...')
        q.put(value)
        time.sleep(random.random())


def read(q):
    print(f'process to read: {os.getpid()}')
    while True:
        value = q.get(True)
        print(f'get {value} from queue.')


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    pw.start()
    pr.start()
    pw.join()
    # 写完即可关闭读进程
    pr.terminate()
