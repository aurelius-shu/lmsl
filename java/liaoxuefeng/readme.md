# Spring 开发

## IoC 容器

### IoC 原理

`IoC`，`Inversion of Control`，控制反转，即组件的创建、配置等控制转移到了 IoC 容器中，应用程序只需要直接使用已经装配到 `IoC` 容器的组件；
依赖注入，直接持有依赖的对象，而不是重新 new 一个该对象
无侵入容器，不需要事先特定接口

`ApplicationContext ` IoC 容器实例

Spring还提供另一种IoC容器叫`BeanFactory`，使用方式和`ApplicationContext`类似，工厂模式

`BeanFactory`的实现是按需创建，即第一次获取Bean时才创建这个Bean，而`ApplicationContext`会一次性创建所有的Bean。实际上，`ApplicationContext`接口是从`BeanFactory`接口继承而来的，并且，`ApplicationContext`提供了一些额外的功能，包括国际化支持、事件和通知机制等。通常情况下，我们总是使用`ApplicationContext`，很少会考虑使用`BeanFactory`

## 使用 AOP

`AOP`，`Aspect Oriented Programing`，面向切面编程，通过动态代理，在组件原有逻辑基础上添加额外处理

### AOP 避坑指南

1. 访问被注入的 Bean 时，总是调用方法而非直接访问字段
2. 编写Bean时，如果可能会被代理，就不要编写 public final方法

Java 编译器在发现构造方法中没有 super() 时，会自动加上；
如果直接构造字节码，一个类的构造方法中不一定要调用 super()；Spring 通过CGLIB 构造的 Proxy 类就是如此；

在 $$EnhancerBySpringCGLIB 类中不会执行成员变量的赋值语句；
proxy 的目的是代理方法，成员变量的初始化时在构造函数中完成的
