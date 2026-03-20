# Redfish Schema文档接口

> 共 2 个接口 (有效: 2, 有请求体: 0)

## 查询单个Schema 文件归档地址

**章节**: 3.1.6

**方法**: GET

**URL**: `/redfish/v1/JSONSchemas/member_id`

**描述**: 查询服务器当前的单个Schema文件归档地址。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/JSONSchemas/member_id'
```

---

## 查询单个Schema 文件资源

**章节**: 3.1.7

**方法**: GET

**URL**: `/redfish/v1/SchemaStore/language_id/file_id`

**描述**: 查询服务器当前单个Schema文件资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/SchemaStore/language_id/file_id'
```

---

