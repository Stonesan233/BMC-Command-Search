# Redfish Redfish版本接口

> 共 1 个接口 (有效: 1, 有请求体: 1)

## 查询Redfish 版本信息

**章节**: 3.1.1

**方法**: GET

**URL**: `/redfish`

**描述**: 查询当前使用的Redfish协议的版本号。

**请求体**:
```json
{
  "v1": "/redfish/v1/"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish'
```

---

