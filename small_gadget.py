from gadget_class import gagdet
import time

raspi=gagdet()
raspi.set_gpio(0)
raspi.step(2)

while True:
  if raspi.logger()<0.0:
    raspi.set_gpio(1)
  else:
    raspi.set_gpio(0)
  raspi.step(2)
  time.sleep(2)
  
  print(raspi.logger())