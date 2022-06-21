<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [常见命令](#常见命令)
- [docker](#docker)
- [示例](#示例)

<!-- /code_chunk_output -->

# 常见命令

**flushall**

清空整个 Redis 服务器的数据(删除所有数据库的所有 key )

**flushdb**

清空当前数据库中的所有 key

# docker

```shell
docker run --name redis -d -p 6379:6379 redis redis-server --appendonly yes
```

# 示例

```python
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'Aurelius')
print(redis.get('name'))
```
