from multiprocessing import Pool
import os, time, random


def proc(name):
    print(f'run task {name} ({os.getpid()})')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f'task {name} runs: {end-start}')


if __name__ == "__main__":
    print(f'parent process {os.getpid()}')
    p = Pool(4)
    for i in range(5):
        p.apply_async(proc, args=(i, ))
    print('waiting for all subprocesses done...')
    p.close()
    p.join()
    print('all subprocess done.')
