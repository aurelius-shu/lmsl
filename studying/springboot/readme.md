# SpringBoot

## SpringBoot 启动过程

1. 创建 SpringApplication
   1. 保存一些信息。
   2. 判定当前应用的类型。ClassUtils。Servlet
   3. bootstrappers：初始启动引导器（List<Bootstrapper>）：去 spring.factories 文件中找 org.springframework.boot.Bootstrapper
   4. 找 ApplicationContextInitializer；去 spring.factories 找 ApplicationContextInitializer
      - List<ApplicationContextInitializer<?>> initializers
   5. 找 ApplicationListener ；应用监听器。去 spring.factories 找 ApplicationListener
      - List<ApplicationListener<?>> listeners
2. 运行 SpringApplication
   1. StopWatch
   2. 记录应用的启动时间
   3. 创建引导上下文（Context 环境）createBootstrapContext()
      - 获取到所有之前的 bootstrappers 挨个执行 intitialize() 来完成对引导启动器上下文环境设置
   4. 让当前应用进入 headless 模式。java.awt.headless
   5. 获取所有 RunListener（运行监听器）【为了方便所有 Listener 进行事件感知】
      - getSpringFactoriesInstances 去 spring.factories 找 SpringApplicationRunListener.
   6. 遍历 SpringApplicationRunListener 调用 starting 方法；
      - 相当于通知所有感兴趣系统正在启动过程的人，项目正在 starting。
   7. 保存命令行参数；ApplicationArguments
   8. 准备环境 prepareEnvironment（）;
      - 返回或者创建基础环境信息对象。StandardServletEnvironment
      - 配置环境信息对象。
        - 读取所有的配置源的配置属性值。
      - 绑定环境信息
      - 监听器调用 listener.environmentPrepared()；通知所有的监听器当前环境准备完成
   9. 创建 IOC 容器（createApplicationContext（））
      - 根据项目类型（Servlet）创建容器，
      - 当前会创建 AnnotationConfigServletWebServerApplicationContext
   10. 准备 ApplicationContext IOC 容器的基本信息 prepareContext()
       - 保存环境信息
       - IOC 容器的后置处理流程。
       - 应用初始化器；applyInitializers；
         - 遍历所有的 ApplicationContextInitializer 。调用 initialize.。来对 ioc 容器进行初始化扩展功能
         - 遍历所有的 listener 调用 contextPrepared。EventPublishRunListenr；通知所有的监听器 contextPrepared
       - 所有的监听器 调用 contextLoaded。通知所有的监听器 contextLoaded；
   11. 刷新 IOC 容器。refreshContext
       - 创建容器中的所有组件（Spring 注解）
   12. 容器刷新完成后工作？afterRefresh
   13. 所有监听 器 调用 listeners.started(context); 通知所有的监听器 started
   14. 调用所有 runners；callRunners()
       - 获取容器中的 ApplicationRunner
       - 获取容器中的 CommandLineRunner
       - 合并所有 runner 并且按照@Order 进行排序
       - 遍历所有的 runner。调用 run 方法
   15. 如果以上有异常，
       - 调用 Listener 的 failed
   16. 调用所有监听器的 running 方法 listeners.running(context); 通知所有的监听器 running
   17. running 如果有问题。继续通知 failed 。调用所有 Listener 的 failed；通知所有的监听器 failed

## Listeners

1. ApplicationContextInitializer
   org.springframework.context.ApplicationContextInitializer
2. ApplicationListener
   org.springframework.context.ApplicationListener
3. SpringApplicationRunListener
   org.springframework.boot.SpringApplicationRunListener

## 配置加载

prepareEnvironment(listeners, applicationArguments)

listeners.environmentPrepared(environment)

ConfigFileApplicationListener

## EnvironmentPostProcessor

