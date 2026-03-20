# 传感器

> 共 9 条命令

## fanlevel

**章节**: 7.12.1

**描述**: fanlevel命令用于设置风扇运行速度。

**命令格式**:
```
ipmcset -d fanlevel -v <fanlevel> [fanid]
```

**参数**: 参数说明, fanlevel, 表示设置当前风扇PWM占, 转换为风扇真实的转速, fanid

**示例**:
```
ipmcset -d fanlevel -v 50 2
```

---

## faninfo

**章节**: 7.12.2

**描述**: faninfo命令用来查询风扇的工作模式和当前转速。

**命令格式**:
```
ipmcget -d faninfo
```

**示例**:
```
ipmcget -d faninfo
```

---

## fanmode

**章节**: 7.12.3

**描述**: fanmode命令用来设置风扇的运行模式。

**命令格式**:
```
ipmcset -d fanmode -v <mode> [timeout]
```

**参数**: 参数说明, mode, 表示风扇工作模式, Atlas, 用户指南

**示例**:
```
ipmcset -d fanmode -v 1 60
```

---

## coolingmode

**章节**: 7.12.4

**描述**: coolingmode命令用来设置散热设备的运行模式。

**命令格式**:
```
ipmcset -d coolingmode -v <devicetype> <mode> [timeout]
```

**参数**: 参数说明, devicetype, 表示散热设备类型, mode, 表示散热设备工作模式

**示例**:
```
ipmcset -d fan -v 1 60
```

---

## coolingdeviceinfo

**章节**: 7.12.5

**描述**: coolingdeviceinfo命令用来查询散热设备的工作模式和当前转速。

**命令格式**:
```
ipmcget -d coolingdeviceinfo -v <devicetype>
```

**参数**: 参数说明, devicetype, 表示散热设备类型

**示例**:
```
ipmcget -d coolingdeviceinfo -v fan
```

---

## coolinglevel

**章节**: 7.12.6

**描述**: coolinglevel命令用于设置散热设备运行速度。

**命令格式**:
```
ipmcset -d coolinglevel -v <devicetype> <level> [id]
```

**参数**: 参数说明, devicetype, 表示设备类型, level, 表示设置当前散热设备

**示例**:
```
ipmcset -d coolinglevel -v fan 50 2
```

---

## sensor -d list

**章节**: 7.13.1

**描述**: sensor -d list命令用来查询所有传感器信息。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 357   ---  ## Page 369

**命令格式**:
```
ipmcget -t sensor -d list
```

**示例**:
```
ipmcget -t sensor -d list
```

---

## sensor -d test

**章节**: 7.13.2

**描述**: test命令用于模拟传感器状态或读数。 须知 测试之前请先使用ipmcget -t sensor -d list命令查询传感器状态，确保在传感器状态 正常的情况下进行测试，否则已经故障告警的传感器在测试结束后会重复上报一次故 障告警。

**命令格式**:
```
ipmcset -t sensor -d test -v <sensorname/stopall> [value/stop]
```

**参数**: 参数说明, sensorname, 传感器名称, 模拟值

**示例**:
```
ipmcset -t sensor -d test -v "CPU1 Core Rem" 100
```

---

## sensor -d state

**章节**: 7.13.3

**描述**: sensor -d state命令用于设置传感器的使能状态。 说明 该命令只支持离散型传感器，不支持门限型传感器。

**命令格式**:
```
ipmcset -t sensor -d state -v <sensorname> <enabled | disabled>
```

**参数**: 参数说明, sensorname, 传感器名称, enabled

**示例**:
```
ipmcset -t sensor -d state -v "SEL Status" enabled
```

---

