<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [自定义配置](#自定义配置)
  - [安装插件](#安装插件)
  - [设置主题](#设置主题)
  - [安装字体](#安装字体)
  - [设置注释](#设置注释)
  - [设置编码](#设置编码)
  - [自动引入依赖](#自动引入依赖)
  - [设置大小写匹配](#设置大小写匹配)
  - [设置注释缩进](#设置注释缩进)
  - [设置自动编译](#设置自动编译)
  - [快捷键](#快捷键)
  - [模板](#模板)

<!-- /code_chunk_output -->

# 自定义配置

## 安装插件

- Material Theme UI
- Statistic
- Alibaba p3c
- Key promoter

## 设置主题

- GitHub Dark(Material)
- Features -> Large Tool Windows(Experimental)

## 安装字体

- Consolas

## 设置注释

- File and Code Templates

```java
/**
 * @author cm.huang@aftership.com (Aurelius Huang)
 * @description
 * @createTime ${YEAR}-${MONTH}-${DAY} ${TIME}
 * @since 1.0.0
 */
```

## 设置编码

- encoding: UTF-8

## 自动引入依赖

- Editor -> General -> Auto Import
  Add unambiguous imports on the fly：自动导入不明确的结构
  Optimize imports on the fly：自动帮我们优化导入的包，

## 设置大小写匹配

- Editor -> General -> Code Completion
  - Match case: 去掉勾选

## 设置注释缩进

- Editor -> Code Style -> Java -> Code Generation
  - Line command at first column
  - Add a space at comment start

## 设置自动编译

- Compiler
  - Build project automatically
  - Compile independent modules in parallel

## 快捷键

## 模板

- psvm & main -> public static void main
- sout -> System.out.println
- fori -> for int
- list.for -> for item
- ifn -> if(args == null)
- inn -> if(args != null)
- prsf -> private static final
- psf -> public static final
- psfi -> public static final int
- psfs -> public static final String
