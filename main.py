"""
Copyright © 2023 Walkline Wang (https://walkline.wang)
Gitee: https://gitee.com/walkline/micropython-smartconfig-cmodule
"""
from utime import sleep
import network
import socket
import smartconfig


def inet_pton(ip_str:str):
	'''将字符串 IP 地址转换为字节串'''
	ip_bytes = b''
	ip_segs = ip_str.split('.')

	for seg in ip_segs:
		ip_bytes += int(seg).to_bytes(1, 'little')

	return ip_bytes

def send_ack(local_ip, local_mac):
	'''向手机发送配网完成通知'''
	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	data = smartconfig.info()[2].to_bytes(1, 'little') + local_mac
	port = 10000 # airkiss 端口号

	if smartconfig.info()[3] == smartconfig.TYPE_ESPTOUCH:
		data += inet_pton(local_ip)
		port = 18266 # esptouch 端口号

	for _ in range(30):
		sleep(0.1)
		try:
			udp.sendto(data, ('255.255.255.255', port))
		except OSError:
			pass

station = network.WLAN(network.STA_IF)
station.active(True)

smartconfig.start()

# 手机连接 2.4G 无线网络（重要）
# 关注 安信可科技 微信公众号，点击 应用开发→微信配网，或
# 关注 乐鑫信息科技 微信公众号，点击 商铺→Airkiss 设备，或
# 安装 EspTouch app，点击 EspTouch，或
# 安装 腾讯连连 app，任意添加一个设备
# 输入 Wi-Fi密码 后点击 连接按钮

while not smartconfig.success():
	sleep(0.5)

ssid, password, sc_type, token = smartconfig.info()
print(smartconfig.info())

# 以下代码用于向手机发送配网完成通知，可选项
station.connect(ssid, password)

while not station.isconnected():
	sleep(0.5)

send_ack(station.ifconfig()[0], station.config('mac'))