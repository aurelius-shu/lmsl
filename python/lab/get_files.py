import os
from typing import MappingView


def get_files(dir, suffix):
    res = []
    print(dir)
    for root, dirs, files in os.walk(dir):
        print('root:')
        print(root)
        print('dirs:')
        print(dirs)
        print('files:')
        print(files)
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    print(res)


# get_files(r'D:\WorkSpace\notebook\lab\udf', '.py')

import os


def pick(obj, suffix):
    if obj.endswith(suffix):
        print(obj)


def scan_path(ph, suffix):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(os.path.join(ph, obj)):
            pick(obj, suffix)
        elif os.path.isdir(obj):
            scan_path(obj)


# scan_path(r'D:\WorkSpace\notebook\lab\udf', '.py')

from glob import iglob


def func(fp, suffix):
    for i in iglob(f'{fp}/**/*{suffix}', recursive=True):
        print(i)


# func(r'D:\WorkSpace\notebook\lab\udf', '.py')


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        size = 0
        while size < len(nums):
            if target - nums[size] in d:
                if d[target - nums[size]] < size:
                    return [d[target - nums[size]], size]
            else:
                d[nums[size]] = size
            size += 1


# solution = Solution()
# print(solution.twoSum([2,7,11,15], 9))

# mulitprocessing.Process
import os
from multiprocessing import Process
import time


def pro_func(name, age, **kwargs):
    for i in range(5):
        print(f'子进程正在运行中，name={name},age={age},pid={os.getpid()}')
        print(kwargs)
        time.sleep(0.2)


# if __name__ == '__main__':
#     p = Process(target=pro_func, args=('小明', 18), kwargs={'m':20})
#     p.start()
#     time.sleep(1)
#     p.terminate()
#     p.join()

import threading, time


def thread():
    time.sleep(2)
    print('子线程结束')


def main():
    t1 = threading.Thread(target=thread)
    t1.setDaemon(True)
    t1.start()
    print('主线程结束')


if __name__ == '__main__':
    main()