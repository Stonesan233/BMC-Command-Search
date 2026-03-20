# 证书管理

> 共 4 条命令

## certificate -d import

**章节**: 7.3.25

**描述**: certificate -d import命令用于导入SSL证书到iBMC系统。

**命令格式**:
```
ipmcset -t certificate -d import -v <localpath | URL> <type> [passphrase]
```

**参数**: 参数说明, localpath, 待导入的SSL证书的, 路径, URL

**示例**:
```
ipmcset -t certificate -d import -v <localpath | URL> <type> [passphrase]
```

---

## certificate -d info

**章节**: 7.3.26

**描述**: certificate -d info命令用于查询SSL证书的信息。

**命令格式**:
```
ipmcget -t certificate -d info
```

**示例**:
```
ipmcget -t certificate -d info
```

---

## syslog -d auth

**章节**: 7.5.2

**描述**: syslog -d auth命令用于查询和设置证书认证方式。

**命令格式**:
```
ipmcget -t syslog -d auth
```

**参数**: 参数说明, option

**示例**:
```
ipmcset -t syslog -d auth -v 2
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

