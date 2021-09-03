# beta

## 20210826

### Spring

特点：

1. 降低代码解耦，组件的创建和使用分离，组件的创建、注入（相互引用）、配置转交给 IoC 容器
2. AOP 编程支持，解耦，重用，不修改源码添加功能到主干

#### IoC

```
Inversion of Control - 控制反转
Dependency Inj·ection - 依赖注入
```

1. 实现原理
   XML/注解解析 + 工厂模式 + 反射

2. 作用域
   singleton, prototype, request, session

3. 生命周期
   construct, set, postconstruct, getbean, predestroy

4. 循环依赖

   - 构造器注入无法解决循环依赖，BeanCurrentlyCreationException
   - setter 注入避免循环依赖
   - singleton 支持循环依赖，prototype 不支持

5. 三级缓存

   - A 创建需要 B，现将 A 放入三级缓存，去创建 B
   - B 创建需要 A，去 一、二、三级缓存一次查找 A，在 三级缓存找到 A，将 A 注入 B，并将 A 从三级缓存移到二级缓存
   - B 创建完成，直接放入一级缓存，返回 A 的创建，将一级缓存中的 B 注入 A，A 完成创建，将 A 从二级缓存移到一级缓存

#### AOP

1. 实现原理
   JVM 动态代理、CGLIB 动态代理
2.

#### DataBase

#### Web

#### JMX

#### Question
