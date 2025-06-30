class thread_one:

  def __init__(self,i):   # initial action
    print(" start "+str(i))

  def thread(self,i,q): # class body
    import time
    import random
    a=q.get()
    #print("a")
    if a<0.0:
      ssr=1
    else:
      ssr=0
    q.put(ssr)   # set value to queu
    return
