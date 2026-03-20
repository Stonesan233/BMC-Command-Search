# Redfish 资产管理接口

> 共 5 个接口 (有效: 5, 有请求体: 5)

## 查询资源服务信息

**章节**: 3.13.1

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/AssetService`

**描述**: 查询服务器当前资源服务信息。

**请求体**:
```json
{
  "HostName": "huawei"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/AssetService'
```

---

## 查询硬件资产清单信息

**章节**: 3.13.2

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/AssetService/AssetList`

**描述**: 查询服务器当前硬件资产信息。

**请求体**:
```json
{
  "HostName": "huawei"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/AssetService/AssetList'
```

---

## 查询硬件资产变更信息

**章节**: 3.13.3

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/AssetService/AssetChange`

**描述**: 查询服务器当前资产变更信息

**请求体**:
```json
{
  "HostName": "huawei"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/AssetService/AssetChange'
```

---

## 刷新硬件资产变更信息

**章节**: 3.13.4

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/AssetService/AssetChange/`

**描述**: 刷新服务器当前资产变更信息。

**请求体**:
```json
{
  "HostName": "huawei"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/AssetService/AssetChange/' -H 'Content-Type: application/json' -d '{  "HostName": "huawei" }'
```

---

## 确认供应链配置检查信息命令功能

**章节**: 3.13.5

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/AssetService/Actions/`

**描述**: 确认供应链配置检查信息命令功能

**请求体**:
```json
{
  "HostName": "huawei"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/AssetService/Actions/' -H 'Content-Type: application/json' -d '{  "HostName": "huawei" }'
```

---

