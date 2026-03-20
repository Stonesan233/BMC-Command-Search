# Redfish 管理器接口

> 共 167 个接口 (有效: 163, 有请求体: 96)

## 查询管理集合资源信息

**章节**: 3.2.1

**方法**: GET

**URL**: `/redfish/v1/Managers`

**描述**: 查询服务器当前管理集合资源的信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers'
```

---

## 查询指定管理资源信息

**章节**: 3.2.2

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id`

**描述**: 查询服务器指定管理资源信息，当前仅可查询服务器自身iBMC管理资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id'
```

---

## 修改指定管理资源信息

**章节**: 3.2.3

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id`

**描述**: 修改服务器指定管理资源信息

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id' -H 'Content-Type: application/json' -d '{}'
```

---

## 卸载语言

**章节**: 3.2.4

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 卸载语言

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{}'
```

---

## 恢复出厂设置（自定义接口）

**章节**: 3.2.5

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 恢复出厂设置

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{}'
```

---

## 一键收集

**章节**: 3.2.6

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 收集单板所有模块的维护相关信息

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导入BIOS、BMC 和RAID 控制器配置

**章节**: 3.2.7

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 导入BIOS、BMC和RAID控制器配置 注：导入BIOS配置资源表示已下发BIOS setup项，但当前还未生效，下次系统重启时生效。下电状态导入RAID控制器配置，在下次系统重启时生效。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导出BIOS、BMC 和RAID 控制器配置

**章节**: 3.2.8

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 导出BIOS、BMC和RAID控制器配置。  注：RAID控制器配置需在操作系统重启完成之后导出才有效。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{}'
```

---

## 下载BMC 文件

**章节**: 3.2.9

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 下载BMC文件

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{}'
```

---

## 进入最小系统

**章节**: 3.2.10

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 进入最小系统

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询虚拟媒体集合资源

**章节**: 3.2.11

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/VirtualMedia`

**描述**: 查询虚拟媒体集合资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VirtualMedia'
```

---

## 查询虚拟媒体资源

**章节**: 3.2.12

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/VirtualMedia/CD`

**描述**: 查询虚拟媒体资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VirtualMedia/CD'
```

---

## 设置虚拟媒体资源

**章节**: 3.2.13

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/VirtualMedia/CD`

**描述**: 设置虚拟媒体资源

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VirtualMedia/CD' -H 'Content-Type: application/json' -d '{}'
```

---

## 连接虚拟媒体

**章节**: 3.2.14

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/`

**描述**: 连接虚拟媒体

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/' -H 'Content-Type: application/json' -d '{}'
```

---

## 断开虚拟媒体

**章节**: 3.2.15

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/`

**描述**: 断开虚拟媒体

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询虚拟SP U 盘资源

**章节**: 3.2.16

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/VirtualMedia/`

**描述**: 查询虚拟SP U盘资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VirtualMedia/'
```

---

## 查询虚拟iBMA U 盘资源

**章节**: 3.2.17

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/VirtualMedia/`

**描述**: 查询虚拟iBMA U盘资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VirtualMedia/'
```

---

## 连接虚拟iBMA U 盘

**章节**: 3.2.18

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/VirtualMedia/`

**描述**: 连接虚拟iBMA U盘

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VirtualMedia/' -H 'Content-Type: application/json' -d '{}'
```

---

## 断开虚拟iBMA U 盘

**章节**: 3.2.19

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/VirtualMedia/`

**描述**: 断开虚拟iBMA U盘

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VirtualMedia/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询NTP 配置资源信息

**章节**: 3.2.20

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/NtpService`

**描述**: 查询NTP配置资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NtpService'
```

---

## 修改NTP 资源属性

**章节**: 3.2.21

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/NtpService`

**描述**: NTP资源属性设置

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NtpService' -H 'Content-Type: application/json' -d '{}'
```

---

## 上传NTP 组密钥

**章节**: 3.2.22

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/NtpService/Actions/`

**描述**: NTP组密钥导入。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NtpService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询SNMP 资源信息

**章节**: 3.2.23

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SnmpService`

**描述**: 查询服务器SNMP资源信息。   ## 命令格式  操作类型：GET  URL：https://device_ip/redfish/v1/Managers/manager_id/SnmpService...

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SnmpService'
```

---

## 修改SNMP 资源属性

**章节**: 3.2.24

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SnmpService`

**描述**: 修改服务器SNMP资源属性信息。

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SnmpService' -H 'Content-Type: application/json' -d '{}'
```

---

## 修改指定用户SNMP v3 加密密码

**章节**: 3.2.25

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SnmpService/Actions/`

**描述**: 修改指定用户SNMP v3加密密码。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SnmpService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## SNMP 发送测试事件

**章节**: 3.2.26

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SnmpService/Actions/`

**描述**: SNMP发送测试事件。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SnmpService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询SMTP 资源信息

**章节**: 3.2.27

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SmtpService`

**描述**: 查询SMTP资源信息

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SmtpService'
```

---

## 修改SMTP 资源属性

**章节**: 3.2.28

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SmtpService`

**描述**: 修改SMTP资源属性

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SmtpService' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 导入SMTP 根证书

**章节**: 3.2.29

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SmtpService/Actions/`

**描述**: 导入Smtp根证书  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2.0.1版本后CA...

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SmtpService/Actions/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 发送SMTP 测试邮件

**章节**: 3.2.30

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SmtpService/Actions/`

**描述**: 发送SMTP测试邮件

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SmtpService/Actions/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 查询Syslog 资源信息

**章节**: 3.2.31

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SyslogService`

**描述**: 查询Syslog资源信息

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SyslogService'
```

---

## 修改指定Syslog 资源信息

**章节**: 3.2.32

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SyslogService`

**描述**: Syslog资源属性设置

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SyslogService' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 导入Syslog 根证书

**章节**: 3.2.33

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SyslogService/`

**描述**: 导入Syslog根证书  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2.0.1版本后...

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SyslogService/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 导入Syslog 本地证书

**章节**: 3.2.34

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SyslogService/`

**描述**: 导入Syslog本地证书  此资源已经废弃，仅供兼容性用途使用。归一到/redfish/v1/Managers/manager_id/ SecurityService/HttpsCert进行管理   ...

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SyslogService/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## Syslog 发送测试事件

**章节**: 3.2.35

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SyslogService/`

**描述**: 发送测试事件

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SyslogService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导入Syslog 服务器证书吊销列表

**章节**: 3.2.36

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SyslogService/`

**描述**: 导入Syslog服务器证书吊销列表。  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2...

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SyslogService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 删除Syslog 服务器证书吊销列表

**章节**: 3.2.37

**描述**: 删除Syslog服务器证书吊销列表。  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2...

**curl命令**:
```bash
# 删除Syslog 服务器证书吊销列表
```

---

## 查询KVM 资源

**章节**: 3.2.38

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/KvmService`

**描述**: 查询KVM资源。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/KvmService'
```

---

## 修改KVM 资源属性

**章节**: 3.2.39

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/KvmService`

**描述**: 修改KVM资源属性

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/KvmService' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 设置KVM Key

**章节**: 3.2.40

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/KvmService/Actions/`

**描述**: 设置KVM Key。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/KvmService/Actions/' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 查询iBMC 网口集合资源信息

**章节**: 3.2.41

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/EthernetInterfaces`

**描述**: 查询服务器指定管理资源的网口集合信息，当前仅可查询iBMC管理资源的网口集合资源信息。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/EthernetInterfaces'
```

---

## 查询指定iBMC 网口资源信息

**章节**: 3.2.42

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/EthernetInterfaces/`

**描述**: 查询服务器指定iBMC网口资源信息，当前仅可查询iBMC管理网口的资源信息。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/EthernetInterfaces/'
```

---

## 修改指定iBMC 网口信息

**章节**: 3.2.43

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/EthernetInterfaces/`

**描述**: 修改服务器指定iBMC网口的信息，当前仅可修改iBMC管理网口的信息。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/EthernetInterfaces/' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 查询iBMC 服务信息

**章节**: 3.2.44

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/NetworkProtocol`

**描述**: 查询服务器当前iBMC支持的服务指定状态及端口信息。

**请求体**:
```json
{
  "Oem": {
    "Huawei": {
      "EncryptionEnabled": false,
      "FloppyDriveEnabled": true
    }
  }
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NetworkProtocol'
```

---

## 修改iBMC 服务信息

**章节**: 3.2.45

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/NetworkProtocol`

**描述**: 修改服务器iBMC指定服务的使能状态及端口号。

**请求体**:
```json
{
  "Oem": {
    "Huawei": {
      "EncryptionEnabled": false,
      "FloppyDriveEnabled": true
    }
  }
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NetworkProtocol' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 重启iBMC

**章节**: 3.2.46

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/`

**描述**: 重启iBMC。

**请求体**:
```json
{
  "Oem": {
    "Huawei": {
      "EncryptionEnabled": false,
      "FloppyDriveEnabled": true
    }
  }
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 切换iBMC 镜像

**章节**: 3.2.47

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 切换iBMC镜像。

**请求体**:
```json
{
  "Oem": {
    "Huawei": {
      "EncryptionEnabled": false,
      "FloppyDriveEnabled": true
    }
  }
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 查询安全服务集合资源信息

**章节**: 3.2.48

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SecurityService`

**描述**: 查询服务器当前支持的安全服务集合的信息。

**请求体**:
```json
{
  "Oem": {
    "Huawei": {
      "EncryptionEnabled": false,
      "FloppyDriveEnabled": true
    }
  }
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService'
```

---

## 修改安全服务集合资源信息

**章节**: 3.2.49

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SecurityService`

**描述**: 修改服务器当前支持的安全服务集合的信息。

**请求体**:
```json
{
  "Oem": {
    "Huawei": {
      "EncryptionEnabled": false,
      "FloppyDriveEnabled": true
    }
  }
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 查询安全策略集合资源信息

**章节**: 3.2.50

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SecurityPolicy`

**描述**: 查询服务器当前支持的安全策略集合的信息。

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityPolicy'
```

---

## 修改安全策略集合资源信息

**章节**: 3.2.51

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SecurityPolicy`

**描述**: 修改服务器当前支持的安全策略集合的信息。

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityPolicy' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Connect",  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO" }'
```

---

## 更新系统主密钥

**章节**: 3.2.52

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 更新系统主密钥。

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Disconnect" }'
```

---

## 导入远程HTTPS 传输服务器根证书

**章节**: 3.2.53

**描述**: 远程HTTPS传输服务器证书导入。  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2....

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
# 导入远程HTTPS 传输服务器根证书
```

---

## 删除远程HTTPS 传输服务器根证书

**章节**: 3.2.54

**描述**: 远程HTTPS传输服务器证书删除。  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2....

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
# 删除远程HTTPS 传输服务器根证书
```

---

## 导入远程HTTPS 传输服务器根证书的吊销列表

**章节**: 3.2.55

**描述**: 导入远程HTTPS 传输服务器根证书的吊销列表

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
# 导入远程HTTPS 传输服务器根证书的吊销列表
```

---

## 查询SSL 证书资源信息

**章节**: 3.2.56

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 查询服务器当前支持的SSL证书资源的信息。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/'
```

---

## 生成CSR

**章节**: 3.2.57

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 生成SSL证书的CSR。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 导出CSR

**章节**: 3.2.58

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导出SSL证书的CSR。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 导入服务器证书

**章节**: 3.2.59

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导入服务器证书。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导入自定义证书

**章节**: 3.2.60

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导入自定义的证书文件。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 查询SSL 证书更新服务资源信息

**章节**: 3.2.61

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 查询iBMC当前支持的证书更新服务资源的信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/'
```

---

## 修改SSL 证书更新服务资源信息

**章节**: 3.2.62

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 修改证书更新服务资源信息

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 导入SSL 证书更新服务的CA 证书

**章节**: 3.2.63

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导入SSL证书自动更新的CA服务器证书  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5....

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 导入SSL 证书更新服务的CA 证书吊销列表

**章节**: 3.2.64

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导入CA服务器的证书吊销列表  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2.0.1...

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 删除SSL 证书更新服务的CA 证书吊销列表

**章节**: 3.2.65

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 删除CA服务器的证书吊销列表  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2.0.1...

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 导入SSL 证书更新服务的客户端证书

**章节**: 3.2.66

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导入CA服务器的客户端证书

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 更新BMC 证书

**章节**: 3.2.67

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 更新BMC证书

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询VNC 资源

**章节**: 3.2.68

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/VncService`

**描述**: 查询VNC资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VncService'
```

---

## 修改VNC 资源属性

**章节**: 3.2.69

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/VNCService`

**描述**: 修改VNC资源属性

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/VNCService' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询SP 服务资源

**章节**: 3.2.70

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService`

**描述**: 查询SP服务资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService'
```

---

## 修改SP 服务资源属性

**章节**: 3.2.71

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SPService`

**描述**: 修改SP服务资源属性

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService' -H 'Content-Type: application/json' -d '{}'
```

---

## 删除SP 服务的升级文件或者配置文件命令功能

**章节**: 3.2.72

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/Actions/`

**描述**: 删除SP 服务的升级文件或者配置文件命令功能

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 触发导出SP 服务的RAID 当前配置命令功能

**章节**: 3.2.73

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/Actions/`

**描述**: 触发导出SP 服务的RAID 当前配置命令功能

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 更新SP 相关的schema 文件

**章节**: 3.2.74

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/Actions/`

**描述**: 更新SP相关的schema。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 收集SP 相关的日志信息

**章节**: 3.2.75

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/Actions/`

**描述**: 收集SP相关的日志信息

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/Actions/' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": false,  "CertVerificationEnabled": false,  "ServerAddress": "device_ip",  "ServerPort": 25,  "TLSEnabled": true,  "AnonymousLoginEnabled": false,  "SenderUserName": "huawei",  "SenderPassword": "Password",  "SenderAddress": "huawei@outlook.com",  "EmailSubject": "Server Alert",  "EmailSubjectContains": [],  "AlarmSeverity": "Normal",  "ReportType": "SEL",  "RecipientAddresses": [   {    "Enabled": false,    "EmailAddress": "smtptest@it.software.com",    "Description": "smtptest"   }  ] }'
```

---

## 查询SP 服务的OS 安装配置集合资源

**章节**: 3.2.76

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询SP的OS安装配置集合资源的信息。本资源受许可证控制，需要通过许可证授权后才能使用。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 创建SP 服务的OS 安装配置

**章节**: 3.2.77

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 创建SP服务的OS安装配置。本资源受许可证控制，需要通过许可证授权后才能使用。

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": false,  "CertVerificationEnabled": false,  "ServerAddress": "device_ip",  "ServerPort": 25,  "TLSEnabled": true,  "AnonymousLoginEnabled": false,  "SenderUserName": "huawei",  "SenderPassword": "Password",  "SenderAddress": "huawei@outlook.com",  "EmailSubject": "Server Alert",  "EmailSubjectContains": [],  "AlarmSeverity": "Normal",  "ReportType": "SEL",  "RecipientAddresses": [   {    "Enabled": false,    "EmailAddress": "smtptest@it.software.com",    "Description": "smtptest"   }  ] }'
```

---

## 查询SP 服务的OS 安装配置资源

**章节**: 3.2.78

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询SP的OS安装配置资源的信息。本资源受许可证控制，需要通过许可证授权后才能  使用。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 查询SP 服务的升级集合资源命令功能

**章节**: 3.2.79

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询SP 服务的升级集合资源命令功能

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 查询SP 服务的升级资源

**章节**: 3.2.80

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询SP的升级资源的信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 升级SP 或者升级固件

**章节**: 3.2.81

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 升级SP或者升级固件。

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content" }'
```

---

## 查询SP 服务的硬件信息资源命令功能

**章节**: 3.2.82

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/DeviceInfo`

**描述**: 查询SP 服务的硬件信息资源命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/DeviceInfo'
```

---

## 查询SP 服务的配置结果集合资源命令功能

**章节**: 3.2.83

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/SPResult`

**描述**: 查询SP 服务的配置结果集合资源命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/SPResult'
```

---

## 查询SP 服务的配置结果资源命令功能

**章节**: 3.2.84

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/SPResult/`

**描述**: 查询SP 服务的配置结果资源命令功能

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/SPResult/'
```

---

## 查询SP 服务的配置信息集合资源

**章节**: 3.2.85

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/SPCfg`

**描述**: 查询SP服务的配置信息资源。

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/SPCfg'
```

---

## 查询SP 服务的配置信息资源

**章节**: 3.2.86

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/SPCfg/`

**描述**: 查询SP服务的配置信息资源。

**请求体**:
```json
{
  "ServiceEnabled": true
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/SPCfg/'
```

---

## 查询SP 服务的诊断配置集合资源命令功能

**章节**: 3.2.87

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/SPDiagnose`

**描述**: 查询SP 服务的诊断配置集合资源命令功能

**请求体**:
```json
{
  "ServiceEnabled": true
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/SPDiagnose'
```

---

## 创建SP 服务的诊断配置

**章节**: 3.2.88

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/SPDiagnose`

**描述**: 创建SP服务的诊断配置。

**请求体**:
```json
{
  "ServiceEnabled": true
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/SPDiagnose' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": true }'
```

---

## 查询SP 服务的诊断配置资源命令功能

**章节**: 3.2.89

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询SP 服务的诊断配置资源命令功能

**请求体**:
```json
{
  "ServiceEnabled": true
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 查询SP 服务的硬盘擦除配置集合资源

**章节**: 3.2.90

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询SP的硬盘擦除配置集合资源的信息。

**请求体**:
```json
{
  "ServiceEnabled": true
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 创建SP 服务的硬盘擦除配置命令功能

**章节**: 3.2.91

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 创建SP 服务的硬盘擦除配置命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content" }'
```

---

## 查询SP 服务的硬盘擦除配置资源命令功能

**章节**: 3.2.92

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询SP 服务的硬盘擦除配置资源命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 查询SP 系统擦除配置集合资源命令功能

**章节**: 3.2.93

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询SP 系统擦除配置集合资源命令功能

**请求体**:
```json
{
  "Type": "text",
  "Content": "content"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 创建SP 系统擦除配置

**章节**: 3.2.94

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 创建SP系统擦除配置文件。

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "content",  "Password": "123" }'
```

---

## 查询指定SP 系统擦除配置

**章节**: 3.2.95

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/`

**描述**: 查询指定SP系统擦除配置信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/'
```

---

## 查询SP 插件集合资源

**章节**: 3.2.96

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService/Plugins`

**描述**: 查询SP插件集合资源的信息。

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/Plugins'
```

---

## 查询SP 插件资源

**章节**: 3.2.97

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SPService//Plugins/`

**描述**: 查询SP插件资源的信息。

**请求体**:
```json
{
  "MemberId": "0"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService//Plugins/'
```

---

## 安装SP 插件

**章节**: 3.2.98

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/Plugins`

**描述**: 安装SP插件。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/Plugins' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 删除SP 插件资源

**章节**: 3.2.99

**方法**: DELETE

**URL**: `/redfish/v1/Managers/manager_id/SPService//Plugins/`

**描述**: 删除SP插件资源。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X DELETE 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService//Plugins/'
```

---

## 查询诊断服务资源

**章节**: 3.2.100

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService`

**描述**: 查询诊断服务资源。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService'
```

---

## 修改诊断服务资源

**章节**: 3.2.101

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService`

**描述**: 修改诊断服务资源。

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService' -H 'Content-Type: application/json' -d '{}'
```

---

## 停止录像回放

**章节**: 3.2.102

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 断开正在播放录像的网络链路。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导出录像

**章节**: 3.2.103

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 导出录像文件。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 截屏

**章节**: 3.2.104

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 截取业务侧系统屏幕图像。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 删除截屏

**章节**: 3.2.105

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 删除手动截屏文件。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导出黑匣子

**章节**: 3.2.106

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 导出黑匣子。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导出串口数据

**章节**: 3.2.107

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 导出串口数据。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导出NPU 日志

**章节**: 3.2.108

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 导出NPU日志。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导出NPU 运行日志

**章节**: 3.2.109

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 导出NPU运行日志

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询工作记录信息

**章节**: 3.2.110

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 查询工作记录信息。工作记录信息保存了自己日常的工作内容，方便以后查看。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/'
```

---

## 添加工作记录

**章节**: 3.2.111

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 添加工作记录。

**请求体**:
```json
{
  "HostName": "huawei"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{  "HostName": "huawei" }'
```

---

## 查询指定日志服务资源信息命令功能

**章节**: 3.2.115

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/LogServices/`

**描述**: 查询指定日志服务资源信息命令功能

**请求体**:
```json
{
  "HostName": "huawei"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/'
```

---

## 导出日志信息

**章节**: 3.2.116

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/LogServices/`

**描述**: 导出日志信息。

**请求体**:
```json
{
  "HostName": "huawei"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/' -H 'Content-Type: application/json' -d '{  "HostName": "huawei" }'
```

---

## 查询日志集合资源信息

**章节**: 3.2.117

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/LogServices/`

**描述**: 查询服务器当前日志集合资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/'
```

---

## 查询日志资源信息

**章节**: 3.2.118

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/LogServices/`

**描述**: 查询服务器当前日志资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/'
```

---

## 查询License 服务信息

**章节**: 3.2.119

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/LicenseService`

**描述**: 查询License服务信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LicenseService'
```

---

## 安装license

**章节**: 3.2.120

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/LicenseService/`

**描述**: 安装license。

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LicenseService/' -H 'Content-Type: application/json' -d '{  "ResetType": "ForceRestart" }'
```

---

## 导出license

**章节**: 3.2.121

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/LicenseService/`

**描述**: 导出license。

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LicenseService/' -H 'Content-Type: application/json' -d '{  "ResetType": "ForceRestart" }'
```

---

## 失效license

**章节**: 3.2.122

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/LicenseService/`

**描述**: 失效license。

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LicenseService/' -H 'Content-Type: application/json' -d '{  "ResetType": "ForceRestart" }'
```

---

## 删除license

**章节**: 3.2.123

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/LicenseService/`

**描述**: 删除license。

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LicenseService/' -H 'Content-Type: application/json' -d '{  "ResetType": "ForceRestart" }'
```

---

## 查询FDMService 服务资源命令功能

**章节**: 3.2.124

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/FDMService`

**描述**: 查询FDMService 服务资源命令功能

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/FDMService'
```

---

## 修改FDMService 服务资源属性

**章节**: 3.2.125

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/FDMService`

**描述**: 修改FDMService的资源属性。

**请求体**:
```json
{
  "ResetType": "ForceRestart"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/FDMService' -H 'Content-Type: application/json' -d '{  "ResetType": "ForceRestart" }'
```

---

## 查询NIC 集合资源

**章节**: 3.2.126

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/NICs`

**描述**: 查询NIC集合信息

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NICs'
```

---

## 查询指定NIC 资源

**章节**: 3.2.127

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/NICs/nicid`

**描述**: 查询指定NIC信息

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NICs/nicid'
```

---

## 修改指定NIC 资源

**章节**: 3.2.128

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/NICs/nicid`

**描述**: 修改指定NIC资源

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NICs/nicid' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询LLDP 服务资源信息

**章节**: 3.2.129

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/LldpService`

**描述**: 查询LLDP配置资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LldpService'
```

---

## 修改LLDP 服务资源信息

**章节**: 3.2.130

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/LldpService`

**描述**: LLDP服务资源属性设置

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LldpService' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询SMS 服务资源信息

**章节**: 3.2.131

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SmsService`

**描述**: 查询SMS配置资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SmsService'
```

---

## 修改SMS 服务资源信息

**章节**: 3.2.132

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SmsService`

**描述**: SMS服务资源属性设置

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SmsService' -H 'Content-Type: application/json' -d '{}'
```

---

## 刷新可安装的BMA

**章节**: 3.2.133

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SmsService/Actions/`

**描述**: 刷新可安装的BMA

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SmsService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询USB 管理服务资源信息

**章节**: 3.2.134

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/USBMgmtService`

**描述**: 查询USB管理服务配置资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/USBMgmtService'
```

---

## 修改USB 管理服务资源信息命令功能

**章节**: 3.2.135

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/USBMgmtService`

**描述**: 修改USB 管理服务资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/USBMgmtService' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询FPCService 服务资源

**章节**: 3.2.136

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/FPCService`

**描述**: 查询FPCService资源属性

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/FPCService'
```

---

## 查询FPC 内存健康状态信息

**章节**: 3.2.137

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/FPCService/Memory`

**描述**: 查询服务器当前FPC内存健康状态信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/FPCService/Memory'
```

---

## 内存隔离联动模式下发隔离任务命令功能

**章节**: 3.2.138

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/FPCService/Memory/`

**描述**: 内存隔离联动模式下发隔离任务命令功能

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/FPCService/Memory/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询场景化智能节能信息

**章节**: 3.2.139

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/EnergySavingService`

**描述**: 查询场景化智能节能信息。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/EnergySavingService'
```

---

## 智能节能场景配置

**章节**: 3.2.140

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/EnergySavingService/`

**描述**: 智能节能场景配置。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/EnergySavingService/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 创建SP 服务的RAID 配置

**章节**: 3.2.141

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SPService/SPRAID`

**描述**: 创建SP服务的RAID配置。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SPService/SPRAID' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 报废处置

**章节**: 3.2.142

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 产品报废处置。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 查询DICE 证书资源信息

**章节**: 3.2.143

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 查询服务器当前支持的DICE证书资源的信息。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/'
```

---

## 导出DICE CSR

**章节**: 3.2.144

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导出DICE CSR。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 导入DICE 证书

**章节**: 3.2.145

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导入DICE证书。

**请求体**:
```json
{
  "Type": "text",
  "Content": ""
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "" }'
```

---

## 导出DICE 证书链

**章节**: 3.2.146

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导出DICE证书链。

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "RootCertId": 1 }'
```

---

## 导出融合身份认证证书链

**章节**: 3.2.147

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 导出融合身份认证证书链。

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "RootCertId": 1 }'
```

---

## 查询TPCM 服务信息

**章节**: 3.2.148

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 查询TPCM服务信息

**请求体**:
```json
{
  "RootCertId": 1
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/'
```

---

## 设置TPCM 服务信息

**章节**: 3.2.149

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/SecurityService/`

**描述**: 设置TPCM服务信息

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
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/SecurityService/' -H 'Content-Type: application/json' -d '{  "Type": "text",  "Content": "123",  "RootCertId": 1 }'
```

---

## 查询CA 证书集合资源信息

**章节**: 3.2.150

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/Certificates`

**描述**: 查询设备当前CA证书集合资源信息。  说明  自iBMC300 5.2.0.1版本后证书升级为资源池，根证书和所有其他BMC业务公用。建议使用此接口对CA证书进行管理。  共用根证书的包括BMC所有校...

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Certificates'
```

---

## 查询指定CA 证书资源信息

**章节**: 3.2.151

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/Certificates/`

**描述**: 查询指定用户资源信息。  说明  自iBMC300 5.2.0.1版本后证书升级为资源池，根证书和所有其他BMC业务公用。建议使用此接口对CA证书、吊销列表进行管理。  共用根证书的包括BMC所有校验...

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCA3.crl"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Certificates/'
```

---

## 删除CA 证书的吊销列表

**章节**: 3.2.152

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Certificates/`

**描述**: CA证书吊销列表删除。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Certificates/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询全量告警信息

**章节**: 3.2.153

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/LogServices/EventLog`

**描述**: 查询服务器全量告警资源信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/EventLog'
```

---

## 设置事件记录模式

**章节**: 3.2.154

**方法**: PATCH

**URL**: `/redfish/v1/Managers/manager_id/LogServices/EventLog`

**描述**: 设置事件记录模式

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/EventLog' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/c.csr" }'
```

---

## 查询PRBS 测试接口集合的资源信息命令功能

**章节**: 3.2.155

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 查询PRBS 测试接口集合的资源信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/'
```

---

## 查询PRBS 测试对象集合的资源信息命令功能

**章节**: 3.2.156

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 查询PRBS 测试对象集合的资源信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/'
```

---

## 查询单个PRBS 测试对象信息命令功能

**章节**: 3.2.157

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 查询单个PRBS 测试对象信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/'
```

---

## 查询PRBS 测试信息

**章节**: 3.2.158

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 查询PRBS测试信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/c.csr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/c.csr" }'
```

---

## 下发PRBS 测试配置

**章节**: 3.2.159

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 下发PRBS测试配置

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 清除PRBS 测试统计

**章节**: 3.2.160

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 清除PRBS测试统计。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 终止PRBS 测试

**章节**: 3.2.161

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/DiagnosticService/`

**描述**: 终止PRBS测试。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/DiagnosticService/' -H 'Content-Type: application/json' -d '{}'
```

---

## 下发入侵检测配置信息

**章节**: 3.2.162

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 支持网管侧下发入侵检测配置信息到安全组件

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询系统日志集合资源信息

**章节**: 3.2.163

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/LogServices/`

**描述**: 查询服务器当前日志集合资源信息

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/'
```

---

## 查询系统日志资源信息

**章节**: 3.2.164

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/LogServices/`

**描述**: 查询系统日志资源信息

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCATest.crt"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/'
```

---

## 清空日志信息

**章节**: 3.2.165

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/LogServices/`

**描述**: 查询系统日志资源信息

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCATest.crt"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/LogServices/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/HuaweiCATest.crt" }'
```

---

## 设置BMC 吊销版本列表

**章节**: 3.2.166

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 设置BMC吊销版本列表

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCATest.crt"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/HuaweiCATest.crt" }'
```

---

## 恢复出厂设置

**章节**: 3.2.167

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/`

**描述**: 恢复出厂设置

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCATest.crt"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/HuaweiCATest.crt" }'
```

---

## 测试文件服务器连通性

**章节**: 3.2.168

**方法**: POST

**URL**: `/redfish/v1/Managers/manager_id/Actions/Oem/`

**描述**: 测试文件服务器连通性

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCATest.crt"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Managers/manager_id/Actions/Oem/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/HuaweiCATest.crt" }'
```

---

## 查询SSL 证书集合资源信息命令功能

**章节**: 3.2.169

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/NetworkProtocol/`

**描述**: 查询SSL 证书集合资源信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCATest.crt"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NetworkProtocol/'
```

---

## 查询指定SSL 证书资源信息

**章节**: 3.2.170

**方法**: GET

**URL**: `/redfish/v1/Managers/manager_id/NetworkProtocol/`

**描述**: 查询指定SSL证书资源信息，当前仅支持Subject下的AlternativeNames字段查询，剩余SSL证书历史资源请在redfish/v1/Managers/manager_id/Securit...

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/HuaweiCATest.crt"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Managers/manager_id/NetworkProtocol/'
```

---

