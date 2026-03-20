# Redfish 服务根接口

> 共 6 个接口 (有效: 6, 有请求体: 0)

## 查询当前根服务资源

**章节**: 3.1.2

**方法**: GET

**URL**: `/redfish/v1`

**描述**: 查询服务器当前根服务资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1'
```

---

## 修改当前根服务资源

**章节**: 3.1.3

**方法**: PATCH

**URL**: `/redfish/v1`

**描述**: 修改当前根服务资源。

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询Metadata 文档

**章节**: 3.1.4

**方法**: GET

**URL**: `/redfish/v1/$metadata`

**描述**: 查询Redfish规范里的元数据文档。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/$metadata'
```

---

## 查询系统概览信息

**章节**: 3.1.11

**方法**: GET

**URL**: `/redfish/v1/SystemOverview`

**描述**: 查询系统概览信息

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/SystemOverview'
```

---

## 查询性能数据采集服务资源命令功能

**章节**: 3.1.12

**方法**: GET

**URL**: `/redfish/v1/PerformanceCollection`

**描述**: 查询性能数据采集服务资源命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/PerformanceCollection'
```

---

## 查询归档的BMC 事件上报注册文件资源命令功能

**章节**: 3.1.13

**方法**: GET

**URL**: `/redfish/v1/RegistryStore/Messages/en/file_id`

**描述**: 查询归档的BMC 事件上报注册文件资源命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/RegistryStore/Messages/en/file_id'
```

---

