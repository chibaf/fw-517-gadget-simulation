class thread_one:

  def __init__(self,i):   # initial action
    print(" start "+str(i))

  def thread(self,i,q): # class body
    import time
    import random
#    time.sleep(1)
    #a=q.get()
    #print("a")
    ret = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]  # return value
    q.put(ret)   # set value to queu
    return
