# SNMP 固件命令

> 共 2 个命令 (有效: 2)

## firmwareProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).firmwareProperty(11)`

**描述**: 固件版本信息，包括固件名称、固件类型、固件发布时间日期、固件版本、固件位置号信息管理。  firmwareProperty表节点的OID： iso(1).org(3).dod(6).internet(

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.11
```

---

## firmwareUpgrade

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). firmwareUpgrade (30)`

**描述**: firmwareUpgrade提供升级功能，其子节点firmwareUpgradeStart为启动升级功能, firmwareUpgradeState查询升级状态及进度，firmwareUpgrade

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.28
```

---

