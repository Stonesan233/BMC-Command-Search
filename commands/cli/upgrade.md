# 固件升级

> 共 4 条命令

## upgrade

**章节**: 7.3.15

**描述**: upgrade命令用于升级固件。

**命令格式**:
```
ipmcset -d upgrade -v <filepath> [activemode]
```

**参数**: 参数说明, filepath, 表示将要升级的目标文件, activemode, 表示升级完成后是否立即

**示例**:
```
ipmcset -d upgrade -v /tmp/image.hpm 1
```

---

## rollback

**章节**: 7.3.17

**描述**: rollback命令用来将主用iBMC固件当前版本的镜像文件切换到可用版本的镜像文件。

**命令格式**:
```
ipmcset -d rollback
```

**示例**:
```
ipmcset -d rollback
```

---

## rollbackstatus

**章节**: 7.3.18

**描述**: rollbackstatus命令用来查询软件回滚状态。

**命令格式**:
```
ipmcget -d rollbackstatus
```

**示例**:
```
ipmcget -d rollbackstatus
```

---

## upgradebios

**章节**: 7.8.15

**描述**: maintenance -d upgradebios命令用来升级BIOS。 Atlas 900 A3 SuperPoD 超节点 iBMC 用户指南 7 CLI 介绍 文档版本 04 (2025-12-09) 版权所有 © 华为技术有限公司 314   ---  ## Page 326  须知 升级BIOS时，会将BIOS的定制配置擦除，导致BIOS的定制功能失效，请谨慎操作。

**命令格式**:
```
ipmcset -t maintenance -d upgradebios -v filepath
```

**参数**: 参数说明, filepath

**示例**:
```
ipmcset -t maintenance -d upgradebios -v /tmp/biosimage.hpm
```

---

