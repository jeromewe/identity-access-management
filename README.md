# Identity and Access Management(身份和访问管理)

[![Python3](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-2.2-brightgreen.svg?style=plastic)](https://www.djangoproject.com/)

身份和访问管理 是CMP里重要的组成部分负责管理用户与凭证，是符合多租户架构的系统。

身份和访问管理 使用 Python3 / Django 进行开发，遵循 Web 2.0 规范，配备了业界领先的方案，交互界面美观、用户体验好。

身份和访问管理 采纳分布式架构，支持Docker部署方式


## 核心功能列表

<table class="subscription-level-table">
    <tr class="subscription-level-tr-border">
        <td class="features-first-td-background-style" rowspan="4">身份验证 Authentication</td>
        <td class="features-second-td-background-style" rowspan="3" >登录认证
        </td>
        <td class="features-third-td-background-style">统一登录和认证
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-third-td-background-style">LDAP 认证
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-third-td-background-style">RADIUS 认证
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-third-td-background-style">支持 OpenID，实现单点登录
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-second-td-background-style">多因子认证
        </td>
        <td class="features-third-td-background-style">MFA（Microsoft Authenticator）
        </td>
        <td class="features-third-td-background-style">RADIUS 二次认证
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-first-td-background-style" rowspan="9">账号管理 Account</td>
        <td class="features-second-td-background-style" rowspan="2">多账号管理
        </td>
        <td class="features-third-td-background-style">管理用户管理
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-third-td-background-style">系统用户管理
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-second-td-background-style" rowspan="4">统一密码管理
        </td>
        <td class="features-third-td-background-style">
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-third-td-background-style">自动生成密码
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-third-td-background-style">密码自动推送
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-third-td-background-style">密码过期设置
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-outline-td-background-style" rowspan="2">密码变更
        </td>
        <td class="features-outline-td-background-style">定期修改密码
        </td>
    </tr>
    <tr class="subscription-level-tr-border">
        <td class="features-outline-td-background-style">生成随机密码
        </td>
    </tr> 
</table>

## 安装及使用指南

-  [Docker 快速安装文档]()
-  [Step by Step 安装文档]()
-  [完整文档]()

## 演示截屏

- [系统截图]()
- [视频演示]()

## License & Copyright

Copyright (c) <wenhaijie>, All rights reserved.

Licensed under The GNU General Public License version 3 (GPLv3)  (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
