# Redfish 账户管理接口

> 共 34 个接口 (有效: 31, 有请求体: 26)

## Web 二次认证

**章节**: 3.5.9

**方法**: POST

**URL**: `/redfish/v1/AccountService/Accounts`

**描述**: 在Web页面操作中，二次认证包括：修改VNC密码、创建新用户、删除用户、修改指定用户信息、SSH公钥导入、SSH公钥删除、修改自定义角色权限、修改指定域控制器、修改SNMPV3加密密码的信息、新增/修...

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Accounts' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 查询用户服务信息

**章节**: 3.6.1

**方法**: GET

**URL**: `/redfish/v1/AccountService`

**描述**: 查询服务器当前用户服务信息，包括密码长度、允许错误密码次数、锁定时长等。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService'
```

---

## 修改用户服务信息

**章节**: 3.6.2

**方法**: PATCH

**URL**: `/redfish/v1/AccountService`

**描述**: 修改服务器当前用户服务信息，包括允许错误密码次数、锁定时长等。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/AccountService' -H 'Content-Type: application/json' -d '{  "TransferProtocol": "HTTPS",  "Path": "/tmp/web/aaa.tar.gz" }'
```

---

## 查询用户集合资源信息

**章节**: 3.6.3

**方法**: GET

**URL**: `/redfish/v1/AccountService/Accounts`

**描述**: 查询服务器当前用户集合资源信息。

**请求体**:
```json
{
  "TransferProtocol": "HTTPS",
  "Path": "/tmp/web/aaa.tar.gz"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/Accounts'
```

---

## 查询指定用户资源信息

**章节**: 3.6.4

**方法**: GET

**URL**: `/redfish/v1/AccountService/Accounts/member_id`

**描述**: 查询指定用户资源信息。

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
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/Accounts/member_id'
```

---

## 创建新用户

**章节**: 3.6.5

**方法**: POST

**URL**: `/redfish/v1/AccountService/Accounts`

**描述**: 创建新用户。

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Accounts' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 删除用户

**章节**: 3.6.6

**方法**: DELETE

**URL**: `/redfish/v1/AccountService/Accounts/account_id`

**描述**: 删除指定用户。

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
curl -k -u admin:password -X DELETE 'https://<bmc_ip>/redfish/v1/AccountService/Accounts/account_id'
```

---

## 修改指定用户信息

**章节**: 3.6.7

**方法**: PATCH

**URL**: `/redfish/v1/AccountService/Accounts/account_id`

**描述**: 修改指定用户的用户名、密码、权限、锁定状态、使能状态、登录接口等信息。

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
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/AccountService/Accounts/account_id' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 双因素认证的根证书导入

**章节**: 3.6.8

**方法**: POST

**URL**: `/redfish/v1/AccountService/Oem/Huawei/Actions/`

**描述**: 双因素认证的根证书导入。  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2.0.1版本...

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
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Oem/Huawei/Actions/' -H 'Content-Type: application/json' -d '{  "Oem": {   "Huawei": {    "EncryptionEnabled": false,    "FloppyDriveEnabled": true   }  } }'
```

---

## 双因素认证的根证书删除

**章节**: 3.6.9

**描述**: 双因素认证的根证书删除。  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2.0.1版本...

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
# 双因素认证的根证书删除
```

---

## 双因素认证的用户的客户端证书导入命令功能

**章节**: 3.6.10

**方法**: POST

**URL**: `/redfish/v1/AccountService/Accounts/account_id/Oem/`

**描述**: 双因素认证的用户的客户端证书导入命令功能

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Accounts/account_id/Oem/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Connect",  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO" }'
```

---

## 双因素认证的用户的客户端证书删除命令功能

**章节**: 3.6.11

**方法**: POST

**URL**: `/redfish/v1/AccountService/Accounts/account_id/Oem/`

**描述**: 双因素认证的用户的客户端证书删除命令功能

**请求体**:
```json
{
  "VmmControlType": "Connect",
  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Accounts/account_id/Oem/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Connect",  "Image": "nfs://device_ip/usr/SLE-12-Server-DVD-x86_64-GM-DVD1.ISO" }'
```

---

## 双因素认证的客户端证书吊销列表导入命令功能

**章节**: 3.6.12

**方法**: POST

**URL**: `/redfish/v1/AccountService/Oem/Huawei/Actions/`

**描述**: 双因素认证的客户端证书吊销列表导入命令功能

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Oem/Huawei/Actions/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Disconnect" }'
```

---

## 双因素认证的客户端证书吊销列表删除命令功能

**章节**: 3.6.13

**方法**: POST

**URL**: `/redfish/v1/AccountService/Oem/Huawei/Actions/`

**描述**: 双因素认证的客户端证书吊销列表删除命令功能

**请求体**:
```json
{
  "VmmControlType": "Disconnect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Oem/Huawei/Actions/' -H 'Content-Type: application/json' -d '{  "VmmControlType": "Disconnect" }'
```

---

## SSH 公钥导入

**章节**: 3.6.14

**方法**: POST

**URL**: `/redfish/v1/AccountService/Accounts/account_id/Oem/`

**描述**: SSH公钥导入。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Accounts/account_id/Oem/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## SSH 公钥删除

**章节**: 3.6.15

**方法**: POST

**URL**: `/redfish/v1/AccountService/Accounts/account_id/Oem/`

**描述**: SSH公钥删除。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Accounts/account_id/Oem/' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 查询角色集合资源信息

**章节**: 3.6.16

**方法**: GET

**URL**: `/redfish/v1/AccountService/Roles`

**描述**: 查询服务器当前角色集合资源信息。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/Roles'
```

---

## 查询指定角色信息

**章节**: 3.6.17

**方法**: GET

**URL**: `/redfish/v1/AccountService/Roles/role_id`

**描述**: 查询服务器指定角色信息。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/Roles/role_id'
```

---

## 修改自定义角色权限

**章节**: 3.6.18

**方法**: PATCH

**URL**: `/redfish/v1/AccountService/Roles/role_id`

**描述**: 修改指定角色的权限。

**请求体**:
```json
{
  "USBStickControlType": "Connect"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/AccountService/Roles/role_id' -H 'Content-Type: application/json' -d '{  "USBStickControlType": "Connect" }'
```

---

## 创建自定义角色

**章节**: 3.6.19

**方法**: POST

**URL**: `/redfish/v1/AccountService/Roles`

**描述**: 创建自定义角色。

**curl命令**:
```bash
curl -k -u admin:password -X POST 'https://<bmc_ip>/redfish/v1/AccountService/Roles' -H 'Content-Type: application/json' -d '{}'
```

---

## 删除自定义角色

**章节**: 3.6.20

**方法**: DELETE

**URL**: `/redfish/v1/AccountService/Roles/role_id`

**描述**: 删除指定自定义角色。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X DELETE 'https://<bmc_ip>/redfish/v1/AccountService/Roles/role_id'
```

---

## 查询Ldap 服务资源

**章节**: 3.6.21

**方法**: GET

**URL**: `/redfish/v1/AccountService/LdapService`

**描述**: 查询Ldap资源。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/LdapService'
```

---

## 修改Ldap 功能开启使能

**章节**: 3.6.22

**方法**: PATCH

**URL**: `/redfish/v1/AccountService/LdapService`

**描述**: Ldap功能是否开启。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/AccountService/LdapService' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 查询Ldap 域控制器集合信息命令功能

**章节**: 3.6.23

**方法**: GET

**URL**: `/redfish/v1/AccountService/LdapService/LdapControllers`

**描述**: 查询Ldap 域控制器集合信息命令功能

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/LdapService/LdapControllers'
```

---

## 查询具体域控制器的信息

**章节**: 3.6.24

**方法**: GET

**URL**: `/redfish/v1/AccountService/LdapService/`

**描述**: 查询Ldap资源。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/LdapService/'
```

---

## 修改具体域控制器的信息

**章节**: 3.6.25

**方法**: PATCH

**URL**: `/redfish/v1/AccountService/LdapService/`

**描述**: 修改具体域控制器资源属性。

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/AccountService/LdapService/' -H 'Content-Type: application/json' -d '{  "Type": "URI",  "Content": "/tmp/ntp.keys" }'
```

---

## 具体域控制器Ldap 证书的导入

**章节**: 3.6.26

**描述**: 导入Ldap证书。  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2.0.1版本后CA...

**请求体**:
```json
{
  "Type": "URI",
  "Content": "/tmp/ntp.keys"
}
```

**curl命令**:
```bash
# 具体域控制器Ldap 证书的导入
```

---

## 具体域控制器Ldap 服务器证书吊销列表导入

**章节**: 3.6.27

**描述**: 导入Ldap服务器证书吊销列表。  此资源已经废弃，仅供兼容性用途使用。建议使用redfish/v1/CertificateService接口进行CA证书/吊销列表管理  自iBMC300 5.2.0...

**curl命令**:
```bash
# 具体域控制器Ldap 服务器证书吊销列表导入
```

---

## 查询权限映射资源信息

**章节**: 3.6.28

**方法**: GET

**URL**: `/redfish/v1/AccountService/PrivilegeMap`

**描述**: 查询权限映射资源信息。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/PrivilegeMap'
```

---

## 查询Kerberos 服务资源

**章节**: 3.6.29

**方法**: GET

**URL**: `/redfish/v1/AccountService/KerberosService`

**描述**: 查询Kerberos资源。

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/KerberosService'
```

---

## 修改Kerberos 功能开启使能命令功能

**章节**: 3.6.30

**方法**: PATCH

**URL**: `/redfish/v1/AccountService/KerberosService`

**描述**: 修改Kerberos 功能开启使能命令功能

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/AccountService/KerberosService' -H 'Content-Type: application/json' -d '{}'
```

---

## 查询Kerberos 域控制器集合信息命令功能

**章节**: 3.6.31

**方法**: GET

**URL**: `/redfish/v1/AccountService/KerberosService/`

**描述**: 查询Kerberos 域控制器集合信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/KerberosService/'
```

---

## 查询具体Kerberos 域控制器的信息命令功能

**章节**: 3.6.32

**方法**: GET

**URL**: `/redfish/v1/AccountService/KerberosService/`

**描述**: 查询具体Kerberos 域控制器的信息命令功能

**curl命令**:
```bash
curl -k -u admin:password -X GET 'https://<bmc_ip>/redfish/v1/AccountService/KerberosService/'
```

---

## 修改具体Kerberos 域控制器的信息

**章节**: 3.6.33

**方法**: PATCH

**URL**: `/redfish/v1/AccountService/KerberosService/`

**描述**: 修改具体Kerberos域控制器资源属性。

**curl命令**:
```bash
curl -k -u admin:password -X PATCH 'https://<bmc_ip>/redfish/v1/AccountService/KerberosService/' -H 'Content-Type: application/json' -d '{}'
```

---

