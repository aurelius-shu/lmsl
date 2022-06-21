import os

print(f'Process {os.getpid()} start...')
pid = os.fork()
if pid = 0:
    print(f'child process {os.getpid()}, parent is {os.getppid()}')
else:
    print(f'process {os.getpid()} created a child process {pid}')