# SNMP 散热命令

> 共 2 个命令 (有效: 1)

## fanProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).fanProperty(8)`

**描述**: 风扇管理，包括风扇模式、风扇全局转速百分比、风扇整体健康状况，单个风扇实际转速(RPM)、单个风扇在位状态、单个风扇健康状态、丝印信息、单个风扇转速百分比等。  fanProperty表节点的OID：

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.8
```

---

## temperatureProperty

**描述**: 索引与温度实体对应关系如下表：  Atlas 系列硬件产品 iBMC 300 SNMP 接口参考   # 5 MIB 表详细规格

**命令**:
```bash
# temperatureProperty
```

---

