# SNMP 网络命令

> 共 2 个命令 (有效: 2)

## networkProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).networkProperty(12)`

**描述**: 网络信息节点为表节点，其子节点eth号、IP地址、子网掩码、默认网关、IP模式、MAC地址、网口类型、边带网口、网络使能（已废弃）、网络模式、vlanID、网络信息IPv4启用状态为叶子节点，该网络信

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.12
```

---

## networkTimeProtocol

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1). networkTimeProtocol (27)`

**描述**: 网络时间协议的信息，包括当前单板是否支持NTP同步时间，使能状态，主NTP服务器地址，备NTP服务器地址，NTP服务器源（手动或自动），绑定的IP协议版本，NTP时间同步周期等信息。  NTP主备服务

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.25
```

---

