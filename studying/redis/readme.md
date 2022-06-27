<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [基础应用 å](#基础应用-å)
  - [key 操作](#key-操作)
  - [数据类型](#数据类型)
  - [其他操作](#其他操作)
- [原理](#原理)
- [集群](#集群)
- [拓展](#拓展)
- [源码](#源码)
- [docker](#docker)
- [参考资料](#参考资料)

<!-- /code_chunk_output -->

# 基础应用 å

## key 操作

**flushall**

清空整个 Redis 服务器的数据(删除所有数据库的所有 key )

**flushdb**

清空当前数据库中的所有 key

## 数据类型

## 其他操作

# 原理

# 集群

# 拓展

# 源码

# docker

```shell
docker run --name redis -d -p 6379:6379 redis redis-server --appendonly yes
```

```python
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'Aurelius')
print(redis.get('name'))
```

# 参考资料

1. 《[Redis 深度历险]()》
