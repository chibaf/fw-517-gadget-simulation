from gadget_class import gagdet

raspi=gagdet()
#
raspi.set_gpio(1)
raspi.step(3)
print(raspi.logger())
#
raspi.set_gpio(0)
raspi.step(4)
print(raspi.logger())