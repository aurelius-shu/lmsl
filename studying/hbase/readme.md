<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [简介](#简介)
- [安装部署](#安装部署)
- [Shell 命令](#shell-命令)
- [API](#api)
- [架构原理](#架构原理)
  - [逻辑架构](#逻辑架构)
  - [数据模型](#数据模型)
  - [写流程](#写流程)
    - [MemStore Flush](#memstore-flush)
  - [读流程](#读流程)
- [优化](#优化)
- [不足](#不足)
- [参考资料](#参考资料)

<!-- /code_chunk_output -->

# 简介

# 安装部署

# Shell 命令

# API

# 架构原理

## 逻辑架构

## 数据模型

## 写流程

### MemStore Flush

条件：
资源充足：128 MB
资源不充足：Lower Mark & High Marker
资源太充足：1 小时强制刷写
写效率太低：WAL 文件超过 hbase.regionserver.max.logs(32)

1. 小文件问题
2. 数据洪峰
3. 避免

## 读流程

# 优化

# 不足

1. 逻辑结构
2. 物理存储结构
3. 数据模型

# 参考资料
