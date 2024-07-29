<h1 align="center">MicroPython SmartConfig CModule</h1>
<p align="center"><img src="https://img.shields.io/badge/Licence-MIT-green.svg?style=for-the-badge" /></p>

## 模块方法列表

* `version()`：获取 SmartConfig 内部版本号
* `start()`：开启配网功能
* `stop()`：停止配网功能
* `done()`：获取配网完成状态
	* `True`：已获取配网信息
	* `False`：未获取到配网信息
* `timeout()`：设置/获取配网超时时间，单位为秒，有效值范围：`15~255`
* `fast_mode()`：设置/获取配网模式，默认为正常模式
* `v2_key()`：设置/获取 EspTouch V2 协议使用的密钥，长度为`16`，传递`None`或空字符串清空秘钥
* `info()`：获取配网信息，返回值包含如下信息：

	```python
	# v2_data - EspTouch V2 custom data
	tuple('ssid', 'password', b'bssid', type[, b'v2_data'])
	```

* `ssid()`：获取`ssid`
* `password()`：获取`password`
* `bssid()`：获取`bssid`
* `type()`：设置/获取配网协议类型
* `v2_data()`：获取`EspTouch V2`自定义数据

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
