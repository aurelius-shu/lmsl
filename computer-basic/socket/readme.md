# Socket

## I/O 模型

**I/O 的两个阶段**

1. wait for data（等待数据从网络到达内核的缓冲区）
2. copy data from kernel to user

**recvfrom**

用于接收 Socket 传来的数据

### 阻塞式 I/O

1. application 向 kernel 发起 recvfrom 的 sys.call
2. kernel `阻塞`，完成 wait 和 copy 两个阶段后，返回 OK

### 非阻塞式 I/O

1. application 以轮询方式向 kernel 发起 recvfrom 的 sys.call，
2. 处于 wait 阶段时，kernel 直接返回当前 wait 阶段状态，非阻塞
3. 处于 copy 阶段时，kernel `阻塞`，执行 copy
4. copy 完成时，kernel 返回 OK

### I/O 复用

1. application 向 kernel 发起 select/poll/epoll 的 sys.call，kernel 从多个 Sokect 中返回一个 wait 已完成的 Sokect，单 Socket `阻塞`，多 Socket `复用`且`非阻塞`
2. application 向 kernel 发起 recvfrom 的 sys.call，kernel `阻塞`，执行 copy
3. copy 完成时，kernel 返回 OK

### 信号驱动 I/O

1. application 向 kernel 发起 sigaction 的 sys.call，并启用 signal hander 监听，kernel 直接返回，并在 wait 已完成时再次发送 SIGIO 信号，`非阻塞`
2. application 的 signal handler 接收到 SIGIO 信号后，调用 recvfrom ，kernel `阻塞`，执行 copy
3. copy 完成时，kernel 返回 OK

### 异步 I/O

1. application 向 kernel 发起 aio_read，并启用 signal handler 监听，kernel 直接返回，`非阻塞`
2. wait，copy 完成后，kernel 返回完成信号，`非阻塞`

### 五大 I/O 比较

1. 阻塞式 I/O 阻塞 wait, copy
2. 非阻塞 I/O 阻塞 copy
3. I/O 复用 阻塞 wait, copy
4. 型号驱动 I/O 阻塞 copy
5. 异步 I/O 无阻塞
6. 信号驱动 I/O 比非阻塞 I/O 的轮询方式 CPU 利用率更高

`同步 I/O`: 阻塞式 I/O、非阻塞式 I/O、I/O 复用、信号驱动 I/O

## I/O 复用模式

### select

监听一组文件描述符，等待描述符称为就绪状态，从而完成 I/O

1. 会修改描述符
2. 描述符数组默认长度 1024
3. 每次调用需要复制描述符到 kernel，速度较慢
4. 几乎支持所有系统

### poll

与 select 类似

1. 不会修改描述符
2. 描述符数组长度不受限制
3. 提供更多事务类型，
4. 每次调用需要复制描述符到 kernel，速度较慢
5. 支持较新系统

### epoll

只需将描述拷贝进 kernel 一次，不需要通过轮询获得事件完成的描述符

1. 仅适用于 Linux
2. 比 select 和 poll 灵活，没有描述符数量限制
3. 对多线程更友好，另一个线程关闭调用的描述符时，不会导致不确定结果

#### 工作模式

1. LT(level trigger)
   检测到完成的描述符并通知进程，进程可以不立即处理该事件，下次 epoll_wait 调用还会通知进程，支持阻塞与非阻塞
2. ET(edge trigger)
   检测到完成的描述符并通知进程，进程必须立即处理该事件，下次 epoll_wait 调用不会通知进程，只支持非阻塞
   减少了重复通知，效率比 LT 高
   避免阻塞读写将其他多个描述符的任务饿死

### 应用场景

1. select: timeout 精度高（微秒），适合实时性要求高的场景，如核反应堆，移植性好，几乎全平台支持
2. poll: 没有描述符限制，适用于实时性要求不高的场景
3. epoll: 1000 个以上描述符，长连接，Linux 平台，短连接不需要使用 epoll，因为 epoll 描述符存储在 kernel，不易调试，且需要频繁调用 epoll_ctl 修改，降低了效率
