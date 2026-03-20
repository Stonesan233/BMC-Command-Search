# 服务管理

> 共 21 条命令

## service -d state

**章节**: 7.3.19

**描述**: service -d state命令用于设置iBMC的服务状态。

**命令格式**:
```
ipmcset -t service -d state -v <option> <enabled | disabled>
```

**参数**: 参数说明, option, 服务类型, enabled, 启用服务

**示例**:
```
ipmcset -t service -d state -v http enabled
```

---

## service -d list

**章节**: 7.3.21

**描述**: service -d list命令用于查询服务状态。

**命令格式**:
```
ipmcget -t service -d list
```

**参数**: 无, Atlas, 用户指南, 7, 文档版本

**示例**:
```
ipmcget -t service -d list
```

---

## trap -d state

**章节**: 7.4.1

**描述**: trap -d state命令用于查询和设置iBMC的SNMP trap功能的使能和禁止状态。

**命令格式**:
```
ipmcget -t trap -d state [-v destination]
```

**参数**: 参数说明, destination, 表示SNMP, disabled, 表示禁用SNMP

**示例**:
```
ipmcset -t trap -d state -v 1 disabled
```

---

## trap -d community

**章节**: 7.4.3

**描述**: trap -d community命令用于设置iBMC的SNMP trap团体名称。

**命令格式**:
```
ipmcset -t trap -d community
```

**参数**: 参数说明, Community, 表示SNMP, 硬件产品, 不开启密码检查时的取值

**示例**:
```
ipmcset -t trap -d community
```

---

## trap -d version

**章节**: 7.4.6

**描述**: trap -d version命令用于查询和设置SNMP trap版本信息。

**命令格式**:
```
ipmcget -t trap -d version
```

**参数**: 参数说明, V1, 表示SNMP, V2C, 表示SNMP

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

**参数**: 参数说明, level, 表示SNMP, Atlas, 用户指南

**示例**:
```
ipmcset -t trap -d severity -v minor
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

## syslog -d address

**章节**: 7.5.8

**描述**: syslog -d address命令用于设置syslog服务器地址。

**命令格式**:
```
ipmcset -t syslog -d address -v <destination> <ipaddr>
```

**参数**: 参数说明, destination, 表示syslog上报通道的编, 1, ipaddr

**示例**:
```
ipmcset -t syslog -d address -v <destination> <ipaddr>
```

---

## syslog -d test

**章节**: 7.5.11

**描述**: syslog -d test命令用于测试配置的syslog服务器是否可连接。

**命令格式**:
```
ipmcset -t syslog -d test -v <destination>
```

**参数**: 参数说明, destination, 表示syslog上报通道的编, 1

**示例**:
```
ipmcset -t syslog -d test -v <destination>
```

---

## vnc -d info

**章节**: 7.6.1

**描述**: vnc -d info命令用于查询VNC服务的信息。

**命令格式**:
```
ipmcget -t vnc -d info
```

**示例**:
```
ipmcget -t vnc -d info
```

---

## vnc -d timeout

**章节**: 7.6.3

**描述**: vnc -d timeout命令用于设置VNC服务的超时时长。

**命令格式**:
```
ipmcset -t vnc -d timeout -v <value>
```

**参数**: 参数说明, value, 表示VNC服务的超时时长, 位为分钟

**示例**:
```
ipmcset -t vnc -d timeout -v 0
```

---

## vnc -d ssl

**章节**: 7.6.4

**描述**: vnc -d ssl命令用于设置VNC服务SSL加密功能的状态。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 275   ---  ## Page 287

**命令格式**:
```
ipmcset -t vnc -d ssl -v <enabled|disabled>
```

**参数**: 参数说明, enabled, 表示启用SSL加密功能, disabled, 表示禁止SSL加密功能

**示例**:
```
ipmcset -t vnc -d ssl -v enabled
```

---

## vnc -d keyboardlayout

**章节**: 7.6.5

**描述**: vnc -d keyboardlayout命令用于设置VNC服务的键盘布局。

**命令格式**:
```
ipmcset -t vnc -d keyboardlayout -v <en|jp|de>
```

**参数**: 参数说明, en, 表示美式键盘, jp, 表示日式键盘

**示例**:
```
ipmcset -t vnc -d keyboardlayout -v jp
```

---

## macaddr

**章节**: 7.7.7

**描述**: macaddr命令用来查询服务器主板上网口的MAC地址。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 281   ---  ## Page 293

**命令格式**:
```
ipmcget -d macaddr
```

**示例**:
```
ipmcget -d macaddr
```

---

## bbuinfo

**章节**: 7.7.21

**描述**: bbuinfo命令用来查询服务器BBU模块基本信息。

**命令格式**:
```
ipmcget -d bbuinfo
```

**示例**:
```
ipmcget -d bbuinfo
```

---

## serialnumber

**章节**: 7.8.8

**描述**: serialnumber命令用来查询服务器的设备序列号。

**命令格式**:
```
ipmcget [-t smbios] -d serialnumber
```

**示例**:
```
ipmcget -d serialnumber
```

---

## ntp -d preferredserver

**章节**: 7.10.4

**描述**: ntp -d preferredserver命令用于设置首选NTP服务器地址信息。

**命令格式**:
```
ipmcset -t ntp -d preferredserver -v addr
```

**参数**: 参数说明, addr, 表示首选NTP服务器地址

**示例**:
```
ipmcset -t ntp -d preferredserver -v example.com
```

---

## ntp -d alternativeserver

**章节**: 7.10.5

**描述**: ntp -d alternativeserver命令用于设置备用NTP服务器地址信息。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 348   ---  ## Page 360

**命令格式**:
```
ipmcset -t ntp -d alternativeserver -v addr
```

**参数**: 参数说明, addr, 表示备用NTP服务器地址

**示例**:
```
ipmcget -d ntpinfo
```

---

## ntp -d extraserver

**章节**: 7.10.6

**描述**: ntp -d extraserver命令用于设置拓展NTP服务器地址信息。

**命令格式**:
```
ipmcset -t ntp -d extraserver -v addr
```

**参数**: 参数说明, addr, 表示拓展NTP服务器地址

**示例**:
```
ipmcset -t ntp -d extraserver -v 192.168.2.2
```

---

## ntp -d authstatus

**章节**: 7.10.7

**描述**: ntp -d authstatus命令用于设置服务器身份认证状态。 ● 使能身份认证后，iBMC与NTP服务器通信时会进行身份校验。 ● 禁用身份认证后，iBMC与NTP服务器通信时无需进行身份校验。

**命令格式**:
```
ipmcset -t ntp -d authstatus -v status
```

**参数**: 参数说明, status, 表示服务器身份认证状态

**示例**:
```
ipmcset -t ntp -d authstatus -v enabled
```

---

## ledinfo

**章节**: 7.11.1

**描述**: ledinfo命令用来查询服务器指示灯信息。

**命令格式**:
```
ipmcget -d ledinfo
```

**参数**: 无, Atlas, 用户指南, 7, 文档版本

**示例**:
```
ipmcget -d ledinfo
```

---

