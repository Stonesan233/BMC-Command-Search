# Redfish LCN服务接口

> 共 17 个接口 (有效: 17, 有请求体: 16)

## 查询LCNService 资源

**章节**: 3.16.1

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/LCNService`

**描述**: 查询服务器当前LCNService资源。  说明  iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支持...

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService'
```

---

## 查询LCN 设备集合信息

**章节**: 3.16.2

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices`

**描述**: 查询LCN设备集合资源的信息。  说明  iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支持

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices'
```

---

## 查询指定LCN 设备信息

**章节**: 3.16.3

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 查询指定LCN设备信息。  iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支			持

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/'
```

---

## 修改指定LCN 设备信息

**章节**: 3.16.4

**方法**: PATCH

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 修改指定LCN设备信息。  说明  iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支  持

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 查询LCN 设备子卡集合信息命令功能

**章节**: 3.16.5

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 查询LCN 设备子卡集合信息命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/'
```

---

## 查询指定LCN 设备子卡信息

**章节**: 3.16.6

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 查询指定LCN设备子卡信息。  说明 iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支持

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/'
```

---

## 查询LCN 设备用户信息

**章节**: 3.16.7

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 查询LCN设备用户信息。  说明  iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支  持

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/'
```

---

## 导出指定LCN 设备日志

**章节**: 3.16.8

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 导出指定LCN设备日志。  说明 				iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支				持

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "RootCertId": 1 }'
```

---

## 设置与指定LCN 设备通信的内部网络命令功能

**章节**: 3.16.9

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 设置与指定LCN 设备通信的内部网络命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": "123",
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "123",  "RootCertId": 1 }'
```

---

## 设置指定LCN 设备的网络接口命令功能

**章节**: 3.16.10

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 设置指定LCN 设备的网络接口命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": "123",
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "123",  "RootCertId": 1 }'
```

---

## 创建指定LCN 设备的用户

**章节**: 3.16.11

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 创建指定LCN设备的用户。  iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支持   ## 命令格式 ...

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCA3.crl"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/HuaweiCA3.crl" }'
```

---

## 删除指定LCN 设备的用户

**章节**: 3.16.12

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 删除指定LCN设备的用户。  说明  iBMC300 5.8.3.27及以上版本，Atlas900 A3 SuperPod，Atlas 800T A3，Atlas 800I A3机型支持

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{}'
```

---

## 修改指定LCN 设备的用户密码命令功能

**章节**: 3.16.13

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 修改指定LCN 设备的用户密码命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/c.csr" }'
```

---

## 重启指定LCN 设备

**章节**: 3.16.14

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 重启指定的LCN设备。  说明 	iBMC300 5.8.3.51及以上版本，Atlas 800T A3，Atlas 800I A3机型支持

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/c.csr" }'
```

---

## 重启指定LCN 设备并恢复默认出厂配置命令功能

**章节**: 3.16.15

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 重启指定LCN 设备并恢复默认出厂配置命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/c.csr" }'
```

---

## 查询指定LCN 设备升级服务的资源信息命令功能

**章节**: 3.16.16

**方法**: GET

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 查询指定LCN 设备升级服务的资源信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/'
```

---

## 升级指定LCN 设备的系统软件命令功能

**章节**: 3.16.17

**方法**: POST

**URL**: `/redfish/v1/Oem/Huawei/LCNService/LCNDevices/`

**描述**: 升级指定LCN 设备的系统软件命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Oem/Huawei/LCNService/LCNDevices/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/c.csr" }'
```

---

