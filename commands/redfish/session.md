# Redfish 会话管理接口

> 共 8 个接口 (有效: 8, 有请求体: 5)

## 查询会话服务信息

**章节**: 3.5.1

**方法**: GET

**URL**: `/redfish/v1/SessionService`

**描述**: 查询服务器当前会话服务的信息。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/SessionService'
```

---

## 修改会话服务信息

**章节**: 3.5.2

**方法**: PATCH

**URL**: `/redfish/v1/SessionService`

**描述**: 修改服务器当前会话服务的超时时间。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/SessionService' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 创建会话

**章节**: 3.5.3

**方法**: POST

**URL**: `/redfish/v1/SessionService/Sessions`

**描述**: 创建新会话。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/SessionService/Sessions' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 查询会话集合资源信息

**章节**: 3.5.4

**方法**: GET

**URL**: `/redfish/v1/SessionService/Sessions`

**描述**: 查询服务器当前会话集合资源信息。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/SessionService/Sessions'
```

---

## 查询指定会话资源信息

**章节**: 3.5.5

**方法**: GET

**URL**: `/redfish/v1/SessionService/Sessions/session_id`

**描述**: 查询服务器指定会话资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/SessionService/Sessions/session_id'
```

---

## 删除指定会话

**章节**: 3.5.6

**方法**: DELETE

**URL**: `/redfish/v1/SessionService/Sessions/session_id`

**描述**: 删除指定会话。

**curl命令**:
```bash
curl -k -u admin:password -X DELETE 'https://<bmc_ip>/redfish/v1/SessionService/Sessions/session_id'
```

---

## 创建Web 会话

**章节**: 3.5.7

**方法**: POST

**URL**: `/redfish/v1/SessionService/Sessions`

**描述**: 创建新会话，Web使用此会话可通过Redfish接口获取和设置信息。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/SessionService/Sessions' -H 'Content-Type: application/json' -d '{}'
```

---

## Web 执行操作

**章节**: 3.5.8

**方法**: GET

**URL**: `/redfish/v1/SessionService/Sessions`

**描述**: 使用Web会话通过Redfish接口执行查询、设置操作。所有请求中不再携带X-Auth-Token，所有操作响应头中不再返回“ETag”参数，PATCH操作请求头不再携带“If-Match”。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/SessionService/Sessions'
```

---

