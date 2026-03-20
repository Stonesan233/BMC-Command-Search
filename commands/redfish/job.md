# Redfish 作业服务接口

> 共 5 个接口 (有效: 5, 有请求体: 4)

## 查询编排任务服务信息

**章节**: 3.14.1

**方法**: GET

**URL**: `/redfish/v1/JobService`

**描述**: 查询服务器当前编排任务服务信息。  说明 			iBMC300 5.8.0.1及以上版本支持

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/JobService'
```

---

## 修改编排任务服务信息

**章节**: 3.14.2

**方法**: PATCH

**URL**: `/redfish/v1/JobService`

**描述**: 修改服务器当前编排任务的服务信息。  说明 	iBMC300 5.8.0.1及以上版本支持

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/JobService' -H 'Content-Type: application/json' -d '{  "ResetType": "ForceRestart" }'
```

---

## 创建编排任务

**章节**: 3.14.4

**方法**: POST

**URL**: `/redfish/v1/JobService/Jobs`

**描述**: 创建编排任务。  说明  iBMC300 5.8.0.1及以上版本支持

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/JobService/Jobs' -H 'Content-Type: application/json' -d '{  "ResetType": "ForceRestart" }'
```

---

## 查询指定编排任务信息

**章节**: 3.14.5

**方法**: GET

**URL**: `/redfish/v1/JobService/Jobs/job_id`

**描述**: 查询指定编排任务信息

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/JobService/Jobs/job_id'
```

---

## 修改指定编排任务信息

**章节**: 3.14.6

**方法**: PATCH

**URL**: `/redfish/v1/JobService/Jobs/job_id`

**描述**: 修改指定编排任务信息。  说明  iBMC300 5.8.0.1及以上版本支持

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/JobService/Jobs/job_id' -H 'Content-Type: application/json' -d '{}'
```

---

