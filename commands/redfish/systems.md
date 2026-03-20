# Redfish 系统资源接口

> 共 70 个接口 (有效: 70, 有请求体: 41)

## 查询系统集合资源信息

**章节**: 3.3.1

**方法**: GET

**URL**: `/redfish/v1/Systems`

**描述**: 查询服务器当前系统集合资源的信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems'
```

---

## 查询指定系统资源信息

**章节**: 3.3.2

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id`

**描述**: 查询服务器指定系统资源信息，当前仅可查询服务器本身系统资源信息。  注：查询BIOS配置信息时，查询的是BIOS配置项实时生效信息。BIOS配置信息查询受License控制。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id'
```

---

## 修改指定系统资源属性

**章节**: 3.3.3

**方法**: PATCH

**URL**: `/redfish/v1/Systems/system_id`

**描述**: 修改指定系统资源属性。  注：修改BIOS配置信息时，无需系统重启即可实时生效，系统重启后修改失效。BIOS配置信息修改受License控制。  修改通电开机策略与当前状态不同时，优先以Redfish...

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Systems/system_id' -H 'Content-Type: application/json' -d '{}'
```

---

## 重启服务器

**章节**: 3.3.4

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Actions/`

**描述**: 重启服务器。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## FRU 上下电控制

**章节**: 3.3.5

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Actions/Oem/Huawei/`

**描述**: 控制FRU上下电状态。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Actions/Oem/Huawei/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询主机以太网接口集合资源信息命令功能

**章节**: 3.3.6

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/EthernetInterfaces`

**描述**: 查询主机以太网接口集合资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/EthernetInterfaces'
```

---

## 查询指定主机以太网接口资源信息

**章节**: 3.3.7

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/EthernetInterfaces/`

**描述**: 查询服务器指定主机以太网接口资源的信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/EthernetInterfaces/'
```

---

## 配置以太网

**章节**: 3.3.8

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/EthernetInterfaces/`

**描述**: 配置以太网。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/EthernetInterfaces/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询Bond 集合资源信息

**章节**: 3.3.9

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/NetworkBondings`

**描述**: 查询Bond集合资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/NetworkBondings'
```

---

## 查询Bond 资源信息

**章节**: 3.3.10

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/NetworkBondings/`

**描述**: 查询Bond资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/NetworkBondings/'
```

---

## 配置Bond

**章节**: 3.3.11

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/NetworkBondings/`

**描述**: 配置Bond。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/NetworkBondings/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询网络桥接集合资源信息命令功能

**章节**: 3.3.12

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/NetworkBridge`

**描述**: 查询网络桥接集合资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/NetworkBridge'
```

---

## 查询网络桥接资源信息

**章节**: 3.3.13

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/NetworkBridge/bridge`

**描述**: 查询网络桥接资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/NetworkBridge/bridge'
```

---

## 查询内存集合资源信息

**章节**: 3.3.14

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Memory`

**描述**: 查询服务器当前内存集合资源信息。  说明  查询所有在位内存信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Memory'
```

---

## 查询指定内存资源信息

**章节**: 3.3.15

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Memory/memory_id`

**描述**: 查询服务器指定内存资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Memory/memory_id'
```

---

## 查询指定内存指标资源信息命令功能

**章节**: 3.3.16

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Memory/memory_id/`

**描述**: 查询指定内存指标资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Memory/memory_id/'
```

---

## 查询VLAN 集合资源信息

**章节**: 3.3.17

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/EthernetInterfaces/`

**描述**: 查询VLAN集合资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/EthernetInterfaces/'
```

---

## 查询VLAN 资源信息

**章节**: 3.3.18

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/EthernetInterfaces/`

**描述**: 查询VLAN资源信息。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/EthernetInterfaces/'
```

---

## 配置VLAN

**章节**: 3.3.19

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/EthernetInterfaces/`

**描述**: 配置VLAN。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/EthernetInterfaces/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 查询存储集合资源信息

**章节**: 3.3.20

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Storages`

**描述**: 查询服务器当前存储集合资源信息。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages'
```

---

## 查询指定存储资源信息

**章节**: 3.3.21

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id`

**描述**: 查询服务器指定存储资源信息。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id'
```

---

## 修改指定控制器资源信息

**章节**: 3.3.22

**方法**: PATCH

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id`

**描述**: 修改服务器指定控制器的属性。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 恢复指定控制器的默认配置命令功能

**章节**: 3.3.23

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id/`

**描述**: 恢复指定控制器的默认配置命令功能

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 查询逻辑盘集合资源信息

**章节**: 3.3.24

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id/`

**描述**: 查询服务器当前逻辑盘集合资源信息。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id/'
```

---

## 查询指定逻辑盘资源信息命令功能

**章节**: 3.3.25

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id/`

**描述**: 查询指定逻辑盘资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id/'
```

---

## 修改指定逻辑盘资源属性

**章节**: 3.3.26

**方法**: PATCH

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id/`

**描述**: 修改指定逻辑盘的属性。

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id/' -H 'Content-Type: application/json' -d '{}'
```

---

## 初始化指定逻辑盘

**章节**: 3.3.27

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id/`

**描述**: 对指定逻辑盘执行初始化操作。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id/' -H 'Content-Type: application/json' -d '{}'
```

---

## 删除指定逻辑盘

**章节**: 3.3.28

**方法**: DELETE

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id/`

**描述**: 删除指定的逻辑盘。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X DELETE 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id/'
```

---

## 创建逻辑盘

**章节**: 3.3.29

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id/`

**描述**: 创建逻辑盘。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id/' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 查询BIOS 资源信息

**章节**: 3.3.30

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Bios`

**描述**: 查询服务器当前BIOS资源信息。  注：查询BIOS配置信息时，查询的是BIOS持久化生效的配置项信息。BIOS实际支持的资源信息受BIOS版本限制。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios'
```

---

## 恢复BIOS 属性默认值

**章节**: 3.3.31

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Actions/`

**描述**: 恢复BIOS属性默认值。  注：恢复BIOS默认资源表示已下发BIOS默认值，但当前还未生效，下次系统重启时生效。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Actions/' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 修改BIOS 密码

**章节**: 3.3.32

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Actions/`

**描述**: 修改BIOS的密码。  注：BMC只是修改BIOS密码，BIOS密码生效需重启OS，且如果OS重启前有多次设置，以最后一次的设置请求为准1。   ## 命令格式  操作类型：POST  URL：htt...

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Actions/' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 查询BIOS 设置资源信息

**章节**: 3.3.33

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Bios/Settings`

**描述**: 查询服务器当前BIOS设置资源信息。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Settings'
```

---

## 修改BIOS 设置资源属性

**章节**: 3.3.34

**方法**: PATCH

**URL**: `/redfish/v1/Systems/system_id/Bios/Settings`

**描述**: 修改BIOS设置资源的属性。  注：BIOS设置资源表示已下发BIOS setup项，但当前还未生效，下次系统重启时生效。

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
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Settings' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 清除未生效的BIOS 配置

**章节**: 3.3.35

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Settings/`

**描述**: 清除未生效的BIOS配置属性。

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Settings/' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 查询BIOS 策略重配资源信息

**章节**: 3.3.36

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Bios/PolicyConfig`

**描述**: 查询服务器当前BIOS策略重配资源信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/PolicyConfig'
```

---

## 查询BIOS 策略重配设置资源信息

**章节**: 3.3.37

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Bios/PolicyConfig/`

**描述**: 查询服务器当前BIOS策略重配设置资源信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/PolicyConfig/'
```

---

## 修改BIOS 策略重配设置资源属性

**章节**: 3.3.38

**方法**: PATCH

**URL**: `/redfish/v1/Systems/system_id/Bios/PolicyConfig/`

**描述**: 修改BIOS策略重配设置资源的属性。

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
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/PolicyConfig/' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 导入安全启动证书

**章节**: 3.3.39

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Oem/Huawei/`

**描述**: 导入BIOS安全启动证书 注：导入的BIOS安全启动证书表示已下发的配置，但当前还未生效，下次系统重启时生效；系统启动过程中无法导入证书。

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 重置安全启动证书

**章节**: 3.3.40

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Oem/Huawei/`

**描述**: 重置BIOS安全启动证书 注：重置BIOS安全启动证书表示已下发的配置，但当前还未生效，下次系统重启时生效；系统启动过程中无法重置证书。

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Connect",  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO" }'
```

---

## 导入HTTPS 启动证书

**章节**: 3.3.41

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Oem/Huawei/`

**描述**: 导入BIOS HTTPS启动证书 注：导入的BIOS HTTPS启动证书表示已下发的配置，但当前还未生效，下次系统重启时生效；系统启动过程中无法导入证书。

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Connect",  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO" }'
```

---

## 重置HTTPS 启动证书

**章节**: 3.3.42

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Oem/Huawei/`

**描述**: 重置BIOS HTTPS启动证书 注：重置BIOS HTTPS启动证书表示已下发的配置，但当前还未生效，下次系统重启时生效；系统启动过程中无法重置证书。

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Disconnect" }'
```

---

## 导入HTTPS 启动证书吊销列表

**章节**: 3.3.43

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Oem/Huawei/`

**描述**: 导入BIOS HTTPS启动证书吊销列表 注：导入的BIOS HTTPS启动证书吊销列表表示已下发的配置，但当前还未生效，下次系统重启时生效；系统启动过程中无法导入吊销列表。

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Disconnect" }'
```

---

## 重置HTTPS 启动证书吊销列表

**章节**: 3.3.44

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Bios/Oem/Huawei/`

**描述**: 重置BIOS HTTPS证书吊销列表 注：重置BIOS HTTPS启动证书吊销列表表示已下发的配置，但当前还未生效，下次系统重启时生效；系统启动过程中无法重置证书吊销列表。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 查询Bios 证书信息

**章节**: 3.3.45

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Bios/Oem/Huawei/`

**描述**: 查询Bios证书信息  注：系统启动过程中无法查询证书信息。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Bios/Oem/Huawei/'
```

---

## 查询处理器集合资源信息

**章节**: 3.3.46

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Processors`

**描述**: 查询服务器当前处理器集合资源信息。  说明 	查询所有在位处理器信息。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Processors'
```

---

## 查询指定处理器资源信息命令功能

**章节**: 3.3.47

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/Processors/processor_id`

**描述**: 查询指定处理器资源信息命令功能

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/Processors/processor_id'
```

---

## 修改指定CPU 资源属性

**章节**: 3.3.48

**方法**: PATCH

**URL**: `/redfish/v1/Systems/system_id/Processors/cpu_id`

**描述**: 修改指定CPU资源的属性。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Systems/system_id/Processors/cpu_id' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 查询网络接口集合资源信息

**章节**: 3.3.49

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/NetworkInterfaces`

**描述**: 查询服务器当前网络接口集合资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/NetworkInterfaces'
```

---

## 查询网络接口资源信息

**章节**: 3.3.50

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/NetworkInterfaces/`

**描述**: 查询服务器指定网络接口资源信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/NetworkInterfaces/'
```

---

## 查询网络端口集合资源信息

**章节**: 3.3.51

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/NetworkInterfaces/`

**描述**: 查询服务器当前网络端口集合资源信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/NetworkInterfaces/'
```

---

## 查询日志服务集合资源信息

**章节**: 3.3.52

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/LogServices`

**描述**: 查询服务器当前日志服务集合资源信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/LogServices'
```

---

## 查询指定日志服务资源信息

**章节**: 3.3.53

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/LogServices/logservices_id`

**描述**: 查询服务器当前日志服务资源信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/LogServices/logservices_id'
```

---

## 修改指定日志服务资源属性命令功能

**章节**: 3.3.54

**方法**: PATCH

**URL**: `/redfish/v1/Systems/system_id/LogServices/LogService_id`

**描述**: 修改指定日志服务资源属性命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Systems/system_id/LogServices/LogService_id' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 清空日志信息

**章节**: 3.3.55

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/LogServices/`

**描述**: 清空日志信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/LogServices/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 查询SEL 日志

**章节**: 3.3.56

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/LogServices/`

**描述**: 查询SEL日志。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/LogServices/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 收集SEL 日志

**章节**: 3.3.57

**方法**: POST

**URL**: `/redfish/v1/Systems/systems_id/LogServices/`

**描述**: 收集SEL日志

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/systems_id/LogServices/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询日志集合资源信息

**章节**: 3.3.58

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/LogServices/Log_id/`

**描述**: 查询服务器当前日志集合资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/LogServices/Log_id/'
```

---

## 查询日志资源信息

**章节**: 3.3.59

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/LogServices/`

**描述**: 查询服务器当前日志资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/LogServices/'
```

---

## 查询CPU 历史占用率资源信息

**章节**: 3.3.60

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/`

**描述**: 查询CPU历史占用率资源信息

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/'
```

---

## 查询内存历史占用率资源信息命令功能

**章节**: 3.3.61

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/`

**描述**: 查询内存历史占用率资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/'
```

---

## 查询网口历史占用率资源信息命令功能

**章节**: 3.3.62

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/`

**描述**: 查询网口历史占用率资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/'
```

---

## 清空网口历史占用率资源信息

**章节**: 3.3.63

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Actions/Oem/Huawei/`

**描述**: 清空网口历史占用率资源信息

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Actions/Oem/Huawei/' -H 'Content-Type: application/json' -d '{}'
```

---

## 批量查询处理器资源信息

**章节**: 3.3.64

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/ProcessorView`

**描述**: 查询服务器当前处理器资源。  说明 	查询所有处理器资源，包括不在位的处理器资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/ProcessorView'
```

---

## 批量查询内存资源信息

**章节**: 3.3.65

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/MemoryView`

**描述**: 查询服务器当前内存资源。  说明 	查询环境所有内存资源，包括不在位的内存资源信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/MemoryView'
```

---

## 查询电子保单信息

**章节**: 3.3.66

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/DigitalWarranty`

**描述**: 查询电子保单信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/DigitalWarranty'
```

---

## 修改电子保单信息

**章节**: 3.3.67

**方法**: PATCH

**URL**: `/redfish/v1/Systems/system_id/DigitalWarranty`

**描述**: 修改电子保单信息。

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
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Systems/system_id/DigitalWarranty' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": false,  "CertVerificationEnabled": false,  "ServerAddress": "device_ip",  "ServerPort": 25,  "TLSEnabled": true,  "AnonymousLoginEnabled": false,  "SenderUserName": "huawei",  "SenderPassword": "Password",  "SenderAddress": "huawei@outlook.com",  "EmailSubject": "Server Alert",  "EmailSubjectContains": [],  "AlarmSeverity": "Normal",  "ReportType": "SEL",  "RecipientAddresses": [   {    "Enabled": false,    "EmailAddress": "smtptest@it.software.com",    "Description": "smtptest"   }  ] }'
```

---

## 导入Foreign 配置

**章节**: 3.3.68

**方法**: POST

**URL**: `/redfish/v1/Systems/system_id/Storages/storage_id/`

**描述**: 导入Foreign磁盘包含的RAID配置信息，需输入配置文件

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Systems/system_id/Storages/storage_id/' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": false,  "CertVerificationEnabled": false,  "ServerAddress": "device_ip",  "ServerPort": 25,  "TLSEnabled": true,  "AnonymousLoginEnabled": false,  "SenderUserName": "huawei",  "SenderPassword": "Password",  "SenderAddress": "huawei@outlook.com",  "EmailSubject": "Server Alert",  "EmailSubjectContains": [],  "AlarmSeverity": "Normal",  "ReportType": "SEL",  "RecipientAddresses": [   {    "Enabled": false,    "EmailAddress": "smtptest@it.software.com",    "Description": "smtptest"   }  ] }'
```

---

## 查询IB 集合资源信息

**章节**: 3.3.69

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/InfiniBandInterfaces`

**描述**: 查询IB集合资源信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/InfiniBandInterfaces'
```

---

## 查询IB 资源信息

**章节**: 3.3.70

**方法**: GET

**URL**: `/redfish/v1/Systems/system_id/InfiniBandInterfaces/ib_id`

**描述**: 查询IB资源信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Systems/system_id/InfiniBandInterfaces/ib_id'
```

---

