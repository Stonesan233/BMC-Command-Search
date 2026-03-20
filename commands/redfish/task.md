# Redfish 任务服务接口

> 共 8 个接口 (有效: 8, 有请求体: 8)

## 查询任务服务资源信息

**章节**: 3.8.1

**方法**: GET

**URL**: `/redfish/v1/TaskService`

**描述**: 查询服务器当前任务服务资源的信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TaskService'
```

---

## 查询任务集合资源信息

**章节**: 3.8.2

**方法**: GET

**URL**: `/redfish/v1/TaskService/Tasks`

**描述**: 查询服务器当前任务集合资源的信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TaskService/Tasks'
```

---

## 查询指定任务资源信息

**章节**: 3.8.3

**方法**: GET

**URL**: `/redfish/v1/TaskService/Tasks/taskid`

**描述**: 查询服务器指定任务资源的信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TaskService/Tasks/taskid'
```

---

## 查询指定Monitor 信息

**章节**: 3.8.4

**方法**: GET

**URL**: `/redfish/v1/TaskService/Tasks/task_id/Monitor`

**描述**: 查询服务器指定Monitor的信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TaskService/Tasks/task_id/Monitor'
```

---

## 查询任务集合资源信息

**章节**: 3.10.12

**方法**: GET

**URL**: `/redfish/v1/Sms/1/TaskService/Tasks`

**描述**: 查询服务器当前任务集合资源的信息。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Sms/1/TaskService/Tasks'
```

---

## 查询指定任务资源信息命令功能

**章节**: 3.10.13

**方法**: GET

**URL**: `/redfish/v1/Sms/1/TaskService/Tasks/taskid`

**描述**: 查询指定任务资源信息命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Sms/1/TaskService/Tasks/taskid'
```

---

## 查询导出表

**章节**: 3.11.5

**方法**: GET

**URL**: `/redfish/v1/TaskService/Tasks/task_id/Monitor`

**描述**: 查询服务器指定Monitor的信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TaskService/Tasks/task_id/Monitor'
```

---

## 查询数据表筛选结果

**章节**: 3.11.10

**方法**: GET

**URL**: `/redfish/v1/TaskService/Tasks/task_id/Monitor`

**描述**: 查询指定Monitor的信息，包含数据表筛选结果。本资源受许可证控制，需要通过许可证授权后才能使用。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/TaskService/Tasks/task_id/Monitor'
```

---

