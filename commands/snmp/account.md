# SNMP 账户命令

> 共 1 个命令 (有效: 1)

## userProperty

**OID**: `iso(1).org(3).dod(6).internet(1).private(4).enterprises(1).huawei(2011).products(2) .hwServer(235).hwBMC(1).hwiBMC(1).userProperty(14).userDescriptionTable(50)节点userDescriptionEntry是描述表节点userDescriptionTable组成成分的。`

**描述**: 管理本地用户的用户名、用户使能、用户ID、用户密码和用户组，以及支持删除用户信息。  userDescriptionTable表节点的OID： iso(1).org(3).dod(6).interne

**命令**:
```bash
snmpwalk -v2c -c public <bmc_ip> .1.3.6.1.4.1.2011.2.235.1.1.14
```

---

