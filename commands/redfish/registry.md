# Redfish 注册表接口

> 共 2 个接口 (有效: 2, 有请求体: 0)

## 查询所有归档资源

**章节**: 3.1.8

**方法**: GET

**URL**: `/redfish/v1/Registries`

**描述**: 查询服务器当前所有的归档文件资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Registries'
```

---

## 查询单个归档资源

**章节**: 3.1.9

**方法**: GET

**URL**: `/redfish/v1/Registries/registries_id`

**描述**: 查询服务器当前具体的消息归档文件资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Registries/registries_id'
```

---

