class thread_two:

  def __init__(self,i):   # initial action
    print(" start "+str(i))

  def thread(self,i,q): # class body
    import time
    import random
    time.sleep(0.5)
    ssr=q.get()
    if ssr==1:
      dt=1
    else:
      dt=-1
    q.put(dt)   # set value to queu
    return
