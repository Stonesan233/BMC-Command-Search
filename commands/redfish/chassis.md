# Redfish 机箱接口

> 共 58 个接口 (有效: 57, 有请求体: 40)

## 查询机箱集合资源信息

**章节**: 3.4.1

**方法**: GET

**URL**: `/redfish/v1/Chassis`

**描述**: 查询服务器系统内的机箱集合资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis'
```

---

## 查询指定机箱资源信息

**章节**: 3.4.2

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id`

**描述**: 查询指定的服务器机箱资源信息。  说明 	GA140C等机型为纯液冷散热，响应体以实际返回结果为准。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id'
```

---

## 修改指定机箱资源信息

**章节**: 3.4.3

**方法**: PATCH

**URL**: `/redfish/v1/Chassis/chassis_id`

**描述**: 修改指定的服务器机箱资源信息。  说明  GA140C等机型为纯液冷散热，响应体以实际返回结果为准。   ## 命令格式  操作类型：PATCH  URL：https://device_ip/redf...

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id' -H 'Content-Type: application/json' -d '{}'
```

---

## 控制机箱定位指示灯状态

**章节**: 3.4.4

**方法**: POST

**URL**: `/redfish/v1/Chassis/Chassis_id/Oem/Huawei/Actions/`

**描述**: 控制机箱定位指示灯状态。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/Chassis_id/Oem/Huawei/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 恢复超节点配置信息为默认值命令功能

**章节**: 3.4.5

**方法**: POST

**URL**: `/redfish/v1/Chassis/Chassis_id/Oem/Huawei/Actions/`

**描述**: 恢复超节点配置信息为默认值命令功能

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/Chassis_id/Oem/Huawei/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询指定机箱散热资源信息

**章节**: 3.4.6

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/Thermal`

**描述**: 查询指定服务器机箱的温度和风扇传感器信息。  GA140C等机型为纯液冷散热，响应体以实际返回结果为准。   ## 命令格式  操作类型：GET  URL：https://device_ip/redf...

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Thermal'
```

---

## 修改指定机箱散热资源信息

**章节**: 3.4.7

**方法**: PATCH

**URL**: `/redfish/v1/Chassis/chassis_id/Thermal`

**描述**: 修改指定机箱散热资源信息。  说明  GA140C等机型为纯液冷散热，响应体以实际返回结果为准。

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Thermal' -H 'Content-Type: application/json' -d '{}'
```

---

## 清空进风口历史温度数据

**章节**: 3.4.8

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Thermal/Oem/Huawei/`

**描述**: 清空进风口历史温度的数据

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Thermal/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 查询指定机箱电源信息

**章节**: 3.4.9

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/Power`

**描述**: 查询指定服务器机箱的电压、功率和电源信息。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Power'
```

---

## 修改指定电源属性

**章节**: 3.4.10

**方法**: PATCH

**URL**: `/redfish/v1/Chassis/chassis_id/Power`

**描述**: 修改服务器指定电源属性。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Power' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 清空历史功率数据

**章节**: 3.4.11

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Power/Oem/Huawei/`

**描述**: 清空历史功率数据。  说明  GA140C等机型为纯液冷散热，响应体以实际返回结果为准。   ## 命令格式  操作类型：POST  URL：https://device_ip/redfish/v1/...

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Power/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 重新统计功率数据

**章节**: 3.4.12

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Power/Oem/Huawei/`

**描述**: 重新统计功率数据。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Power/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 收集功率统计数据

**章节**: 3.4.13

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Power/Oem/Huawei/`

**描述**: 收集功率统计数据  说明  GA140C等机型为纯液冷散热，响应体以实际返回结果为准。

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Power/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "Language": "fr" }'
```

---

## 查询指定机箱电源子系统信息

**章节**: 3.4.14

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/PowerSubsystem`

**描述**: 查询指定服务器机箱的电源子系统信息

**请求体**:
```json
{
  "Language": "fr"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PowerSubsystem'
```

---

## 查询电源转换器集合资源信息

**章节**: 3.4.15

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/PowerSubsystem/Oem/`

**描述**: 查询电源转换器集合资源信息

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PowerSubsystem/Oem/'
```

---

## 查询电源转换器单个资源信息命令功能

**章节**: 3.4.16

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/PowerSubsystem/Oem/`

**描述**: 查询电源转换器单个资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PowerSubsystem/Oem/'
```

---

## 查询网络适配器集合资源信息命令功能

**章节**: 3.4.17

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/NetworkAdapters`

**描述**: 查询网络适配器集合资源信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/NetworkAdapters'
```

---

## 查询网络适配器单个资源信息命令功能

**章节**: 3.4.18

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/NetworkAdapters/`

**描述**: 查询网络适配器单个资源信息命令功能

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/NetworkAdapters/'
```

---

## 查询网络端口集合资源信息命令功能

**章节**: 3.4.19

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/NetworkAdapters/`

**描述**: 查询网络端口集合资源信息命令功能

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/NetworkAdapters/'
```

---

## 查询网络端口单个资源信息

**章节**: 3.4.20

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/NetworkAdapters/`

**描述**: 查询指定服务器机箱的网络端口单个资源信息。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/NetworkAdapters/'
```

---

## 修改网络端口单个资源信息

**章节**: 3.4.21

**方法**: PATCH

**URL**: `/redfish/v1/Chassis/chassis_id/NetworkAdapters/`

**描述**: 修改指定服务器机箱的网络端口单个资源信息。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/NetworkAdapters/' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 查询网络端口上接的光模块资源信息

**章节**: 3.4.22

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/Transceivers/`

**描述**: 查询指定服务器机箱的网络端口上接的光模块资源信息。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Transceivers/'
```

---

## 查询网络端口上接的光模块集合资源信息命令功能

**章节**: 3.4.23

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/Transceivers`

**描述**: 查询网络端口上接的光模块集合资源信息命令功能

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Transceivers'
```

---

## 查询驱动器集合资源信息

**章节**: 3.4.24

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/Drives`

**描述**: 查询驱动器集合资源信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Drives'
```

---

## 查询指定驱动器资源信息

**章节**: 3.4.25

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/drives/drive_id`

**描述**: 查询服务器指定驱动器的信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/drives/drive_id'
```

---

## 修改指定驱动器属性

**章节**: 3.4.26

**方法**: PATCH

**URL**: `/redfish/v1/Chassis/chassis_id/Drives/drives_id`

**描述**: 修改服务器指定驱动器的属性。

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
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Drives/drives_id' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 加密盘的数据安全擦除

**章节**: 3.4.27

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Drives/drives_id/`

**描述**: 加密盘的数据安全擦除。

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Drives/drives_id/' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 查询扩展板卡集合资源信息命令功能

**章节**: 3.4.28

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/Boards`

**描述**: 查询扩展板卡集合资源信息命令功能

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Boards'
```

---

## 查询指定扩展板卡资源信息命令功能

**章节**: 3.4.29

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/Boards/board_id`

**描述**: 查询指定扩展板卡资源信息命令功能

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Boards/board_id'
```

---

## 修改指定拓展板卡资源属性

**章节**: 3.4.30

**方法**: PATCH

**URL**: `/redfish/v1/Chassis/chassis_id/Boards/board_id`

**描述**: 修改服务器指定扩展板卡资源属性。   ## 命令格式  操作类型：PATCH  URL：https://device_ip/redfish/v1/Chassis/chassis_id/Boards/b...

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Boards/board_id' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Connect",  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO" }'
```

---

## NPU 模组复位

**章节**: 3.4.31

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Boards/board_id/Actions/`

**描述**: 复位NPU模组。

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Boards/board_id/Actions/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Connect",  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO" }'
```

---

## 查询PCIe 设备集合资源信息

**章节**: 3.4.32

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/PCIeDevices`

**描述**: 查询PCIe设备集合资源信息。

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PCIeDevices'
```

---

## 查询指定PCIe 设备资源信息命令功能

**章节**: 3.4.33

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/PCIeDevices/pciedevices_id`

**描述**: 查询指定PCIe 设备资源信息命令功能

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PCIeDevices/pciedevices_id'
```

---

## 修改指定PCIe 设备资源信息命令功能

**章节**: 3.4.34

**方法**: PATCH

**URL**: `/redfish/v1/Chassis/chassis_id/PCIeDevices/pciedevices_id`

**描述**: 修改指定PCIe 设备资源信息命令功能

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PCIeDevices/pciedevices_id' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 复位指定SDI 卡

**章节**: 3.4.35

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/PCIeDevices/`

**描述**: 复位指定SDI卡

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PCIeDevices/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 设置指定SDI 卡电源状态

**章节**: 3.4.36

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/PCIeDevices/`

**描述**: 设置指定SDI卡电源状态

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PCIeDevices/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 指定PCIe 设备资源导入https 证书命令功能

**章节**: 3.4.37

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/PCIeDevices/`

**描述**: 指定PCIe 设备资源导入https 证书命令功能

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PCIeDevices/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 查询指定PCIe 功能资源信息

**章节**: 3.4.38

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/PCIeDevices/`

**描述**: 查询服务器指定PCIe功能资源信息。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/PCIeDevices/'
```

---

## 查询进风口历史温度资源信息

**章节**: 3.4.39

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/Thermal/`

**描述**: 查询进风口历史温度资源信息

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Thermal/'
```

---

## 查询历史功率资源信息

**章节**: 3.4.40

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Power/Oem/Huawei/`

**描述**: 查询历史功率资源信息  说明 	GA140C等机型为纯液冷散热，响应体以实际返回结果为准。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Power/Oem/Huawei/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 查询门限传感器列表资源信息命令功能

**章节**: 3.4.41

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/ThresholdSensors`

**描述**: 查询门限传感器列表资源信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThresholdSensors'
```

---

## 查询离散型传感器列表资源信息命令功能

**章节**: 3.4.42

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/DiscreteSensors`

**描述**: 查询离散型传感器列表资源信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/DiscreteSensors'
```

---

## 查询备电集合资源信息

**章节**: 3.4.43

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/BackupBatteryUnits`

**描述**: 查询备电集合资源信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/BackupBatteryUnits'
```

---

## 查询备电单个资源信息

**章节**: 3.4.44

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/BackupBatteryUnits/`

**描述**: 查询指定备电单个资源信息。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/BackupBatteryUnits/'
```

---

## 查询指定机箱泵资源信息命令功能

**章节**: 3.4.45

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem`

**描述**: 查询指定机箱泵资源信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem'
```

---

## 修改指定机箱泵资源信息

**章节**: 3.4.46

**方法**: PATCH

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem`

**描述**: 修改指定服务器机箱泵资源信息。  说明  iBMC300 5.5.0.1 及以上版本支持。   ## 命令格式  操作类型：PATCH  URL：https://device_ip/redfish/v...

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 重启整机服务器

**章节**: 3.4.47

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Actions/Chassis.Reset`

**描述**: 重启整机多个服务器。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Actions/Chassis.Reset' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询漏液检测系统信息

**章节**: 3.4.48

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem/`

**描述**: 查询液冷系统信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem/'
```

---

## 查询漏液检测器集合

**章节**: 3.4.49

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem/`

**描述**: 查询漏液检测器集合资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem/'
```

---

## 查询漏液检测

**章节**: 3.4.50

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem/`

**描述**: 查询指定检测器的漏液状态。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem/'
```

---

## 查询风扇集合资源信息

**章节**: 3.4.51

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem/Fans`

**描述**: 查询风扇集合资源信息。  说明 	GA140C等机型为纯液冷散热，响应体以实际返回结果为准。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem/Fans'
```

---

## 查询风扇单个资源信息

**章节**: 3.4.52

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem/Fans/`

**描述**: 查询风扇单个资源信息。  说明  GA140C等机型为纯液冷散热，响应体以实际返回结果为准。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem/Fans/'
```

---

## 设置风扇组、泵组转速批量下发

**章节**: 3.4.53

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/Sensors`

**描述**: 风扇组、泵组批量转速下发  说明 	GA140C等机型为纯液冷散热，响应体以实际返回结果为准。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/Sensors' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询指定Sensor 资源信息

**章节**: 3.4.55

**描述**: 查询服务器指定Sensor资源信息。   ## 命令格式  操作类型：GET  URL：https://device_ip/ redfish/v1/Chassis/chassis_id/Sensors...

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
# 查询指定Sensor 资源信息
```

---

## 查询指定机箱散热度量资源信息命令功能

**章节**: 3.4.56

**方法**: GET

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem/`

**描述**: 查询指定机箱散热度量资源信息命令功能

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem/'
```

---

## 重新统计散热组件累计耗电量数据

**章节**: 3.4.57

**方法**: POST

**URL**: `/redfish/v1/Chassis/chassis_id/ThermalSubsystem/`

**描述**: 重新统计散热组件累计耗电量数据

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/Chassis/chassis_id/ThermalSubsystem/' -H 'Content-Type: application/json' -d '{  "ServiceEnabled": false,  "CertVerificationEnabled": false,  "ServerAddress": "device_ip",  "ServerPort": 25,  "TLSEnabled": true,  "AnonymousLoginEnabled": false,  "SenderUserName": "huawei",  "SenderPassword": "Password",  "SenderAddress": "huawei@outlook.com",  "EmailSubject": "Server Alert",  "EmailSubjectContains": [],  "AlarmSeverity": "Normal",  "ReportType": "SEL",  "RecipientAddresses": [   {    "Enabled": false,    "EmailAddress": "smtptest@it.software.com",    "Description": "smtptest"   }  ] }'
```

---

## 查询单个电源信息

**章节**: 3.4.58

**方法**: GET

**URL**: `/redfish/v1/Chassis/ChassisId/PowerSubsystem/`

**描述**: 查询单个电源信息

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/ChassisId/PowerSubsystem/'
```

---

## 查询单个电源度量信息

**章节**: 3.4.59

**方法**: GET

**URL**: `/redfish/v1/Chassis/ChassisId/PowerSubsystem/`

**描述**: 查询单个电源度量信息

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/Chassis/ChassisId/PowerSubsystem/'
```

---

