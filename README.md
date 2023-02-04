<h1 align="center">MicroPython SmartConfig CModule</h1>

<p align="center"><img src="https://img.shields.io/badge/Licence-MIT-green.svg?style=for-the-badge" /></p>

### 项目介绍

为`MicroPython`提供`SmartConfig`相关功能

### 添加模块

* 将`ports/esp32/`下的文件夹复制到`MicroPython`项目对应位置
* 使用如下命令编译固件：

	```bash
	cd micropython/ports/esp32
	make USER_C_MODULES=../cmodules/micropython.cmake
	```

### 如何使用

参考项目目录下`main.py`文件中的代码，同时还可以 [前往B站](https://www.bilibili.com/video/BV1N34y1971S/) 观看配网演示视频

### 模块方法列表

* `start()`：开启配网功能

* `success()`：获取配网信息状态

	* `True`：表示已获取配网信息
	* `False`：表示未获取到配网信息

* `info()`：获取配网信息，返回值包含如下信息：

	```python
	('ssid', 'password', 'sc_type', 'token')
	```

### 模块常量列表

* `TYPE_UNKNOWN`：配网类型`未知`
* `TYPE_ESPTOUCH`：配网类型为`ESPTouch`
* `TYPE_AIRKISS`：配网类型为`AirKiss`

### 参考资料

* [smartconfig Example](https://github.com/espressif/esp-idf/tree/master/examples/wifi/smart_config)
* [ESP32-C3 MicroPython 固件编译环境搭建教程](https://gitee.com/walkline/esp32-c3_micropython_firmware)
* [WSL 下加速 Github 克隆速度](https://walkline.wang/blog/archives/263)

### 合作交流

* 联系邮箱：<walkline@163.com>
* QQ 交流群：
	* 走线物联：[163271910](https://jq.qq.com/?_wv=1027&k=xtPoHgwL)
	* 扇贝物联：[31324057](https://jq.qq.com/?_wv=1027&k=yp4FrpWh)

<p align="center"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_walkline.png" width="300px" alt="走线物联"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_bigiot.png" width="300px" alt="扇贝物联"></p>
