<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Install on Mac](#install-on-mac)
- [Reference](#reference)

<!-- /code_chunk_output -->

# Install on Mac

```shell
# 安装最新 podman
brew install podman
brew upgrade podman

# 创建 podman 的符号链接 - 无效
ln -s podman docker
# alias 重命名 podman -> docker
vi .zprofile
## alias docker='podman'

# 启动 podman VM
## 安装 fedora-coreos 作为 VM
podman machine init
## Error: exec: "xzcat": executable file not found in $PATH
### 缺少 xz
### brew install xz
### brew link xz
## 启动 podman VM
podman machine start
## 停止 VM
podman machine stop
## 列举 VM
podman machine list
## 删除 VM
podman machine rm
## 通过 SSH 进入 VM
podman machine ssh

# 管理 podman
podman system --help
podman system info
podman system connection list
podman system df
```

# Reference

[MacOS 安装 Podman4.0 替代 Docker](https://zhuanlan.zhihu.com/p/474965478)
