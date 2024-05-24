<h1 align="center">MicroPython SmartConfig CModule</h1>
<p align="center"><img src="https://img.shields.io/badge/Licence-MIT-green.svg?style=for-the-badge" /></p>

## 模块方法列表

* `start()`：开启配网功能
* `stop()`：停止配网功能
* `done()`：获取配网完成状态
	* `True`：已获取配网信息
	* `False`：未获取到配网信息
* `info()`：获取配网信息，返回值包含如下信息：

	```python
	# rvd_data - EspTouch V2 custom data
	tuple('ssid', 'password', b'bssid', type[, b'rvd_data'])
	```

* `ssid()`：获取`ssid`
* `password()`：获取`password`
* `bssid()`：获取`bssid`
* `type()`：设置/获取配网协议类型
* `rvd_data()`：获取`EspTouch V2`自定义数据

### 模块常量列表

* `TYPE_ESPTOUCH`：配网协议类型为`EspTouch`
* `TYPE_AIRKISS`：配网协议类型为`AirKiss`
* `TYPE_ESPTOUCH_AIRKISS`：配网协议类型为`EspTouch`+`AirKiss`
* `TYPE_ESPTOUCH_V2`：配网协议类型为`EspTouch V2`

## 合作交流

* 联系邮箱：<walkline@163.com>
* QQ 交流群：
	* 走线物联：[163271910](https://jq.qq.com/?_wv=1027&k=xtPoHgwL)
	* 扇贝物联：[31324057](https://jq.qq.com/?_wv=1027&k=yp4FrpWh)

<p align="center"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_walkline.png" width="300px" alt="走线物联"><img src="https://gitee.com/walkline/WeatherStation/raw/docs/images/qrcode_bigiot.png" width="300px" alt="扇贝物联"></p>
