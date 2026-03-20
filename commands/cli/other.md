# 其他命令

> 共 41 条命令

## lldpinfo

**章节**: 7.3.32

**描述**: lldpinfo命令用于查询iBMC的LLDP信息。

**命令格式**:
```
ipmcget -d lldpinfo
```

**示例**:
```
ipmcget -d lldpinfo
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

## syslog -d state

**章节**: 7.5.1

**描述**: syslog -d state命令用于查询和设置iBMC的syslog上报功能的使能状态。

**命令格式**:
```
ipmcget -t syslog -d state [-v destination]
```

**参数**: 参数说明, destination, 表示syslog上报通道的编, 启用或禁用syslog功, disabled

**示例**:
```
ipmcset -t syslog -d state -v enabled
```

---

## syslog -d identity

**章节**: 7.5.3

**描述**: syslog -d identity命令用于查询和设置syslog日志上报时使用的主机标识。

**命令格式**:
```
ipmcget -t syslog -d identity
```

**参数**: 参数说明, option, 表示要设置的主机标, 识

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

**参数**: 参数说明, option

**示例**:
```
ipmcget -t syslog -d protocol
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

**参数**: 参数说明, option, 待查询的RAID控制器

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

**参数**: 参数说明, ctrlid, 待查询逻辑盘所属, option, 待查询的逻辑盘的

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

**参数**: 参数说明, option, 待查询的物理盘的

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

**参数**: 参数说明, control_id, 磁盘组所在控制器的, ID, option

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

**参数**: 参数说明, control_id, RAID控制器的ID, raidlevel, 逻辑盘的RAID级别

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

**参数**: 参数说明, control_id, RAID控制器的ID, arrayid, 待添加逻辑盘的磁盘

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

**参数**: 参数说明, control_id, RAID控制器的ID, ldid, 待删除的逻辑盘的ID

**示例**:
```
ipmcset -t storage -d deleteld -v <control_id> <ldid>
```

---

## npuworkmode

**章节**: 7.7.20

**描述**: npuworkmode命令用于查询和设置NPU芯片的工作模式。

**命令格式**:
```
ipmcget -d npuworkmode
```

**参数**: 参数说明, option, NPU芯片的工作模式, Atlas, 用户指南

**示例**:
```
ipmcset -d npuworkmode -v 0
```

---

## timezone

**章节**: 7.8.2

**描述**: timezone命令用来设置iBMC时区。

**命令格式**:
```
ipmcset -d timezone -v <timezone>
```

**参数**: 参数说明, timezone, 当输入的是时间偏移中不带

**示例**:
```
ipmcset -d timezone -v +8:00
```

---

## version

**章节**: 7.8.4

**描述**: version命令用来查询设备的版本信息。

**命令格式**:
```
ipmcget -d version
```

**示例**:
```
ipmcget -d version
```

---

## fruinfo

**章节**: 7.8.5

**描述**: fruinfo命令用于查询除电源模块之外的其它FRU的信息，包括主板、RAID卡、硬盘背 板、PCIe Riser卡等。

**命令格式**:
```
ipmcget [-t fru0] -d fruinfo
```

**示例**:
```
ipmcget -d fruinfo
```

---

## blackbox

**章节**: 7.8.14

**描述**: blackbox命令用来下载黑匣子数据。

**命令格式**:
```
ipmcget -d blackbox
```

**示例**:
```
ipmcget -d blackbox
```

---

## diaginfo

**章节**: 7.8.16

**描述**: diaginfo命令用来一键收集信息，包括iBMC相关的配置信息、版本信息和日志等。一 键收集信息的更多内容请参见本文档6.10 一键收集信息说明。

**命令格式**:
```
ipmcget -d diaginfo [-v destination]
```

**参数**: 参数说明, destination, 将一键收集的信息导出到

**示例**:
```
ipmcget -d diaginfo -v cifs://test:123@10.10.10.1/CIFSshare/
```

---

## restore

**章节**: 7.8.17

**描述**: restore命令用来恢复iBMC出厂设置。执行此命令后iBMC会重启。

**命令格式**:
```
ipmcset -d restore
```

**示例**:
```
ipmcset -d restore
```

---

## securityenhance -d
masterkeyupdateinterval

**章节**: 7.8.19

**描述**: securityenhance -d masterkeyupdateinterval命令用来查询和设置主密钥自动更新 间隔。

**命令格式**:
```
ipmcget -t securityenhance -d masterkeyupdateinterval
```

**参数**: 参数说明, interval, 表示自动更新间隔

**示例**:
```
ipmcget -t securityenhance -d masterkeyupdateinterval
```

---

## biosprint

**章节**: 7.8.21

**描述**: biosprint命令用于查询和设置BIOS全打印开关状态。

**命令格式**:
```
ipmcget -t maintenance -d biosprint
```

**参数**: 参数说明, BIOS全打印开关状态, 全打印的开启和关闭取, 决于本地菜单设置标志

**示例**:
```
ipmcset -t maintenance -d biosprint -v 1
```

---

## retiresystem

**章节**: 7.8.23

**描述**: retiresystem命令用于设置产品报废。

**命令格式**:
```
ipmcset -t maintenance -d retiresystem -v <option>
```

**参数**: 参数说明, 销毁日志选项

**示例**:
```
ipmcset -t maintenance -d retiresystem -v 0
```

---

## retiresystem

**章节**: 7.8.24

**描述**: retiresystem命令用于查询产品报废任务信息。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 321   ---  ## Page 333

**命令格式**:
```
ipmcget -t maintenance -d retiresystem
```

**示例**:
```
ipmcset -t maintenance -d retiresystem
```

---

## listcsr

**章节**: 7.8.25

**描述**: listcsr命令用于查询在位的天池组件信息。

**命令格式**:
```
ipmcget -t maintenance -d listcsr
```

**示例**:
```
ipmcget -t maintenance -d listcsr
```

---

## importcsr

**章节**: 7.8.26

**描述**: importcsr命令用于导入CSR到eeprom。

**命令格式**:
```
ipmcset -t maintenance -d importcsr -v <option> <filepath>
```

**参数**: 参数说明, option, 待导入固件的组件标识, 命令查询, filepath

**示例**:
```
ipmcset -t maintenance -d importcsr -v Connector_CLU_1_0101 /tmp/image.hpm
```

---

## weakpwddic

**章节**: 7.9.15

**描述**: weakpwddic命令用于设置弱口令字典认证功能的使能状态。 出现在弱口令字典中的字符串不能被设置为： ● 本地用户的密码 ● SNMP v1/v2c的只读团体名、读写团体名 ● SNMP v3加密密码

**命令格式**:
```
ipmcset -t user -d weakpwddic -v <enabled | disabled>
```

**参数**: 参数说明, enabled, 使能弱口令字典认证功能, disabled, 禁止弱口令字典认证功能

**示例**:
```
ipmcset -t user -d weakpwddic -v <enabled | disabled>
```

---

## weakpwddic -v export

**章节**: 7.9.16

**描述**: weakpwddic -v export命令用于导出iBMC的弱口令字典。

**命令格式**:
```
ipmcset -t user -d weakpwddic -v export <filepath | file_URL>
```

**参数**: 参数说明, filepath, 将弱口令字典导出到iBMC, file_URL, 将弱口令字典导出到远程

**示例**:
```
ipmcset -t user -d weakpwddic -v export <filepath | file_URL>
```

---

## weakpwddic -v import

**章节**: 7.9.17

**描述**: weakpwddic -v import命令用于导入iBMC的弱口令字典。

**命令格式**:
```
ipmcset -t user -d weakpwddic -v import <filepath | file_URL>
```

**参数**: 参数说明, filepath, 将弱口令字典导入iBMC, file_URL, 将弱口令字典导入iBMC

**示例**:
```
ipmcset -t user -d weakpwddic -v import <filepath | file_URL>
```

---

## identify

**章节**: 7.11.2

**描述**: identify命令用于设置UID指示灯状态。

**命令格式**:
```
ipmcset -d identify [-v {time | force} ]
```

**参数**: 参数说明, time, 表示UID指示灯闪烁时, force, 表示永久点亮UID指示

**示例**:
```
ipmcset -d identify -v force
```

---

## sol -d activate

**章节**: 7.15.1

**描述**: sol -d activate命令用于建立SOL会话连接系统或iBMC串口。

**命令格式**:
```
ipmcset -t sol -d activate -v <option> <mode>
```

**参数**: 参数说明, option, 板串口切换为IMU串口, 不同服务器的参数取值及, 串口的连接方向可能不

**示例**:
```
ipmcset -t sol -d activate -v 1 0
```

---

## sol -d deactivate

**章节**: 7.15.2

**描述**: sol -d deactivate命令用于强制注销SOL会话。

**命令格式**:
```
ipmcset -t sol -d deactivate -v <index>
```

**参数**: 参数说明, index

**示例**:
```
ipmcset -t sol -d deactivate -v 1
```

---

## sol -d session

**章节**: 7.15.4

**描述**: sol -d session命令用于查询SOL会话列表。

**命令格式**:
```
ipmcget -t sol -d session
```

**示例**:
```
ipmcget -t sol -d session
```

---

## lsw -d reset

**章节**: 7.16.1

**描述**: lsw -d reset命令用于复位并修复LSW芯片。

**命令格式**:
```
ipmcset -t lsw -d reset -v <device><type>
```

**参数**: 参数说明, device, 复位器件, type, 复位类型

**示例**:
```
ipmcset -t lsw -d reset -v 1 1
```

---

## help

**章节**: 7.17.1

**描述**: help命令用于查看帮助信息，也可以查看某条命令的具体使用方法。

**命令格式**:
```
ipmcget -d help
```

**参数**: 参数说明, command, 具体命令

**示例**:
```
ipmcget -d help
```

---

## exit

**章节**: 7.17.2

**描述**: exit命令用于断开客户端与iBMC的连接。

**命令格式**:
```
ipmcget -d exit
```

**示例**:
```
ipmcget -d exit
```

---

## free

**章节**: 7.17.4

**描述**: 该命令用于执行Linux中的free命令。

**命令格式**:
```
ipmcget -d free
```

**示例**:
```
ipmcget -d free
```

---

## netstat

**章节**: 7.17.5

**描述**: 该命令用于执行Linux中的netstat命令。

**命令格式**:
```
ipmcget -d netstat
```

**示例**:
```
ipmcget -d netstat
```

---

## df

**章节**: 7.17.6

**描述**: 该命令用于执行Linux中的df命令。

**命令格式**:
```
ipmcget -d df
```

**示例**:
```
ipmcget -d df
```

---

## top

**章节**: 7.17.7

**描述**: 该命令用于执行Linux中的top命令。

**命令格式**:
```
ipmcget -d top
```

**示例**:
```
ipmcget -d top
```

---

## notimeout

**章节**: 7.17.8

**描述**: notimeout命令用于禁止CLP超时，确保可以在CLP命令行进行长时间操作。

**命令格式**:
```
ipmcget -d notimeout
```

**示例**:
```
ipmcget -d notimeout
```

---

