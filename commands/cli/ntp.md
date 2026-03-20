# NTP时间

> 共 5 条命令

## time

**章节**: 7.8.3

**描述**: time命令用来查询iBMC时间。

**命令格式**:
```
ipmcget -d time
```

**示例**:
```
ipmcget -d time
```

---

## ntpinfo

**章节**: 7.10.1

**描述**: ntpinfo命令用于查询iBMC的NTP信息。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 345   ---  ## Page 357

**命令格式**:
```
ipmcget -d ntpinfo
```

**示例**:
```
ipmcget -d ntpinfo
```

---

## ntp -d status

**章节**: 7.10.2

**描述**: ntp -d status命令用于设置NTP功能的使能状态。

**命令格式**:
```
ipmcset -t ntp -d status -v status
```

**参数**: 参数说明, status, 表示NTP功能的使能状态

**示例**:
```
ipmcset -t ntp -d status -v enabled
```

---

## ntp -d mode

**章节**: 7.10.3

**描述**: ntp -d mode命令用于设置NTP信息获取方式。

**命令格式**:
```
ipmcset -t ntp -d mode -v mode
```

**参数**: 参数说明, mode, 表示NTP信息获取方式, 信息, 自动获取NTP信息

**示例**:
```
ipmcset -t ntp -d mode -v manual
```

---

## sol -d timeout

**章节**: 7.15.3

**描述**: sol -d timeout命令用于设置SOL会话超时时间。设置超时时间后，用户在SOL会话中 无输入并达到超时时间后，SOL会话将退出并返回iBMC命令行界面。

**命令格式**:
```
ipmcset -t sol -d timeout -v <value>
```

**参数**: 参数说明, value, 表示SOL会话用户无输入, 0, 超时时间的默认取值为15

**示例**:
```
ipmcset -t sol -d timeout -v 20
```

---

