# 安全配置

> 共 3 条命令

## securitybanner -d
state

**章节**: 7.3.22

**描述**: securitybanner -d state命令用于设置是否在iBMC登录界面显示安全信息。

**命令格式**:
```
ipmcset -t securitybanner -d state -v <enabled | disabled>
```

**参数**: 参数说明, enabled, 表示在登录界面显示安全, disabled, 表示不在登录界面显示安

**示例**:
```
ipmcset -t securitybanner -d state -v enabled
```

---

## securitybanner -d content

**章节**: 7.3.23

**描述**: securitybanner -d content命令用于设置在iBMC登录界面显示的安全信息的具体内 容。

**命令格式**:
```
ipmcset -t securitybanner -d content -v < default | "option">
```

**参数**: 参数说明, default, 表示使用默认的安全信, option, 表示安全信息的具体内容

**示例**:
```
ipmcset -t securitybanner -d content -v < default | "option">
```

---

## securitybanner -d info

**章节**: 7.3.24

**描述**: securitybanner -d info命令用于查询iBMC登录界面显示的安全信息的详细内容。

**命令格式**:
```
ipmcget -t securitybanner -d info
```

**示例**:
```
ipmcget -t securitybanner -d info
```

---

