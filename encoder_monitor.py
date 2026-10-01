import time

from epos_interface import Epos

epos = Epos()
epos.open()

print("Connected.")

try:
    while True:
        status = epos.status()
        print("Position:", status["position"])

        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopping.")
finally:
    epos.close()
