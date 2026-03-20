# 启动配置

> 共 2 条命令

## bootdevice

**章节**: 7.7.1

**描述**: bootdevice用来查询和设置启动设备。

**命令格式**:
```
ipmcget -d bootdevice
```

**参数**: 参数说明, option, 设置的启动设备编, once, 系统启动项的设置仅

**示例**:
```
ipmcset -d bootdevice -v 2 once
```

---

## reboot

**章节**: 7.17.9

**描述**: reboot命令用于重启iBMC系统。

**命令格式**:
```
ipmcget -d reboot
```

**示例**:
```
ipmcget -d reboot
```

---

