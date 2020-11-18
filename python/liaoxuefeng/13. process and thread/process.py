from multiprocessing import Process

import os
import time


def proc(name):
    # time.sleep(5)
    print(f'run child process {name} ({os.getpid()})')


if __name__ == "__main__":
    print(f'parent process {os.getpid()}')
    p = Process(target=proc, args=('test', ))
    print('child process will start.')
    p.start()
    p.join()
    print('child process end.')