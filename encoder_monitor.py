from epos_interface import Epos
import time

epos = Epos()
epos.open()

print("Connected.")

while True:
	status = epos.status()
	print("Position:", status["position"])

	time.sleep(0.1)
