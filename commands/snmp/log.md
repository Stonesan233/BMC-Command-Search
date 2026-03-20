# SNMP 日志命令

> 共 1 个命令 (有效: 1)

## logicalDriveProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).logicalDriveProperty(37)`

**描述**: 逻辑盘的信息，包括逻辑盘的RAID级别，状态，读写策略，大小，条带大小，一致性  检查状态等信息。  logicalDriveProperty表节点的OID为：  iso(1).org(3).dod(

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.35
```

---

