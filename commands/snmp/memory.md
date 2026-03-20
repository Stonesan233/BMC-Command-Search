# SNMP 内存命令

> 共 1 个命令 (有效: 1)

## memoryProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).memoryProperty(16)`

**描述**: 内存的槽位，逻辑通道，制造厂商，容量，主频及丝印等信息。  memoryProperty表节点OID:  iso(1).org(3).dod(6).internet(1).private(4).ent

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.16
```

---

