<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [参见问题](#参见问题)

<!-- /code_chunk_output -->

# 参见问题

1. 转发和重定向的区别

**转发**

1. 地址栏不发生变化，显示的是上一个页面的地址
2. 请求次数：只有 1 次请求
3. 根目录：http://localhost:8080/项目地址/，包含了项目的访问地址
4. 请求域中数据不会丢失

**重定向**

1. 地址栏：显示新的地址
2. 请求次数：2 次
3. 根目录：http://localhost:8080/ 没有项目的名字
4. 请求域中的数据会丢失，因为是 2 次请求
