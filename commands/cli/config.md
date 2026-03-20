# 配置管理

> 共 7 条命令

## config -d export

**章节**: 7.3.27

**描述**: config -d export命令用于导出iBMC、BIOS和RAID控制器当前配置文件。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 253   ---  ## Page 265

**命令格式**:
```
ipmcget -t config -d export -v <localpath | URL>
```

**参数**: 参数说明, localpath, 配置文件导出后的本, 地存放路径, URL

**示例**:
```
ipmcget -t config -d export -v <localpath | URL>
```

---

## config -d import

**章节**: 7.3.28

**描述**: config -d import命令用于导入iBMC、BIOS和RAID控制器配置文件。

**命令格式**:
```
ipmcset -t config -d import -v <localpath | URL>
```

**参数**: 参数说明, localpath, 待导入的配置文件所, URL, 待导入的配置文件所

**示例**:
```
ipmcset -t config -d import -v <localpath | URL>
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

## ldconfig

**章节**: 7.7.17

**描述**: ldconfig用于修改逻辑盘的属性。

**命令格式**:
```
ipmcset -t storage -d ldconfig -v <control_id> <ldid> <[-name <ldname>] [-rp
```

**参数**: 参数说明, control_id, RAID控制器的ID, ldid, 逻辑盘的ID

**示例**:
```
ipmcset -t storage -d ldconfig -v <control_id> <ldid> <[-name <ldname>] [-rp
```

---

## ctrlconfig

**章节**: 7.7.18

**描述**: ctrlconfig用于修改RAID控制器的属性。

**命令格式**:
```
ipmcset -t storage -d ctrlconfig -v <control_id> <[-cb <cbstate>] [-smartercb
```

**参数**: 参数说明, control_id, RAID控制器的ID, cbstate, RAID控制器的

**示例**:
```
ipmcset -t storage -d ctrlconfig -v <control_id> <[-cb <cbstate>] [-smartercb
```

---

## pdconfig

**章节**: 7.7.19

**描述**: pdconfig用于修改RAID控制器所管理的物理盘的属性。

**命令格式**:
```
ipmcset -t storage -d pdconfig -v <pdid> [-state <pdstate>] [-hotspare
```

**参数**: 参数说明, pdid, 物理硬盘的ID, pdstate, 物理盘的运行状态

**示例**:
```
ipmcset -t storage -d pdconfig -v <pdid> [-state <pdstate>] [-hotspare
```

---

## sol -d info

**章节**: 7.15.5

**描述**: sol -d info命令用于查询SOL会话配置信息，如查询SOL会话超时时间。

**命令格式**:
```
ipmcget -t sol -d info
```

**示例**:
```
ipmcget -t sol -d info
```

---

