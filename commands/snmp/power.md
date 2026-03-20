# SNMP 电源命令

> 共 5 个命令 (有效: 4)

## powerStatistic

**描述**: powerStatistic

**命令**:
```bash
# powerStatistic
```

---

## powerSupplyInfo

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).powerSupplyInfo(6)`

**描述**: 电源管理，查看电源整体健康状态，查看和设置工作模式、主备切换，获取单个电源制造厂商，单个电源模式，单个电源型号，单个电源版本，及单个电源额定功率，单个电源输入功率，单个电源在位信息，电源丝印，工作模式

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.6
```

---

## fruPowerProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).fruPowerProperty(7).fruPowerDescriptionTa ble(50)`

**描述**: FRU电源的状态信息，提供上电、下电、重启、安全重启、安全下电再上电五种操  作，包含两个表。  fruPowerDescriptionTable表节点OID：  iso(1).org(3).dod(

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.7
```

---

## powerStatistic

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).powerStatistic(20)`

**描述**: 涉及到系统峰值功率，峰值功率产生时间，历史平均功率，累计耗电量，功率统计开始时间，清除功率统计数据，累计消耗热量。  powerStatistic模块节点的OID： iso(1).org(3).dod

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.20
```

---

## powerManagement

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).powerManagement(23)`

**描述**: 涉及到系统当前功率，功率封顶启用状态，功率封顶值，功率封顶失败时进一步动作。  powerManagement模块节点的OID： iso(1).org(3).dod(6).internet(1).pr

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.21
```

---

