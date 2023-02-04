"""
Copyright © 2024 Walkline Wang (https://walkline.wang)
Gitee: https://gitee.com/walkline/micropython-smartconfig-cmodule
"""
import network
import time
import smartconfig

import esp
esp.osdebug(0)


TYPES = {
	smartconfig.TYPE_ESPTOUCH: 'ESPTOUCH',
	smartconfig.TYPE_AIRKISS: 'AIRKISS',
	smartconfig.TYPE_ESPTOUCH_AIRKISS: 'ESPTOUCH_AIRKISS',
	smartconfig.TYPE_ESPTOUCH_V2: 'ESPTOUCH_V2'
}

TIMEOUT = 120_000 # ms

def run_test():
	sta = network.WLAN(network.STA_IF)
	_ = sta.active(True)

	smartconfig.type(smartconfig.TYPE_ESPTOUCH_AIRKISS)
	print(f'smartconfig type: {TYPES[smartconfig.type()]}')

	smartconfig.start()

	start_ms = time.ticks_ms()

	while not smartconfig.done():
		if time.ticks_ms() - start_ms > TIMEOUT:
			print('smartconfig timeout')
			smartconfig.stop()
			return

		time.sleep_ms(100)

	print('smartconfig done, ', end='')

	if sta.status() == network.STAT_GOT_IP:
		print('and connected to ap')
		print(f'smartconfig info: {smartconfig.info()}')
		print(f'  - ssid: "{smartconfig.ssid()}"')
		print(f'  - password: "{smartconfig.password()}"')
		print(f'  - bssid: {smartconfig.bssid()}')
		print(f'  - type: {smartconfig.type()}({TYPES[smartconfig.type()]})')

		if smartconfig.rvd_data():
			print(f'  - rvd_data: {smartconfig.rvd_data()}') # EspTouch V2 custom data
	else:
		# maybe wrong password or other situations
		print('but failed connect to ap')

	smartconfig.stop()


if __name__ == '__main__':
	run_test()
