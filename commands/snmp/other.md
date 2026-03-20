# SNMP 其他命令

> 共 19 个命令 (有效: 19)

## ldap

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).ldap(3).ldapEnable(1)`

**描述**: 该模块包括ldap启用状态，域控制器地址，用户域，用户组组名、组域、组特权。  由十九个简单叶子节点和六个表节点组成。  LdapEnable简单叶子节点OID:  iso(1).org(3).dod

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.3
```

---

## trap

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).trap(4)`

**描述**: Trap模块的简单节点查询和设置trap目标的使能状态，trap团体名，trap发送级别，trap模式，trap版本，trap标示符，trap详细发送级别，trap v3 用户名；trap模块的表节点

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.4
```

---

## smtp

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).smtp(5)`

**描述**: 管理smtp服务器和smtp目标接收者。  Smtp服务器节点OID： iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawe

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.5
```

---

## fruLedProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).fruLedProperty(9)`

**描述**: LED属性信息，其中包括LED名称、支持颜色、默认本地控制颜色、默认逾越状态颜色、颜色、状态、动作、灯亮持续时间、灯灭持续时间。  fruLedProperty表节点OID： iso(1).org(3

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.9
```

---

## componentProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).componentProperty(10)`

**描述**: 获得部件的信息。包括Mezz卡最大个数、部件信息表节点。  componentProperty 节点OID:  iso(1).org(3).dod(6).internet(1).private(4).

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.10
```

---

## lomProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).lomProperty(17)`

**描述**: 板载网卡的MAC地址查询。  lomProperty表节点的OID： iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.17
```

---

## fruInfo

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).fruInfo(19)`

**描述**: 该规格涉及到FRU资产信息的查询，FRU制造信息为表节点，其子节点单板生产厂商、单板产品名称、单板序列号、单板部件号、单板制造日期、单板FRU文件ID、产品生产厂商、产品名称、产品序列号、产品部件号、

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.19
```

---

## pCIeDeviceProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiMana(1). pCIeDeviceProperty(24).`

**描述**: 该PCIe信息为服务器PCIe信息。包括PCIe整体健康状态，PCIe最大个数，PCIe信息为表节点，其子节点PCIe在位，单体PCIe健康状态，PCIe可用性，PCIe位置，PCIe逻辑分组，PCI

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.22
```

---

## remoteManagement

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). remoteManagement (28)`

**描述**: 该信息为服务器远程管理信息。包括受控上电配置字符串。  remoteManagement表节点的OID： iso(1).org(3).dod(6).internet(1).private(4).ent

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.26
```

---

## snmpMIBConfig

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). snmpMIBConfig (29)`

**描述**: snmpMIBConfig信息snmp的相关配置，其子节点snmpV3Algorithm 当前通信采用的加密和鉴权算法。  snmpMIBConfig模块节点的OID： iso(1).org(3).d

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.27
```

---

## certificate

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). certificate (31). currentCertInfo(1)`

**描述**: certificate提供证书的相关操作，其下子目录：  ●	currentCertInfo为当前证书信息 ●	csrRequestInfo为请求证书的相关操作 ●	customCertInsert为

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.29
```

---

## securityModuleProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).securityModuleProperty(33)`

**描述**: 安全模块信息，包括安全模块在位、协议类型、协议版本、厂商名称、固件版本等信息。  securityModuleProperty表节点的OID： iso(1).org(3).dod(6).interne

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.31
```

---

## fileTransfer

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).fileTransfer(35)`

**描述**: 文件传输功能信息，包括设置文件传输url，查询文件传输状态信息。  fileTransfer表节点的OID： iso(1).org(3).dod(6).internet(1).private(4).e

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.33
```

---

## raidControllerProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).raidControllerProperty(36)`

**描述**: RAID控制器的信息，包括控制器的名称、类型、健康状态、firmware版本、接口类型、内存ECC计数、BBU型号等信息。  raidControllerProperty表节点的OID为：  iso(

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.34
```

---

## remoteControl

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). remoteControl (40)`

**描述**: 该信息为服务器远程控制信息。包括本地KVM使能状态。  remoteControl表节点的OID： iso(1).org(3).dod(6).internet(1).private(4).enterp

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.37
```

---

## twoFactorAuthentication

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). twoFactorAuthentication (41)`

**描述**: 该信息为双因素认证信息。包括功能使能、根证书管理、客户端证书管理。  twoFactorAuthentication表节点的OID： iso(1).org(3).dod(6).internet(1).

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.38
```

---

## configuration

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). configuration (42)`

**描述**: 导入导出BMC、BIOS和RAID控制器配置项，包括启动导出BMC、BIOS和RAID控制器配置，启动导入BMC、BIOS和RAID控制器配置，查询配置导入和导出的状态（导入导出进度或错误信息）。  

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.39
```

---

## businessPortProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). businessPortProperty (43).`

**描述**: 该businessPort信息为服务器网卡网口信息。包括网卡的网口部件丝印信息、网口位置信息、网口的Link状态、网口的Mac地址信息和网口的BDF信息等属性。businessPort信息为表节点，其

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.40
```

---

## shelf

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).shelf(44)`

**描述**: 用于展示机框位置，机框ID，机框类型，机框的健康状态，机框部件号，机框序列号，机框出风口温度。  shelf表节点的OID:  iso(1).org(3).dod(6).internet(1).pri

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.41
```

---

