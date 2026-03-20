# SOL串口

> 共 5 条命令

## sol -d activate

**章节**: 7.15.1

**描述**: sol -d activate命令用于建立SOL会话连接系统或iBMC串口。

**命令格式**:
```
ipmcset -t sol -d activate -v <option> <mode>
```

**示例**:
```
ipmcset -t sol -d activate -v 1 0
```

---

## sol -d deactivate

**章节**: 7.15.2

**描述**: sol -d deactivate命令用于强制注销SOL会话。

**命令格式**:
```
ipmcset -t sol -d deactivate -v <index>
```

**示例**:
```
ipmcset -t sol -d deactivate -v 1
```

---

## sol -d timeout

**章节**: 7.15.3

**描述**: sol -d timeout命令用于设置SOL会话超时时间。设置超时时间后，用户在SOL会话中 无输入并达到超时时间后，SOL会话将退出并返回iBMC命令行界面。

**命令格式**:
```
ipmcset -t sol -d timeout -v <value>
```

**示例**:
```
ipmcset -t sol -d timeout -v 20
```

---

## sol -d session

**章节**: 7.15.4

**描述**: sol -d session命令用于查询SOL会话列表。

**命令格式**:
```
ipmcget -t sol -d session
```

**示例**:
```
ipmcget -t sol -d session
```

---

## sol -d info

**章节**: 7.15.5

**描述**: sol -d info命令用于查询SOL会话配置信息，如查询SOL会话超时时间。

**命令格式**:
```
ipmcget -t sol -d info
```

**示例**:
```
ipmcget -t sol -d info
```

---

