# 用户管理

> 共 20 条命令

## trap -d user

**章节**: 7.4.8

**描述**: trap -d user命令用于查询和设置SNMP trap V3用户。

**命令格式**:
```
ipmcget -t trap -d user
```

**参数**: 参数说明, username, 表示SNMP

**示例**:
```
ipmcset -t trap -d user -v root
```

---

## vnc -d password

**章节**: 7.6.2

**描述**: vnc -d password命令用于设置VNC服务的密码。

**命令格式**:
```
ipmcset -t vnc -d password
```

**示例**:
```
ipmcset -t vnc -d password
```

---

## userlist/list

**章节**: 7.9.1

**描述**: userlist/list命令用来查询所有用户信息。

**命令格式**:
```
ipmcget -d userlist
```

**参数**: 无, Atlas, 用户指南, 7, 文档版本

**示例**:
```
ipmcget -t user -d list
```

---

## adduser

**章节**: 7.9.2

**描述**: adduser用于添加新用户。

**命令格式**:
```
ipmcset [-t user] -d adduser -v <username>
```

**参数**: 参数说明, username

**示例**:
```
ipmcset -d adduser -v test
```

---

## password

**章节**: 7.9.3

**描述**: password命令用来修改用户密码。

**命令格式**:
```
ipmcset [-t user] -d password -v username
```

**参数**: 参数说明, username, 表示已存在的待修改密码

**示例**:
```
ipmcset -d password -v user
```

---

## deluser

**章节**: 7.9.4

**描述**: deluser用来删除用户。

**命令格式**:
```
ipmcset [-t user] -d deluser -v username
```

**参数**: 参数说明, username, 表示当前存在的待删除的

**示例**:
```
ipmcset -d deluser -v test
```

---

## privilege

**章节**: 7.9.5

**描述**: privilege命令用来设置用户权限。

**命令格式**:
```
ipmcset [-t user] -d privilege -v <username> <privalue>
```

**参数**: 参数说明, username, 表示当前存在的待设置权, Atlas, 用户指南

**示例**:
```
ipmcset -d privilege -v test 4
```

---

## passwordcomplexity

**章节**: 7.9.6

**描述**: passwordcomplexity命令用来查询和设置密码复杂度检查功能的启用状态。

**命令格式**:
```
ipmcget [-t user] -d passwordcomplexity
```

**参数**: 参数说明, enabled, 启用密码复杂度检查功能, disabled, 禁用密码复杂度检查功能

**示例**:
```
ipmcget -d passwordcomplexity
```

---

## user -d lock

**章节**: 7.9.7

**描述**: lock命令用于锁定指定的用户，而用户在被锁定之后将不能登录。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 331   ---  ## Page 343

**命令格式**:
```
ipmcset -t user -d lock -v username
```

**参数**: 参数说明, username, 待锁定用户的用户名

**示例**:
```
ipmcset -t user -d lock -v admin
```

---

## user -d unlock

**章节**: 7.9.8

**描述**: unlock命令用于解锁被手动锁定或因密码重试次数用完而锁定的用户。

**命令格式**:
```
ipmcset -t user -d unlock -v username
```

**参数**: 参数说明, username, 待解锁用户的用户名

**示例**:
```
ipmcset -t user -d unlock -v root
```

---

## minimumpasswordage

**章节**: 7.9.9

**描述**: minimumpasswordage命令用于查询和设置密码的最短使用期。 密码最短使用期，是指设置一个密码后，要使用的最短时间，在此期间不能修改此密 码。

**命令格式**:
```
ipmcget -d minimumpasswordage
```

**参数**: 参数说明, time, 密码最短使用期, 0表示密码最短使用期为无

**示例**:
```
ipmcset -d minimumpasswordage -v 1
```

---

## emergencyuser

**章节**: 7.9.10

**描述**: emergencyuser命令用于设置不受登录规则限制的紧急用户。

**命令格式**:
```
ipmcset [-t user] -d emergencyuser -v username
```

**参数**: 参数说明, username, 紧急用户的用户名

**示例**:
```
ipmcset -d emergencyuser -v root
```

---

## addpublickey

**章节**: 7.9.11

**描述**: addpublickey命令为用户添加SSH公钥。

**命令格式**:
```
ipmcset -t user -d addpublickey -v username <filepath|file_URL>
```

**参数**: 参数说明, username, 待导入SSH公钥的用户名, 已存在的SSH用户的用户, 名

**示例**:
```
ipmcset -t user -d addpublickey -v ssh_user /tmp/id_dsa_2048.key
```

---

## delpublickey

**章节**: 7.9.12

**描述**: delpublickey命令为用户删除SSH公钥。

**命令格式**:
```
ipmcset -t user -d delpublickey -v username
```

**参数**: 参数说明, username, 待删除SSH公钥的用户的, 用户名

**示例**:
```
ipmcset -t user -d delpublickey -v ssh_user_01
```

---

## interface

**章节**: 7.9.14

**描述**: interface命令用于设置指定用户登录iBMC的接口类型。

**命令格式**:
```
ipmcset -t user -d interface -v username <enabled | disabled> <option1
```

**参数**: 参数说明, username, 待配置的用户, enabled, 使能指定的接口类型

**示例**:
```
ipmcget -t user -d list
```

---

## snmpprivacypassword

**章节**: 7.9.18

**描述**: snmpprivacypassword命令用于设置指定用户使用SNMPv3连接iBMC的数据加密密 码。

**命令格式**:
```
ipmcset -t user -d snmpprivacypassword -v username
```

**参数**: 参数说明, username, 待配置的用户

**示例**:
```
ipmcset -t user -d snmpprivacypassword -v Administrator
```

---

## securityenhanc -d
inactivetimelimit

**章节**: 7.9.19

**描述**: securityenhance -d inactivetimelimit命令用于设置用户不活动期限。超过设定期限 内未活动的用户会被禁用。

**命令格式**:
```
ipmcset -t securityenhance -d inactivetimelimit -v <value>
```

**参数**: 参数说明, value, 表示不活动期限

**示例**:
```
ipmcset -t securityenhance -d inactivetimelimit -v <value>
```

---

## user -d state

**章节**: 7.9.20

**描述**: user -d state命令用于设置用户的启用状态。

**命令格式**:
```
ipmcset -t user -d state -v <username> [enabled | disabled]
```

**参数**: 参数说明, username, 表示待设置的用户, 已存在的用户名, enabled

**示例**:
```
ipmcset -t user -d state -v <username> [enabled | disabled]
```

---

## user -d
usermgmtbyhost

**章节**: 7.9.21

**描述**: user -d usermgmtbyhost命令用于查询和设置带内用户管理功能的使能状态。

**命令格式**:
```
ipmcset -t user -d usermgmtbyhost -v <option>
```

**参数**: 参数说明, option, 表示待设置的带内用户管, 理使能状态, 功能

**示例**:
```
ipmcset -t user -d usermgmtbyhost -v 0
```

---

## user -d
firstloginpolicy

**章节**: 7.9.22

**描述**: 对于新建的用户或被重置了密码的用户，其登录密码为初始状态，可能存在密码泄露 的风险。 user -d firstloginpolicy命令用于设置用户密码为初始状态的情况下，首次登录时的 密码修改策略。

**命令格式**:
```
ipmcset -t user -d firstloginpolicy -v <username> <option>
```

**参数**: 参数说明, username, 表示待设置的用户, 已存在的用户名, option

**示例**:
```
ipmcset -t user -d firstloginpolicy -v testuser 1
```

---

