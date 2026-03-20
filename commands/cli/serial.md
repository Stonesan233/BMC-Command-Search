# 串口配置

> 共 2 条命令

## serialdir

**章节**: 7.3.13

**描述**: serialdir命令用来查询和设置串口方向。

**命令格式**:
```
ipmcget -d serialdir
```

**参数**: 参数说明, 串口方向, 为系统串口, 为iBMC串口, 板串口切换为SCCL串

**示例**:
```
ipmcset -d serialdir -v 1
```

---

## systemcom

**章节**: 7.8.13

**描述**: systemcom命令用来下载系统串口数据。

**命令格式**:
```
ipmcget -d systemcom
```

**参数**: 无, Atlas, 用户指南, 7, 文档版本

**示例**:
```
ipmcget -d systemcom
```

---

