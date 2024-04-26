<h1 align="center">MicroPython SmartConfig CModule</h1>

<p align="center"><img src="https://img.shields.io/badge/Licence-MIT-green.svg?style=for-the-badge" /></p>

## 项目介绍

为`MicroPython`提供`SmartConfig`相关功能，该模块已[提交 PR](https://github.com/micropython/micropython/pull/13658)，欢迎前往测试并留言支持。

相较于 [之前的版本](https://gitee.com/walkline/micropython-smartconfig-cmodule/tree/adapts_to_idf_443/)，这次更新了以下内容：

* `ESP-IDF`更新至`v5.0.4`
* 去掉了`.py`文件中的辅助函数，改为使用`ESP-IDF`原生`API`实现
* 增加了对`EspTouch V2`协议支持

## 如何添加模块

* 在`MicroPython`项目同级目录克隆或粘贴本项目文件夹，并将文件夹重命名为`smartconfig`

	```bash
	git clone https://gitee.com/walkline/micropython-smartconfig-cmodule.git smartconfig
	```

* 根据`MicroPython`项目固件编译说明做好前期准备

* 使用如下命令编译固件：

	```bash
	cd micropython/ports/esp32
	make USER_C_MODULES=../../../../smartconfig/cmodules/micropython.cmake
	```

## 模块使用说明

参考项目目录下`main.py`文件中的代码，同时还可以 [前往B站](https://www.bilibili.com/video/BV1N34y1971S/) 观看配网演示视频。

查看 [模块方法列表](./DOCS.md)

## 手机操作说明

* 手机连接`2.4G`无线网络（**重要**）
* 任意选择一个`微信公众号`或`App`：
	* 关注`安信可科技`微信公众号，点击`应用开发→微信配网`
	* 关注`乐鑫信息科技`微信公众号，点击`商铺→Airkiss 设备`
	* 安装`EspTouch App`点击`EspTouch`
	* 安装`腾讯连连 App`，任意添加一个设备

* 输入`WiFi 密码`后点击`连接`按钮

## 获取 EspTouch App

* [Esptouch For Android](https://github.com/EspressifApp/EsptouchForAndroid/releases)

* [App Store 上的“Espressif Esptouch”](https://apps.apple.com/cn/app/espressif-esptouch/id1071176700)

## 已知问题

* `2.4G`和`5G`混合网络下使用`AirKiss`协议无法获取相关信息
* 某些（我的）`WiFi6`路由器使用`AirKiss`协议无法获取相关信息

## 参考资料

* [smartconfig Example](https://github.com/espressif/esp-idf/tree/master/examples/wifi/smart_config)

* [App | 乐鑫科技](https://www.espressif.com.cn/zh-hans/support/download/apps?keys=&field_technology_tid%5B%5D=20
)

## 合作交流

* 联系邮箱：<walkline@163.com>
* QQ 交流群：
	* 走线物联：[163271910](https://jq.qq.com/?_wv=1027&k=xtPoHgwL)
	* 扇贝物联：[31324057](https://jq.qq.com/?_wv=1027&k=yp4FrpWh)

<p align="center"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_walkline.png" width="300px" alt="走线物联"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_bigiot.png" width="300px" alt="扇贝物联"></p>
