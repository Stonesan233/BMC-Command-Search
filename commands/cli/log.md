# 日志管理

> 共 9 条命令

## syslog -d severity

**章节**: 7.5.5

**描述**: syslog -d severity命令用于查询和设置通过syslog上报的日志的级别。

**命令格式**:
```
ipmcget -t syslog -d severity
```

**参数**: 参数说明, level, 表示上报日志的级

**示例**:
```
ipmcset -t syslog -d severity -v critical
```

---

## syslog -d logtype

**章节**: 7.5.10

**描述**: syslog -d logtype命令用于设置通过syslog报文上报的日志的类型。

**命令格式**:
```
ipmcset -t syslog -d logtype -v <destination> <type>
```

**参数**: 参数说明, destination, 表示syslog上报通道的编, 1, type

**示例**:
```
ipmcset -t syslog -d logtype -v <destination> <type>
```

---

## healthevents

**章节**: 7.8.7

**描述**: healthevents命令用来查询系统的健康事件信息。

**命令格式**:
```
ipmcget [-t fru0] -d healthevents
```

**示例**:
```
ipmcget -d healthevents
```

---

## sel

**章节**: 7.8.9

**描述**: sel命令用来查询和清除系统SEL信息。

**命令格式**:
```
ipmcget -d sel -v <option> [sel_id]
```

**参数**: 参数说明, option, 要进行的操作, 系统最多可保留日志信息, 5000条日志信息以释放空

**示例**:
```
ipmcget -d sel -v info
```

---

## operatelog

**章节**: 7.8.10

**描述**: operatelog命令用来查询系统操作日志。

**命令格式**:
```
ipmcget -d operatelog
```

**示例**:
```
ipmcget -d operatelog
```

---

## loglist

**章节**: 7.8.11

**描述**: loglist命令用来查询一键收集日志列表。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 311   ---  ## Page 323

**命令格式**:
```
ipmcget -t maintenance -d loglist
```

**示例**:
```
ipmcget -d loglist
```

---

## catlog

**章节**: 7.8.12

**描述**: catlog命令用来查询一键收集日志信息。

**命令格式**:
```
ipmcget -t maintenance -d catlog -v <logname> <logcnt> [filter]
```

**参数**: 参数说明, logname, 查询的日志文件名, 通过ipmcget, maintenance

**示例**:
```
ipmcget -t maintenance -d catlog -v app.log 20
```

---

## dumpdfxlog

**章节**: 7.8.27

**描述**: dumpdfxlog命令用于下载处理器dfx日志。

**命令格式**:
```
ipmcget -t maintenance -d dumpdfxlog -v <option> [-s <systemid>]
```

**参数**: 参数说明, option, 获取dfx日志对应处理器的, 类型, gz

**示例**:
```
ipmcget -t maintenance -d dumpdfxlog -v 0
```

---

## precisealarm

**章节**: 7.13.4

**描述**: precisealarm命令用于模拟iBMC定义的事件。

**命令格式**:
```
ipmcset -t precisealarm -d mock -v {eventcode |stopall} [subjectindex]
```

**参数**: 参数说明, eventcode, iBMC定义的全部事, 事件码的第一个字节表, 处理文档中的详细描

**示例**:
```
ipmcset -t precisealarm -d mock -v 0x2C000025 assert
```

---

