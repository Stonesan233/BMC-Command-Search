# 服务器管理

> 共 21 条命令

## bootdevice

**章节**: 7.7.1

**描述**: bootdevice用来查询和设置启动设备。

**命令格式**:
```
ipmcget -d bootdevice
```

**示例**:
```
ipmcset -d bootdevice -v 2 once
```

---

## frucontrol

**章节**: 7.7.2

**描述**: frucontrol命令设置服务器的重启方式。

**命令格式**:
```
ipmcset [-t fru0] -d frucontrol -v <option>
```

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

**示例**:
```
ipmcset -t fru4 -d frucontrol -v 0
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

## clearcmos

**章节**: 7.7.9

**描述**: clearcmos命令用于清除BIOS Flash上的用户自定义信息。

**命令格式**:
```
ipmcset -d clearcmos
```

**示例**:
```
ipmcset -d clearcmos
```

---

## ctrlinfo

**章节**: 7.7.10

**描述**: ctrlinfo用来查询RAID控制器信息。

**命令格式**:
```
ipmcget -t storage -d ctrlinfo -v <option>
```

**示例**:
```
ipmcget -t storage -d ctrlinfo -v 0
```

---

## ldinfo

**章节**: 7.7.11

**描述**: ldinfo用来查询RAID控制器所管理的逻辑盘的信息。

**命令格式**:
```
ipmcget -t storage -d ldinfo -v <ctrlid> <option>
```

**示例**:
```
ipmcget -t storage -d ldinfo -v 0 0
```

---

## pdinfo

**章节**: 7.7.12

**描述**: pdinfo用来查询物理盘的信息。

**命令格式**:
```
ipmcget -t storage -d pdinfo -v <option>
```

**示例**:
```
ipmcget -t storage -d pdinfo -v 2
```

---

## arrayinfo

**章节**: 7.7.13

**描述**: arrayinfo用来查询磁盘组的信息。

**命令格式**:
```
ipmcget -t storage -d arrayinfo -v <control_id> <option>
```

**示例**:
```
ipmcget -t storage -d arrayinfo -v 0 1
```

---

## createld

**章节**: 7.7.14

**描述**: createld用于使用空闲物理盘创建虚拟盘。

**命令格式**:
```
ipmcset -t storage -d createld -v <control_id> -rl <raidlevel> -pd <pd_id> [-
```

**示例**:
```
ipmcset -t storage -d createld -v <control_id> -rl <raidlevel> -pd <pd_id> [-
```

---

## addld

**章节**: 7.7.15

**描述**: addld用于在已有逻辑盘的磁盘组上添加新的逻辑盘。

**命令格式**:
```
ipmcset -t storage -d addld -v <control_id> -array <arrayid> [-name <ldname>]
```

**示例**:
```
ipmcset -t storage -d addld -v <control_id> -array <arrayid> [-name <ldname>]
```

---

## deleteld

**章节**: 7.7.16

**描述**: deleteld用于删除RAID卡管理的逻辑盘。

**命令格式**:
```
ipmcset -t storage -d deleteld -v <control_id> <ldid>
```

**示例**:
```
ipmcset -t storage -d deleteld -v <control_id> <ldid>
```

---

## ldconfig

**章节**: 7.7.17

**描述**: ldconfig用于修改逻辑盘的属性。

**命令格式**:
```
ipmcset -t storage -d ldconfig -v <control_id> <ldid> <[-name <ldname>] [-rp
```

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

**示例**:
```
ipmcset -t storage -d pdconfig -v <pdid> [-state <pdstate>] [-hotspare
```

---

## npuworkmode

**章节**: 7.7.20

**描述**: npuworkmode命令用于查询和设置NPU芯片的工作模式。

**命令格式**:
```
ipmcget -d npuworkmode
```

**示例**:
```
ipmcset -d npuworkmode -v 0
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

