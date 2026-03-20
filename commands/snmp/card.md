# SNMP 板卡命令

> 共 3 个命令 (有效: 2)

## netCardProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).netCardProperty(25).netCardDescriptionTab le(50)`

**描述**: 该netCard信息为服务器netCard信息。包括网卡的部件位置信息，网卡的部件功能信  息，网卡的部件设备名称，网卡型号，网卡类型，网卡名称，网卡芯片型号，网卡厂商，网卡芯片厂商，网卡驱动名称，网

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.23
```

---

## SDCardProperty

**描述**: Atlas 系列硬件产品 iBMC 300 SNMP 接口参考   # 5 MIB 表详细规格

**命令**:
```bash
# SDCardProperty
```

---

## oCPCardProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1). hwiBMC (1). oCPCardProperty (46)`

**描述**: 该OCPCard信息为服务器OCP卡信息。包括OCPCard整体健康状态，OCPCard最大个数，OCPCard信息为表节点，其子节点OCPCard在位，单体OCPCard健康状态，OCPCard可用

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.42
```

---

