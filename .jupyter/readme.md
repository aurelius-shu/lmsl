<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [jupyter 环境搭建](#jupyter-环境搭建)

<!-- /code_chunk_output -->

# jupyter 环境搭建

```shell
# 升级 pip
pip install --upgrade pip

# 安装 Jupyter Notebook
pip install jupyter

# 安装 工具 jupyter_contrib_nbextensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# 安装 样式 jupyterthemes
pip install --no-dependencies jupyterthemes
pip install lesscpy
jt -t grade3 -N -kl -T

# 运行 Jupyter Notebook
jupyter notebook --port <port_number>
```
