# 系统管理

> 共 4 条命令

## printscreen

**章节**: 7.3.16

**描述**: printscreen命令用于截取服务器当前所显示的屏幕图片。

**命令格式**:
```
ipmcset -d printscreen [-v wakeup]
```

**参数**: 参数说明, wakeup, 截取屏幕图片的同时唤醒, 系统屏保

**示例**:
```
ipmcset -d printscreen
```

---

## systemname

**章节**: 7.8.1

**描述**: systemname命令用来查询系统名称。

**命令格式**:
```
ipmcget -t smbios -d systemname
```

**示例**:
```
ipmcget -t smbios -d systemname
```

---

## health

**章节**: 7.8.6

**描述**: health命令用来查询系统的健康状态。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 307   ---  ## Page 319

**命令格式**:
```
ipmcget [-t fru0] -d health
```

**示例**:
```
ipmcget -d health
```

---

## securityenhance -d updatemasterkey

**章节**: 7.8.18

**描述**: securityenhance -d updatemasterkey命令用来更新系统主密钥。

**命令格式**:
```
ipmcset -t securityenhance -d updatemasterkey
```

**示例**:
```
ipmcset -t securityenhance -d updatemasterkey
```

---

