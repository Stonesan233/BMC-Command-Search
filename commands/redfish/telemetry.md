# Redfish 遥测服务接口

> 共 20 个接口 (有效: 20, 有请求体: 12)

## 查询遥测服务资源信息

**章节**: 3.15.1

**方法**: GET

**URL**: `/redfish/v1/TelemetryService`

**描述**: 查询服务器当前遥测服务资源。  说明 			iBMC300 5.9.0.1及以上版本支持

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService'
```

---

## 修改遥测服务资源信息

**章节**: 3.15.2

**方法**: PATCH

**URL**: `/redfish/v1/TelemetryService`

**描述**: 修改遥测服务资源，设置是否使能遥测服务。  说明  iBMC300 5.9.0.1及以上版本支持

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/TelemetryService' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询指标项资源信息

**章节**: 3.15.3

**方法**: GET

**URL**: `/redfish/v1/TelemetryService/MetricDefinitions`

**描述**: 查询服务器当前指标项集合资源信息。  说明 			iBMC300 5.9.0.1及以上版本支持

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricDefinitions'
```

---

## 查询指定指标定义资源信息

**章节**: 3.15.4

**方法**: GET

**URL**: `/redfish/v1/TelemetryService/MetricDefinitions/id`

**描述**: 查询服务器当前指定指标定义资源信息。  说明  iBMC300 5.9.0.1及以上版本支持   ## 命令格式  操作类型：GET  URL：https://device_ip/redfish/v1...

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricDefinitions/id'
```

---

## 查询指标报告定义资源信息

**章节**: 3.15.5

**方法**: GET

**URL**: `/redfish/v1/TelemetryService/MetricReportDefinitions`

**描述**: 查询服务器当前指标报告定义资源信息。  说明  iBMC300 5.9.0.1及以上版本支持

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricReportDefinitions'
```

---

## 创建指标报告定义资源信息命令功能

**章节**: 3.15.6

**方法**: POST

**URL**: `/redfish/v1/TelemetryService/MetricReportDefinitions`

**描述**: 创建指标报告定义资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricReportDefinitions' -H 'Content-Type: application/json' -d '{}'
```

---

## 修改指定指标报告定义资源信息

**章节**: 3.15.7

**方法**: PATCH

**URL**: `/redfish/v1/TelemetryService/MetricReportDefinitions/id`

**描述**: 修改服务器当前指定指标报告定义资源信息。  说明 	iBMC300 5.9.0.1及以上版本支持

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricReportDefinitions/id' -H 'Content-Type: application/json' -d '{}'
```

---

## 删除指定指标报告定义

**章节**: 3.15.8

**方法**: DELETE

**URL**: `/redfish/v1/TelemetryService/MetricReportDefinitions/id`

**描述**: 删除服务器当前指定指标报告定义。  说明 			iBMC300 5.9.0.1及以上版本支持

**curl命令**:
```bash
curl -k -u admin:password -X DELETE 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricReportDefinitions/id'
```

---

## 查询指定指标报告定义资源信息

**章节**: 3.15.9

**方法**: GET

**URL**: `/redfish/v1/TelemetryService/MetricReportDefinitions/id`

**描述**: 查询服务器当前指定指标报告定义资源信息。  说明 	iBMC300 5.9.0.1及以上版本支持

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricReportDefinitions/id'
```

---

## 查询指标报告集合资源信息命令功能

**章节**: 3.15.10

**方法**: GET

**URL**: `/redfish/v1/TelemetryService/MetricReports`

**描述**: 查询指标报告集合资源信息命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricReports'
```

---

## 查询指定指标报告资源信息

**章节**: 3.15.11

**方法**: GET

**URL**: `/redfish/v1/TelemetryService/MetricReports/id`

**描述**: 查询服务器当前指标报告集合资源信息。  说明  iBMC300 5.9.0.1及以上版本支持   ## 命令格式  操作类型：GET  URL：https://device_ip/redfish/v1...

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService/MetricReports/id'
```

---

## 查询触发器集合资源信息

**章节**: 3.15.12

**方法**: GET

**URL**: `/redfish/v1/TelemetryService/Triggers`

**描述**: 查询服务器当前触发器集合资源信息。  说明 			iBMC300 5.9.0.1及以上版本支持

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService/Triggers'
```

---

## 创建触发器

**章节**: 3.15.13

**方法**: POST

**URL**: `/redfish/v1/TelemetryService/Triggers`

**描述**: 创建触发器。  iBMC300 5.9.0.1及以上版本支持   ## 命令格式  操作类型：POST  URL：https://device_ip/redfish/v1/TelemetryServi...

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/TelemetryService/Triggers' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 查询指定触发器资源信息

**章节**: 3.15.14

**方法**: GET

**URL**: `/redfish/v1/TelemetryService/Triggers/id`

**描述**: 查询服务器当前指定触发器资源信息。  说明  iBMC300 5.9.0.1及以上版本支持

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TelemetryService/Triggers/id'
```

---

## 修改指定触发器资源信息

**章节**: 3.15.15

**方法**: PATCH

**URL**: `/redfish/v1/TelemetryService/Triggers/id`

**描述**: 修改服务器当前指定触发器资源信息。  说明  iBMC300 5.9.0.1及以上版本支持   ## 命令格式  操作类型：PATCH  URL：https://device_ip/redfish/v...

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/TelemetryService/Triggers/id' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 删除指定触发器

**章节**: 3.15.16

**方法**: DELETE

**URL**: `/redfish/v1/TelemetryService/Triggers/id`

**描述**: 删除服务器当前指定触发器。  说明 			iBMC300 5.9.0.1及以上版本支持

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X DELETE 'https://<bmc_ip>/redfish/v1/TelemetryService/Triggers/id'
```

---

## 提交测试指标报告上报

**章节**: 3.15.17

**方法**: POST

**URL**: `/redfish/v1/TelemetryService/Actions/`

**描述**: 提交测试指标报告。  说明 	iBMC300 5.9.0.1及以上版本支持

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/TelemetryService/Actions/' -H 'Content-Type: application/json' -d '{  "RootCertId": 1 }'
```

---

## 清除指标报告

**章节**: 3.15.18

**方法**: POST

**URL**: `/redfish/v1/TelemetryService/Actions/`

**描述**: 清除指标报告

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/TelemetryService/Actions/' -H 'Content-Type: application/json' -d '{  "RootCertId": 1 }'
```

---

## 恢复指标报告定义到默认值命令功能

**章节**: 3.15.19

**方法**: POST

**URL**: `/redfish/v1/TelemetryService/Actions/`

**描述**: 恢复指标报告定义到默认值命令功能

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/TelemetryService/Actions/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "123",  "RootCertId": 1 }'
```

---

## 恢复触发器到默认值

**章节**: 3.15.20

**方法**: POST

**URL**: `/redfish/v1/TelemetryService/Actions/`

**描述**: 恢复触发器到默认值。  说明 			iBMC300 5.9.0.1及以上版本支持

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/TelemetryService/Actions/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "123",  "RootCertId": 1 }'
```

---

