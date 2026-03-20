# 虚拟媒体

> 共 3 条命令

## vmm -d connect

**章节**: 7.3.29

**描述**: vmm -d connect命令用于挂载文件到虚拟光驱。

**命令格式**:
```
ipmcset -t vmm -d connect -v <URL>
```

**参数**: 参数说明, URL, 待挂载的文件所在的, iBMC当前仅支持SMB, Atlas

**示例**:
```
ipmcset -t vmm -d connect -v <URL>
```

---

## vmm -d disconnect

**章节**: 7.3.30

**描述**: vmm -d disconnect命令用于断开虚拟光驱的连接。

**命令格式**:
```
ipmcset -t vmm -d disconnect
```

**示例**:
```
ipmcset -t vmm -d disconnect
```

---

## vmm -d info

**章节**: 7.3.31

**描述**: vmm -d info命令用于查询iBMC虚拟媒体信息。

**命令格式**:
```
ipmcget -t vmm -d info
```

**参数**: 无, Atlas, 用户指南, 7, 文档版本

**示例**:
```
ipmcget -t vmm -d info
```

---

