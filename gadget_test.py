from gadget_class import gagdet

raspi=gagdet()
ret=raspi.set_gpio(1)
print(ret)
print(raspi.logger())