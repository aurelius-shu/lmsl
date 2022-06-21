# Maven

## Question

- Question 1. 高版本 Maven 阻止不安全（HTTP）的私有仓库地址

```text
Could not transfer artifact com... from/to maven-default-http-blocker (http://0.0.0.0/):
```

- Answers

1. 将 Maven 仓库 url 对 http 改为 https

2. 在 `~/.m2/settings.xml` 放开安全校验

```xml
<mirror>
  <id>maven-default-http-blocker</id>
  <mirrorOf>external:http:*</mirrorOf>
  <name>Pseudo repository to mirror external repositories initially using HTTP.</name>
  <url>http://0.0.0.0/</url>
  <!--true 改为 false-->
  <blocked>false</blocked>
</mirror>
```

3. 单独给 Maven 私有仓库放开安全校验

```xml
<mirror>
  <id>automizely-nexus-public</id>
  <mirrorOf>automizely-nexus-public</mirrorOf>
  <url>https://nexus.automizely.org/repository/maven-public/</url>
  <blocked>false</blocked>
</mirror>
```
