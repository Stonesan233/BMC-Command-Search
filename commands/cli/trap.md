# Trap配置

> 共 8 条命令

## trap -d state

**章节**: 7.4.1

**描述**: trap -d state命令用于查询和设置iBMC的SNMP trap功能的使能和禁止状态。

**命令格式**:
```
ipmcget -t trap -d state [-v destination]
```

**示例**:
```
ipmcset -t trap -d state -v 1 disabled
```

---

## trap -d port

**章节**: 7.4.2

**描述**: trap -d port命令用于设置iBMC的SNMP trap上报端口号。

**命令格式**:
```
ipmcset -t trap -d port -v <destination> <portvalue>
```

**示例**:
```
ipmcset -t trap -d port -v 1 1024
```

---

## trap -d community

**章节**: 7.4.3

**描述**: trap -d community命令用于设置iBMC的SNMP trap团体名称。

**命令格式**:
```
ipmcset -t trap -d community
```

**示例**:
```
ipmcset -t trap -d community
```

---

## trap -d address

**章节**: 7.4.4

**描述**: trap -d address命令用于设置SNMP trap上报信息的目的IP地址。

**命令格式**:
```
ipmcset -t trap -d address -v <destination> <ipaddr>
```

**示例**:
```
ipmcset -t trap -d address -v 1 10.10.10.10
```

---

## trap -d trapiteminfo

**章节**: 7.4.5

**描述**: trap -d trapiteminfo命令用于查询SNMP trap上报信息的目的IP地址、上报端口、使 能状态。

**命令格式**:
```
ipmcget -t trap -d trapiteminfo
```

**示例**:
```
ipmcget -t trap -d trapiteminfo
```

---

## trap -d version

**章节**: 7.4.6

**描述**: trap -d version命令用于查询和设置SNMP trap版本信息。

**命令格式**:
```
ipmcget -t trap -d version
```

**示例**:
```
ipmcset -t trap -d version -v V2C
```

---

## trap -d severity

**章节**: 7.4.7

**描述**: trap -d severity命令用于查询和设置SNMP trap的告警发送级别。

**命令格式**:
```
ipmcget -t trap -d severity
```

**示例**:
```
ipmcset -t trap -d severity -v minor
```

---

## trap -d user

**章节**: 7.4.8

**描述**: trap -d user命令用于查询和设置SNMP trap V3用户。

**命令格式**:
```
ipmcget -t trap -d user
```

**示例**:
```
ipmcset -t trap -d user -v root
```

---

