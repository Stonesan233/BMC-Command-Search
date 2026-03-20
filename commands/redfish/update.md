# Redfish 更新服务接口

> 共 14 个接口 (有效: 14, 有请求体: 14)

## 查询升级服务资源信息

**章节**: 3.7.1

**方法**: GET

**URL**: `/redfish/v1/UpdateService`

**描述**: 查询服务器当前升级服务资源的信息。

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/UpdateService'
```

---

## 修改升级服务信息

**章节**: 3.7.2

**方法**: PATCH

**URL**: `/redfish/v1/UpdateService`

**描述**: 修改升级服务资源，设置是否允许降级升级。

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/UpdateService' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Disconnect" }'
```

---

## 查询可升级固件集合资源信息

**章节**: 3.7.3

**方法**: GET

**URL**: `/redfish/v1/UpdateService/FirmwareInventory`

**描述**: 查询服务器当前可升级的固件集合资源的信息。

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/UpdateService/FirmwareInventory'
```

---

## 查询指定可升级固件资源信息

**章节**: 3.7.4

**方法**: GET

**URL**: `/redfish/v1/UpdateService/FirmwareInventory/softid`

**描述**: 查询服务器指定的可升级固件资源的信息。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/UpdateService/FirmwareInventory/softid'
```

---

## 升级固件

**章节**: 3.7.5

**方法**: POST

**URL**: `/redfish/v1/UpdateService/Actions/`

**描述**: 升级服务器固件。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/UpdateService/Actions/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 文件上传

**章节**: 3.7.6

**方法**: POST

**URL**: `/redfish/v1/UpdateService/FirmwareInventory`

**描述**: 通过redfish接口进行文件上传，上传成功后文件被放在/tmp/web目录下。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/UpdateService/FirmwareInventory' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 生效固件

**章节**: 3.7.7

**方法**: POST

**URL**: `/redfish/v1/UpdateService/Actions/Oem/Huawei/`

**描述**: 所有待生效固件开始生效

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/UpdateService/Actions/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 并行升级

**章节**: 3.7.8

**方法**: POST

**URL**: `/redfish/v1/UpdateService/Actions/Oem/Huawei/`

**描述**: 执行并行升级

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/UpdateService/Actions/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 带内升级软件/固件

**章节**: 3.10.2

**方法**: POST

**URL**: `/redfish/v1/Sms/1/UpdateService/Actions/`

**描述**: 设置iBMA下载相关升级包的参数信息，如升级包路径，升级包类型等并启动升级。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Sms/1/UpdateService/Actions/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content" }'
```

---

## 查询升级进度

**章节**: 3.10.3

**方法**: GET

**URL**: `/redfish/v1/Sms/1/UpdateService/Progress`

**描述**: 查询升级进度。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Sms/1/UpdateService/Progress'
```

---

## 查询带内升级软件集合资源信息命令功能

**章节**: 3.10.4

**方法**: GET

**URL**: `/redfish/v1/Sms/1/UpdateService/SoftwareInventory`

**描述**: 查询带内升级软件集合资源信息命令功能

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Sms/1/UpdateService/SoftwareInventory'
```

---

## 查询指定带内升级软件资源信息命令功能

**章节**: 3.10.5

**方法**: GET

**URL**: `/redfish/v1/Sms/1/UpdateService/SoftwareInventory/{item}`

**描述**: 查询指定带内升级软件资源信息命令功能

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Sms/1/UpdateService/SoftwareInventory/{item}'
```

---

## 查询带内升级固件集合资源信息

**章节**: 3.10.6

**方法**: GET

**URL**: `/redfish/v1/Sms/1/UpdateService/FirmwareInventory`

**描述**: 查询iBMA升级服务固件清单相关资源。

**请求体**:
```json
{
  "ServiceEnabled": true
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Sms/1/UpdateService/FirmwareInventory'
```

---

## 查询指定带内升级固件资源信息命令功能

**章节**: 3.10.7

**方法**: GET

**URL**: `/redfish/v1/Sms/1/UpdateService/FirmwareInventory/{item}`

**描述**: 查询指定带内升级固件资源信息命令功能

**请求体**:
```json
{
  "ServiceEnabled": true
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Sms/1/UpdateService/FirmwareInventory/{item}'
```

---

