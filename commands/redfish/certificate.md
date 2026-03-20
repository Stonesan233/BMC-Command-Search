# Redfish 证书管理接口

> 共 7 个接口 (有效: 7, 有请求体: 0)

## 查询证书服务信息

**章节**: 3.12.1

**方法**: GET

**URL**: `/redfish/v1/CertificateService`

**描述**: 查询服务器当前证书服务的信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/CertificateService'
```

---

## 修改证书服务信息

**章节**: 3.12.2

**方法**: PATCH

**URL**: `/redfish/v1/CertificateService`

**描述**: 修改服务器当前证书服务的相关属性。

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/CertificateService' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询证书路径信息

**章节**: 3.12.3

**方法**: GET

**URL**: `/redfish/v1/CertificateService/CertificateLocations`

**描述**: 查询服务器当前各业务使用的所有证书资源路径信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/CertificateService/CertificateLocations'
```

---

## 导入CA 证书

**章节**: 3.12.4

**方法**: POST

**URL**: `/redfish/v1/CertificateService/Actions/`

**描述**: CA证书导入。所有BMC业务使用的CA证书进行统一管理，不再按业务单独提供各自证书管理接口。此接口导入证书会影响到其他所有包含CA证书（远程HTTPS服务器、Syslog服务端证书、Smtp服务端证书...

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/CertificateService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 删除CA 证书

**章节**: 3.12.5

**方法**: POST

**URL**: `/redfish/v1/CertificateService/Actions/`

**描述**: CA证书删除。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/CertificateService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 导入CA 证书的吊销列表

**章节**: 3.12.6

**方法**: POST

**URL**: `/redfish/v1/CertificateService/Actions/`

**描述**: 导入CA证书的吊销列表。证书吊销列表和所有其他BMC业务公用，此接口导入吊销列表会影响到其他包含CA证书吊销列表的接口。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/CertificateService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

## 生成CSR

**章节**: 3.12.7

**方法**: POST

**URL**: `/redfish/v1/CertificateService/Actions/`

**描述**: 生成SSL证书的CSR。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/CertificateService/Actions/' -H 'Content-Type: application/json' -d '{}'
```

---

