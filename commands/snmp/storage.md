# SNMP 存储命令

> 共 2 个命令 (有效: 2)

## hardDiskProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hardDiskProperty (18)`

**描述**: 硬盘信息，包括单个硬盘的在位、丝印、厂商、序列号、型号、容量、状态等信息。  hardDiskProperty表节点的OID： iso(1).org(3).dod(6).internet(1).pri

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.18
```

---

## diskArrayProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).diskArrayProperty(39)`

**描述**: 磁盘组的信息，包括磁盘组的ID，已使用容量，剩余容量，逻辑盘个数，逻辑盘ID，物理盘个数，物理盘ID，空闲块容量。  diskArrayProperty表节点的OID为：  iso(1).org(3)

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.36
```

---

