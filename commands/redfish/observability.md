# Redfish 可观测服务接口

> 共 3 个接口 (有效: 3, 有请求体: 2)

## 查询可观测服务配置资源

**章节**: 3.17.1

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/ObservabilityService`

**描述**: 查询服务器当前可观测服务配置资源。  说明  iBMC300 5.10.0.1及以上版本，当前只针对BMC系统提供可观测服务能力

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCA3.crl"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/ObservabilityService'
```

---

## 设置可观测服务配置资源

**章节**: 3.17.2

**方法**: PATCH

**URL**: `/redfish/v1/Oem/Huawei/ObservabilityService`

**描述**: 修改服务器当前可观测服务配置资源。  说明  iBMC300 5.10.0.1及以上版本，当前只针对BMC系统提供可观测服务能力命令格式 操作类型：PATCH  URL：https://device_...

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Oem/Huawei/ObservabilityService' -H 'Content-Type: application/json' -d '{}'
```

---

## 发送可观测服务测试报文

**章节**: 3.17.3

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/ObservabilityService/Actions/`

**描述**: 发送可观测服务的测试报文，测试连通性。  说明  iBMC300 5.10.0.1及以上版本，当前只针对BMC系统提供可观测服务能力

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/ObservabilityService/Actions/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/c.csr" }'
```

---

