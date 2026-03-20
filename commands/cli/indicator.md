# 指示灯

> 共 2 条命令

## ledinfo

**章节**: 7.11.1

**描述**: ledinfo命令用来查询服务器指示灯信息。

**命令格式**:
```
ipmcget -d ledinfo
```

**示例**:
```
ipmcget -d ledinfo
```

---

## identify

**章节**: 7.11.2

**描述**: identify命令用于设置UID指示灯状态。

**命令格式**:
```
ipmcset -d identify [-v {time | force} ]
```

**示例**:
```
ipmcset -d identify -v force
```

---

