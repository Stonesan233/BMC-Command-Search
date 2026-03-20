# 电源管理

> 共 9 条命令

## reset

**章节**: 7.3.14

**描述**: reset命令用来重启iBMC管理系统。

**命令格式**:
```
ipmcset -d reset
```

**示例**:
```
ipmcset -d reset
```

---

## frucontrol

**章节**: 7.7.2

**描述**: frucontrol命令设置服务器的重启方式。

**命令格式**:
```
ipmcset [-t fru0] -d frucontrol -v <option>
```

**参数**: 参数说明, option, 服务器重启方式, 器, 电服务器

**示例**:
```
ipmcset -d frucontrol -v 0
```

---

## powerstate

**章节**: 7.7.3

**描述**: powerstate命令用于查询和控制服务器的上电和下电状态。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 278   ---  ## Page 290

**命令格式**:
```
ipmcget [-t fru0] -d powerstate
```

**参数**: 参数说明, option, 要对服务器进行的操作

**示例**:
```
ipmcset -d powerstate -v 1
```

---

## shutdowntimeout

**章节**: 7.7.4

**描述**: shutdowntimeout命令用来查询和设置服务器的下电时限。 下电时限：执行下电操作后，iBMC系统等待操作系统下电的时间。如果超过该时间操 作系统仍未自动下电，iBMC会强制执行下电操作。

**命令格式**:
```
ipmcget [-t fru0] -d shutdowntimeout
```

**参数**: 参数说明, time

**示例**:
```
ipmcset -d shutdowntimeout -v 600
```

---

## frucontrol

**章节**: 7.7.5

**描述**: frucontrol命令进行全域重启方式。

**命令格式**:
```
ipmcset -t fru4 -d frucontrol -v <option>
```

**参数**: 参数说明, option, 全域重启方式, 上电, Atlas

**示例**:
```
ipmcset -t fru4 -d frucontrol -v 0
```

---

## powerstate

**章节**: 7.7.6

**描述**: powerstate命令进行全域下电。

**命令格式**:
```
ipmcset -t fru4 -d powerstate -v <option>
```

**参数**: 参数说明, option, 全域下电

**示例**:
```
ipmcset -t fru4 -d frucontrol -v 0
```

---

## poweronlock

**章节**: 7.8.20

**描述**: 默认状态下，若服务器在指定时间内未完成上电，则通过iBMC为服务器上电的功能被 锁定，服务器将无法通过iBMC上电。 poweronlock命令用来查询此上电锁的锁定状态，并可清除此上电锁，取消上述限 制。

**命令格式**:
```
ipmcget -t maintenance -d poweronlock
```

**示例**:
```
ipmcget -t maintenance -d poweronlock
```

---

## resetiME

**章节**: 7.8.22

**描述**: resetiME命令用于重启鲲鹏智能管理引擎，当鲲鹏智能管理引擎无法正常运行时，可 使用该命令将其重启。

**命令格式**:
```
ipmcset -t maintenance -d resetiME
```

**示例**:
```
ipmcset -t maintenance -d resetiME
```

---

## psuinfo

**章节**: 7.14.1

**描述**: psuinfo命令用来获取电源信息。

**命令格式**:
```
ipmcget -d psuinfo
```

**示例**:
```
ipmcget -d psuinfo
```

---

