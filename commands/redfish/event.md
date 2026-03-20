# Redfish 事件服务接口

> 共 14 个接口 (有效: 14, 有请求体: 10)

## 查询事件服务资源

**章节**: 3.9.1

**方法**: GET

**URL**: `/redfish/v1/EventService`

**描述**: 查询服务器事件服务资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/EventService'
```

---

## 修改事件服务资源

**章节**: 3.9.2

**方法**: PATCH

**URL**: `/redfish/v1/EventService`

**描述**: 修改事件服务资源，包括修改事件上报开关状态和修改事件主机标识源。

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/EventService' -H 'Content-Type: application/json' -d '{}'
```

---

## 模拟测试事件

**章节**: 3.9.3

**方法**: POST

**URL**: `/redfish/v1/EventService/Actions/`

**描述**: 模拟测试事件。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/EventService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 对未恢复的事件重新上报

**章节**: 3.9.4

**方法**: POST

**URL**: `/redfish/v1/EventService/Actions/Oem/Huawei/`

**描述**: 对未恢复的事件重新上报。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/EventService/Actions/Oem/Huawei/' -H 'Content-Type: application/json' -d '{}'
```

---

## 模拟精准告警

**章节**: 3.9.5

**方法**: POST

**URL**: `/redfish/v1/EventService/Actions/Oem/Huawei/`

**描述**: 模拟精准告警。

**请求体**:
```json
{
  "ServiceEnabled": false,
  "CertVerificationEnabled": false,
  "ServerAddress": "device_ip",
  "ServerPort": 25,
  "TLSEnabled": true,
  "AnonymousLoginEnabled": false,
  "SenderUserName": "huawei",
  "SenderPassword": "Password",
  "SenderAddress": "huawei@outlook.com",
  "EmailSubject": "Server Alert",
  "EmailSubjectContains": [],
  "AlarmSeverity": "Normal",
  "ReportType": "SEL",
  "RecipientAddresses": [
    {
      "Enabled": false,
      "EmailAddress": "smtptest@it.software.com",
      "Description": "smtptest"
    }
  ]
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/EventService/Actions/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": false,  "CertVerificationEnabled": false,  "ServerAddress": "device_ip",  "ServerPort": 25,  "TLSEnabled": true,  "AnonymousLoginEnabled": false,  "SenderUserName": "huawei",  "SenderPassword": "Password",  "SenderAddress": "huawei@outlook.com",  "EmailSubject": "Server Alert",  "EmailSubjectContains": [],  "AlarmSeverity": "Normal",  "ReportType": "SEL",  "RecipientAddresses": [   {    "Enabled": false,    "EmailAddress": "smtptest@it.software.com",    "Description": "smtptest"   }  ] }'
```

---

## 查询事件订阅集合资源

**章节**: 3.9.6

**方法**: GET

**URL**: `/redfish/v1/EventService/Subscriptions`

**描述**: 查询事件订阅集合资源。

**请求体**:
```json
{
  "ServiceEnabled": false,
  "CertVerificationEnabled": false,
  "ServerAddress": "device_ip",
  "ServerPort": 25,
  "TLSEnabled": true,
  "AnonymousLoginEnabled": false,
  "SenderUserName": "huawei",
  "SenderPassword": "Password",
  "SenderAddress": "huawei@outlook.com",
  "EmailSubject": "Server Alert",
  "EmailSubjectContains": [],
  "AlarmSeverity": "Normal",
  "ReportType": "SEL",
  "RecipientAddresses": [
    {
      "Enabled": false,
      "EmailAddress": "smtptest@it.software.com",
      "Description": "smtptest"
    }
  ]
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/EventService/Subscriptions'
```

---

## 创建事件订阅资源

**章节**: 3.9.7

**方法**: POST

**URL**: `/redfish/v1/EventService/Subscriptions`

**描述**: 创建事件订阅资源。

**请求体**:
```json
{
  "ServiceEnabled": false,
  "CertVerificationEnabled": false,
  "ServerAddress": "device_ip",
  "ServerPort": 25,
  "TLSEnabled": true,
  "AnonymousLoginEnabled": false,
  "SenderUserName": "huawei",
  "SenderPassword": "Password",
  "SenderAddress": "huawei@outlook.com",
  "EmailSubject": "Server Alert",
  "EmailSubjectContains": [],
  "AlarmSeverity": "Normal",
  "ReportType": "SEL",
  "RecipientAddresses": [
    {
      "Enabled": false,
      "EmailAddress": "smtptest@it.software.com",
      "Description": "smtptest"
    }
  ]
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/EventService/Subscriptions' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": false,  "CertVerificationEnabled": false,  "ServerAddress": "device_ip",  "ServerPort": 25,  "TLSEnabled": true,  "AnonymousLoginEnabled": false,  "SenderUserName": "huawei",  "SenderPassword": "Password",  "SenderAddress": "huawei@outlook.com",  "EmailSubject": "Server Alert",  "EmailSubjectContains": [],  "AlarmSeverity": "Normal",  "ReportType": "SEL",  "RecipientAddresses": [   {    "Enabled": false,    "EmailAddress": "smtptest@it.software.com",    "Description": "smtptest"   }  ] }'
```

---

## 查询事件订阅资源

**章节**: 3.9.8

**方法**: GET

**URL**: `/redfish/v1/EventService/Subscriptions/id`

**描述**: 查询事件订阅资源。

**请求体**:
```json
{
  "ServiceEnabled": false,
  "CertVerificationEnabled": false,
  "ServerAddress": "device_ip",
  "ServerPort": 25,
  "TLSEnabled": true,
  "AnonymousLoginEnabled": false,
  "SenderUserName": "huawei",
  "SenderPassword": "Password",
  "SenderAddress": "huawei@outlook.com",
  "EmailSubject": "Server Alert",
  "EmailSubjectContains": [],
  "AlarmSeverity": "Normal",
  "ReportType": "SEL",
  "RecipientAddresses": [
    {
      "Enabled": false,
      "EmailAddress": "smtptest@it.software.com",
      "Description": "smtptest"
    }
  ]
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/EventService/Subscriptions/id'
```

---

## 修改事件订阅资源

**章节**: 3.9.9

**方法**: PATCH

**URL**: `/redfish/v1/EventService/Subscriptions/id`

**描述**: 修改事件订阅资源。

**请求体**:
```json
{
  "ServiceEnabled": false,
  "CertVerificationEnabled": false,
  "ServerAddress": "device_ip",
  "ServerPort": 25,
  "TLSEnabled": true,
  "AnonymousLoginEnabled": false,
  "SenderUserName": "huawei",
  "SenderPassword": "Password",
  "SenderAddress": "huawei@outlook.com",
  "EmailSubject": "Server Alert",
  "EmailSubjectContains": [],
  "AlarmSeverity": "Normal",
  "ReportType": "SEL",
  "RecipientAddresses": [
    {
      "Enabled": false,
      "EmailAddress": "smtptest@it.software.com",
      "Description": "smtptest"
    }
  ]
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/EventService/Subscriptions/id' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": false,  "CertVerificationEnabled": false,  "ServerAddress": "device_ip",  "ServerPort": 25,  "TLSEnabled": true,  "AnonymousLoginEnabled": false,  "SenderUserName": "huawei",  "SenderPassword": "Password",  "SenderAddress": "huawei@outlook.com",  "EmailSubject": "Server Alert",  "EmailSubjectContains": [],  "AlarmSeverity": "Normal",  "ReportType": "SEL",  "RecipientAddresses": [   {    "Enabled": false,    "EmailAddress": "smtptest@it.software.com",    "Description": "smtptest"   }  ] }'
```

---

## 删除事件订阅资源

**章节**: 3.9.10

**方法**: DELETE

**URL**: `/redfish/v1/EventService/Subscriptions/id`

**描述**: 删除事件订阅资源。

**请求体**:
```json
{
  "ServiceEnabled": false,
  "CertVerificationEnabled": false,
  "ServerAddress": "device_ip",
  "ServerPort": 25,
  "TLSEnabled": true,
  "AnonymousLoginEnabled": false,
  "SenderUserName": "huawei",
  "SenderPassword": "Password",
  "SenderAddress": "huawei@outlook.com",
  "EmailSubject": "Server Alert",
  "EmailSubjectContains": [],
  "AlarmSeverity": "Normal",
  "ReportType": "SEL",
  "RecipientAddresses": [
    {
      "Enabled": false,
      "EmailAddress": "smtptest@it.software.com",
      "Description": "smtptest"
    }
  ]
}
```

**curl命令**:
```bash
curl -k -u admin:password -X DELETE 'https://<bmc_ip>/redfish/v1/EventService/Subscriptions/id'
```

---

## 屏蔽系统事件上报

**章节**: 3.9.11

**方法**: POST

**URL**: `/redfish/v1/EventService/Actions/Oem/Huawei/`

**描述**: 屏蔽系统事件上报。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/EventService/Actions/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content" }'
```

---

## 配置事件告警级别

**章节**: 3.9.12

**方法**: POST

**URL**: `/redfish/v1/EventService/Actions/Oem/Huawei/`

**描述**: 设置事件告警级别

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/EventService/Actions/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content" }'
```

---

## 恢复订阅事件信息

**章节**: 3.9.13

**方法**: POST

**URL**: `/redfish/v1/EventService/Subscriptions/{id}/Actions/`

**描述**: 恢复发送指定时间范围内的订阅事件信息。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/EventService/Subscriptions/{id}/Actions/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content" }'
```

---

## 暂停订阅事件信息

**章节**: 3.9.14

**方法**: POST

**URL**: `/redfish/v1/EventService/Subscriptions/{id}/Actions/`

**描述**: 暂停订阅事件发送

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/EventService/Subscriptions/{id}/Actions/' -H 'Content-Type: application/json' -d '{  "MemberId": "0" }'
```

---

