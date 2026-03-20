# 风扇散热

> 共 6 条命令

## fanlevel

**章节**: 7.12.1

**描述**: fanlevel命令用于设置风扇运行速度。

**命令格式**:
```
ipmcset -d fanlevel -v <fanlevel> [fanid]
```

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

**示例**:
```
ipmcset -d coolinglevel -v fan 50 2
```

---

