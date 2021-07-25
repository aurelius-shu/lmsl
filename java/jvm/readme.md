# 栈

## Minor GC、Major GC、Full GC

- Partital GC，部分收集
  - Minor GC/Young GC，只针对新生代，会引发 STW
  - Major GC/Old GC，只针对老年代，比 Minor GC 慢 10 倍以上
- Full GC，整堆收集

## 内存分配策略
