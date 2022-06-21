# Mybatis

## Dynamic SQL

1. foreach

```xml
<script>
    INSERT INTO STUDENT (id,name,sex,tel,address)
    VALUES
    <foreach collection="list" item="item" index="index" separator="," >
        (#{item.id},#{item.name},#{item.sex},#{item.tel},#{item.address})
    </foreach>
</script>
```
