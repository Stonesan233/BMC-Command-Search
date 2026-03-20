# 网络配置

> 共 18 条命令

## ipinfo

**章节**: 7.3.1

**描述**: ipinfo命令用来查询iBMC管理网口的IP信息。

**命令格式**:
```
ipmcget -d ipinfo
```

**示例**:
```
ipmcget -d ipinfo
```

---

## ipaddr

**章节**: 7.3.2

**描述**: ipaddr命令用于设置iBMC管理网口的IPv4地址、掩码、网关。

**命令格式**:
```
ipmcset -d ipaddr -v <ipaddr> <mask> [gateway]
```

**参数**: 参数说明, ipaddr, 表示要设置的iBMC网口的, mask, 表示要设置的iBMC网口的

**示例**:
```
ipmcset -d ipaddr -v 192.168.0.25 255.255.255.0 192.168.0.25
```

---

## ipversion

**章节**: 7.3.3

**描述**: ipversion命令用于设置iBMC网络协议版本。

**命令格式**:
```
ipmcset -d ipversion -v <ipversion>
```

**参数**: 参数说明, ipversion, 表示要设置的iBMC网络协, 议版本

**示例**:
```
ipmcset -d ipversion -v 0
```

---

## backupipaddr

**章节**: 7.3.4

**描述**: backupipaddr命令用于设置iBMC管理网口的备份IPv4地址。 ● 在DHCP功能开启时： – 若iBMC管理网口未分配到IP地址，此时您可以使用备份IP地址登录iBMC系统 进行配置。 – 若iBMC管理网口已分配到IP地址，但用户无法确认分配的具体地址时，您可 以使用备份IP地址登录iBMC系统进行查询。（前提条件为通过DHCP服务器 分配的地址与当前备份地址分布在不同网段，否则无法登录。） ● 在DHCP功能未开启时：备份IP地址不生效，不可使用。

**命令格式**:
```
ipmcset -d backupipaddr -v <ipaddr> <mask>
```

**参数**: 参数说明, ipaddr, 表示要设置的iBMC网口的, mask, 表示要设置的备份IPv4地址

**示例**:
```
ipmcset -d backupipaddr -v 192.168.0.25 255.255.255.0
```

---

## ipmode

**章节**: 7.3.5

**描述**: ipmode命令用于设置iBMC网口的IPv4模式。

**命令格式**:
```
ipmcset -d ipmode -v <dhcp | static>
```

**参数**: 参数说明, dhcp, 表示地址模式为dhcp, static, 表示地址模式为static

**示例**:
```
ipmcset -d ipmode -v dhcp
```

---

## gateway

**章节**: 7.3.6

**描述**: gateway命令用来设置iBMC网口的IPv4网关地址。

**命令格式**:
```
ipmcset -d gateway -v <gateway>
```

**参数**: 参数说明, gateway, 表示iBMC网口的IPv4网

**示例**:
```
ipmcset -d gateway -v 192.168.0.1
```

---

## ipaddr6

**章节**: 7.3.7

**描述**: ipaddr6命令用于设置iBMC网口的IPv6地址、前缀长度和网关地址。

**命令格式**:
```
ipmcset -d ipaddr6 -v <ipaddr6/prefixlen> [gateway6]
```

**参数**: 参数说明, ipaddr6, 表示要设置的iBMC网, prefixlen, 表示要设置的iBMC网

**示例**:
```
ipmcset -d ipaddr6 -v fc00::6516/64 fc00::1
```

---

## ipmode6

**章节**: 7.3.8

**描述**: ipmode6命令用于设置iBMC网口的IPv6模式。

**命令格式**:
```
ipmcset -d ipmode6 -v <dhcp | static>
```

**参数**: 参数说明, dhcp, 表示地址模式为dhcp, static, 表示地址模式为static

**示例**:
```
ipmcset -d ipmode6 -v dhcp
```

---

## gateway6

**章节**: 7.3.9

**描述**: gateway6命令用来设置iBMC网口的IPv6网关地址。

**命令格式**:
```
ipmcset -d gateway6 -v <gateway>
```

**参数**: 参数说明, gateway, 表示iBMC网口的

**示例**:
```
ipmcset -d gateway6 -v fc00::1
```

---

## netmode

**章节**: 7.3.10

**描述**: netmode命令用于设置网口模式。

**命令格式**:
```
ipmcset -d netmode -v <option>
```

**参数**: 参数说明, option, 网口模式

**示例**:
```
ipmcset -d netmode -v 1
```

---

## activeport

**章节**: 7.3.11

**描述**: activeport命令用于设置iBMC管理网口的激活端口。

**命令格式**:
```
ipmcset -d activeport -v <option> [portid]
```

**参数**: 参数说明, option, 激活端口类型, 不同服务器的参数取值范围, portid

**示例**:
```
ipmcset -d activeport -v 0
```

---

## vlan

**章节**: 7.3.12

**描述**: vlan命令用于设置网口的VLAN信息。

**命令格式**:
```
ipmcset -d vlan -v <off | id> [port type]
```

**参数**: 参数说明, off, 禁止VLAN, id, 网口所属VLAN

**示例**:
```
ipmcset -d vlan -v 405
```

---

## service -d port

**章节**: 7.3.20

**描述**: service -d port命令用于设置iBMC指定服务的端口号。

**命令格式**:
```
ipmcset -t service -d port -v <option> <port1value> [port2value]
```

**参数**: 参数说明, option, 服务类型, port1value, 服务的端口号

**示例**:
```
ipmcset -t service -d port -v https 443
```

---

## trap -d port

**章节**: 7.4.2

**描述**: trap -d port命令用于设置iBMC的SNMP trap上报端口号。

**命令格式**:
```
ipmcset -t trap -d port -v <destination> <portvalue>
```

**参数**: 参数说明, destination, 表示SNMP, 1, portvalue

**示例**:
```
ipmcset -t trap -d port -v 1 1024
```

---

## trap -d address

**章节**: 7.4.4

**描述**: trap -d address命令用于设置SNMP trap上报信息的目的IP地址。

**命令格式**:
```
ipmcset -t trap -d address -v <destination> <ipaddr>
```

**参数**: 参数说明, destination, 表示SNMP, ipaddr, 表示接收事件信息上报的

**示例**:
```
ipmcset -t trap -d address -v 1 10.10.10.10
```

---

## syslog -d port

**章节**: 7.5.9

**描述**: syslog -d port命令用于设置syslog服务器端口号。

**命令格式**:
```
ipmcset -t syslog -d port -v <destination> <portvalue>
```

**参数**: 参数说明, destination, 表示syslog上报通道的编, 1, portvalue

**示例**:
```
ipmcset -t syslog -d port -v <destination> <portvalue>
```

---

## ethport

**章节**: 7.7.8

**描述**: ethport命令用来查询iBMC可用网口，包括iBMC专用网口以及支持NCSI功能的网口。

**命令格式**:
```
ipmcget -d ethport
```

**示例**:
```
ipmcget -d ethport
```

---

## ping, ping6

**章节**: 7.17.3

**描述**: ping或ping6命令用于检查网络是否连通。

**命令格式**:
```
ipmcget -d ping, ping6
```

**参数**: 参数说明, IPv4, 目标IPv4地址, Atlas, 用户指南

**示例**:
```
ipmcget -d ping, ping6
```

---

