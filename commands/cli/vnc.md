# VNC配置

> 共 5 条命令

## vnc -d info

**章节**: 7.6.1

**描述**: vnc -d info命令用于查询VNC服务的信息。

**命令格式**:
```
ipmcget -t vnc -d info
```

**示例**:
```
ipmcget -t vnc -d info
```

---

## vnc -d password

**章节**: 7.6.2

**描述**: vnc -d password命令用于设置VNC服务的密码。

**命令格式**:
```
ipmcset -t vnc -d password
```

**示例**:
```
ipmcset -t vnc -d password
```

---

## vnc -d timeout

**章节**: 7.6.3

**描述**: vnc -d timeout命令用于设置VNC服务的超时时长。

**命令格式**:
```
ipmcset -t vnc -d timeout -v <value>
```

**示例**:
```
ipmcset -t vnc -d timeout -v 0
```

---

## vnc -d ssl

**章节**: 7.6.4

**描述**: vnc -d ssl命令用于设置VNC服务SSL加密功能的状态。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 275   ---  ## Page 287

**命令格式**:
```
ipmcset -t vnc -d ssl -v <enabled|disabled>
```

**示例**:
```
ipmcset -t vnc -d ssl -v enabled
```

---

## vnc -d keyboardlayout

**章节**: 7.6.5

**描述**: vnc -d keyboardlayout命令用于设置VNC服务的键盘布局。

**命令格式**:
```
ipmcset -t vnc -d keyboardlayout -v <en|jp|de>
```

**示例**:
```
ipmcset -t vnc -d keyboardlayout -v jp
```

---

