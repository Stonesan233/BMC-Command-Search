# SNMP 传感器命令

> 共 1 个命令 (有效: 1)

## sensorProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).sensorProperty(13).sensorDescriptionTable( 50).sensorDescriptionEntry(1)`

**描述**: 传感器的值的查询（已废弃）。  传感器信息表节点OID：  iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.13
```

---

