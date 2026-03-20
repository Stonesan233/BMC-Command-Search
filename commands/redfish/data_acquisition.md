# Redfish 数据采集接口

> 共 8 个接口 (有效: 6, 有请求体: 8)

## 查询数据采集服务资源

**章节**: 3.11.1

**方法**: GET

**URL**: `/redfish/v1/DataAcquisitionService`

**描述**: 查询数据采集服务资源。本资源受许可证控制，需要通过许可证授权后才能使用。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/DataAcquisitionService'
```

---

## 修改数据采集服务开关状态

**章节**: 3.11.2

**方法**: PATCH

**URL**: `/redfish/v1/DataAcquisitionService`

**描述**: 打开/关闭数据采集服务。本资源受许可证控制，需要通过许可证授权后才能使用。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/DataAcquisitionService' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content" }'
```

---

## 导出数据表

**章节**: 3.11.3

**方法**: POST

**URL**: `/redfish/v1/DataAcquisitionService/Actions/`

**描述**: 导出对应的数据库表，导出格式：csv文件。本资源受许可证控制，需要通过许可证授  权后才能使用。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/DataAcquisitionService/Actions/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content" }'
```

---

## 查询导出进度

**章节**: 3.11.4

**描述**: 查询导出进度

**请求体**:
```json
{
  "Type": "text",
  "Content": "content",
  "Password": "123"
}
```

**curl命令**:
```bash
# 查询导出进度
```

---

## 清空“数据采集点信息表”

**章节**: 3.11.6

**方法**: POST

**URL**: `/redfish/v1/DataAcquisitionService/Actions/`

**描述**: 清空“数据采集点信息表”。本资源受许可证控制，需要通过许可证授权后才能使用。

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/DataAcquisitionService/Actions/' -H 'Content-Type: application/json' -d '{  "MemberId": "0" }'
```

---

## 查询清空进度

**章节**: 3.11.7

**描述**: 查询清空进度

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
# 查询清空进度
```

---

## 查询数据表资源信息

**章节**: 3.11.8

**方法**: GET

**URL**: `/redfish/v1/DataAcquisitionService/`

**描述**: 查询数据表资源信息

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/DataAcquisitionService/'
```

---

## 创建数据表格筛选任务

**章节**: 3.11.9

**方法**: POST

**URL**: `/redfish/v1/DataAcquisitionService/Actions/`

**描述**: 创建对数据表的筛选任务。本资源受许可证控制，需要通过许可证授权后才能使用。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/DataAcquisitionService/Actions/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

