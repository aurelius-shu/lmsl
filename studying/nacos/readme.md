# Nacos

## SpringBoot Starter

1. ClientWorker 不停获取 Config Service 的 md5-version 并与本地比较
2. md5-version 更新时，获取 Config Service 的 configs，并(CacheData)通知 listener 处理 configs -> NacosContextRefresher listener.innerReceive
3. ApplicationContext(AbstractApplicationContext) 发布一个 NacosContextRefresher 的 RefreshEvent
   1. AbstractApplicationContext 通过 ApplicationEventMulticaster(SimpleApplicationEventMulticaster) 广播 multicast applicationEvent
   2. RefreshEventListener 处理 handle(RefreshEvent) -> ContextRefresher refreshEnvironment(extract, addConfigFilesToEnvironment, EnvironmentChangeEvent -> scope.refreshAll)
      1. ContextRefresher extract 16 种环境下 properties ->
      2. ContextRefresher addConfigFilesToEnvironment
         1. BootstrapApplicationListener onApplicationEvent(重走启动流程)
         2. ConfigFileApplicationListener onApplicationEnvironmentPreparedEvent -> load x 9
            1. YamlPropertySourceLoader load x 2
            2. NacosPropertySourceLocator locate -> loadApplicationConfiguration -> loadNacosDataIfPresent -> loadNacosPropertySource
            3. NacosPropertySourceBuilder build -> loadNacosData -> parseNacosData
            4. YamlPropertySourceLoader load (解析 configs)
         3. PropertySourceBootstrapConfiguration initialize
            1. PropertySourceLocator locateCollection
            2. PropertySourceBootstrapConfiguration -> setLogLevels
      3. ContextRefresher changes 拿到变更 keys -> publishEvent(EnvironmentChangeEvent(keys))
         1. AbstractApplicationContext publishEvent
         2. SimpleApplicationEventMulticaster multicast
         3. ConfigurationPropertiesRebinder -> onApplicationEvent -> rebind()
            1. BeanPostProcessor bind -> configurationPropertiesBinder.bind(target)
      4. ContextRefresher RefreshScope refreshALl -> publishEvent(RefreshScopeRefreshedEvent)

## SpringBoot run 过程

prepareContext 时将 PropertySourceLoader 添加到 PropertySourceRepository
running 时 NacosContextRefresher onApplicationEvent -> registerNacosListener

## PropertySource 相关组件

- RefresherEventListener（监听 RefreshEvent，调用 ContextRefresher.refresh 处理 Event）
- ContextRefresher(刷新环境， Scope)
    - refreshEnvironment -> EnvironmentChangeEvent
    - scope.refreshAll -> RefreshScopeRefreshedEvent -> RefreshScope -> eagerlyInitialize
- (Nacos)ContextRefresher(注册 Listener: registerNacosListenersForApplications)
  - 构造一个 ConfigListenter，其中通过 applicationContext 发布该 ContextRefresher（RefreshEvent）到 SimpleApplicationEventMulticaster
  - 注册 ConfigListenter 到 ConfigService，当 ConfigService 接收到变化配置时触发 SimpleApplicationEventMulticaster 的 multicastEvent 处理

- PropertySourceBootstrapConfiguration(自动注入)
  - 注入 PropertySourceLocator
  - 通过 PropertySourceLocator 获取 PropertySource
  - 将 PropertySource 转为 BootstrapPropertySource
  - 将 BootstrapPropertySource 插入到 environment 的 PropertySources 集合中
- PropertySourceLocator(加载 PropertySource: locateCollection)
  - 持有 PropertySourceBuilder
  - 通过 PropertySourceBuilder 构建 PropertySource
  - 将 PropertySource 添加到 CompositePropertySource 并返回
- PropertySourceBuilder(构建 PropertySource）
  - 通过 ConfigService 读取服务端配置资源 configValue
  - 通过 ConfigParserHandler 解析 configValue 获取 PropertySource
  - 通过 PropertySourceRepository 收集管理 PropertySource
- ConfigParserHandler(单例, parseNacosData: configValue -> PropertySource)
  - 加载 SpringFactories 中所有的 PropertySourceLoader
  - 挨个遍历 PropertySourceLoader 尝试解析解析封装 PropertySource(loader.load)

- PropertySource(Map)，应用于 ConfigurationProperties
- PropertySourceLoader(从各类格式(JSON/XML)资源加载 PropertySource(Map))
- ConfigUtils(选择编码选择)
