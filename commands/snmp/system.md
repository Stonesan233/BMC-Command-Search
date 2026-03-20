# SNMP 系统命令

> 共 4 个命令 (有效: 3)

## system

**描述**: system

**命令**:
```bash
# system
```

---

## system

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).system(1)`

**描述**: system模块用于展示系统的健康状态，系统启动选项，系统时间，时区，安全下电超时时间，设备名称，设备序列号，上下电策略，系统名称，GUID，服务器标识，系统上下电状态，系统功率，系统OEM信息，设备

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.1
```

---

## domainNameSystem

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).domainNameSystem(2)`

**描述**: DNS信息为表节点，其子节点DNS域名称、DNS信息获取模式、首选DNS服务器、备用DNS服务器1、备用DNS服务器2、所绑定的网络协议为叶子节点。  domainNameSystem模块节点的OID

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.2
```

---

## syslog

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).syslog(34)`

**描述**: 远程日志上报，包括功能使能、主机标识、日志级别、传输协议、认证类型、证书导入等信息。  securityModuleProperty表节点的OID： iso(1).org(3).dod(6).inte

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.32
```

---

