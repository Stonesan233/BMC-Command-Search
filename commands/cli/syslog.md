# Syslog配置

> 共 12 条命令

## syslog -d state

**章节**: 7.5.1

**描述**: syslog -d state命令用于查询和设置iBMC的syslog上报功能的使能状态。

**命令格式**:
```
ipmcget -t syslog -d state [-v destination]
```

**示例**:
```
ipmcset -t syslog -d state -v enabled
```

---

## syslog -d auth

**章节**: 7.5.2

**描述**: syslog -d auth命令用于查询和设置证书认证方式。

**命令格式**:
```
ipmcget -t syslog -d auth
```

**示例**:
```
ipmcset -t syslog -d auth -v 2
```

---

## syslog -d identity

**章节**: 7.5.3

**描述**: syslog -d identity命令用于查询和设置syslog日志上报时使用的主机标识。

**命令格式**:
```
ipmcget -t syslog -d identity
```

**示例**:
```
ipmcget -t syslog -d identity
```

---

## syslog -d protocol

**章节**: 7.5.4

**描述**: syslog -d protocol命令用于查询和设置上报syslog日志时采用的传输协议类型。

**命令格式**:
```
ipmcget -t syslog -d protocol
```

**示例**:
```
ipmcget -t syslog -d protocol
```

---

## syslog -d severity

**章节**: 7.5.5

**描述**: syslog -d severity命令用于查询和设置通过syslog上报的日志的级别。

**命令格式**:
```
ipmcget -t syslog -d severity
```

**示例**:
```
ipmcset -t syslog -d severity -v critical
```

---

## syslog -d rootcertificate

**章节**: 7.5.6

**描述**: syslog -d rootcertificate命令可查询当前根证书信息。

**命令格式**:
```
ipmcget -t syslog -d rootcertificate
```

**示例**:
```
ipmcget -t syslog -d rootcertificate
```

---

## syslog -d clientcertificate

**章节**: 7.5.7

**描述**: syslog -d clientcertificate命令可查询本地证书信息。

**命令格式**:
```
ipmcget -t syslog -d clientcertificate
```

**示例**:
```
ipmcget -t syslog -d clientcertificate
```

---

## syslog -d address

**章节**: 7.5.8

**描述**: syslog -d address命令用于设置syslog服务器地址。

**命令格式**:
```
ipmcset -t syslog -d address -v <destination> <ipaddr>
```

**示例**:
```
ipmcset -t syslog -d address -v <destination> <ipaddr>
```

---

## syslog -d port

**章节**: 7.5.9

**描述**: syslog -d port命令用于设置syslog服务器端口号。

**命令格式**:
```
ipmcset -t syslog -d port -v <destination> <portvalue>
```

**示例**:
```
ipmcset -t syslog -d port -v <destination> <portvalue>
```

---

## syslog -d logtype

**章节**: 7.5.10

**描述**: syslog -d logtype命令用于设置通过syslog报文上报的日志的类型。

**命令格式**:
```
ipmcset -t syslog -d logtype -v <destination> <type>
```

**示例**:
```
ipmcset -t syslog -d logtype -v <destination> <type>
```

---

## syslog -d test

**章节**: 7.5.11

**描述**: syslog -d test命令用于测试配置的syslog服务器是否可连接。

**命令格式**:
```
ipmcset -t syslog -d test -v <destination>
```

**示例**:
```
ipmcset -t syslog -d test -v <destination>
```

---

## syslog -d iteminfo

**章节**: 7.5.12

**描述**: syslog -d iteminfo命令用于查询4条syslog日志上报通道的配置情况。

**命令格式**:
```
ipmcget -t syslog -d iteminfo
```

**示例**:
```
ipmcget -t syslog -d iteminfo
```

---

