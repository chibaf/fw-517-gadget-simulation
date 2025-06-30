from gadget_class import gagdet
from thread_one_class import thread_one  # import thread body
import threading
import queue  # library for queu operation
import time

i=1   # counter
thread1=thread_one(i)
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)

raspi=gagdet() # initialzation
raspi.set_gpio(0)
#raspi.step(2)

q.put(raspi.logger())
th.start()
while True:
  if th.is_alive()==False:
    i=i+1
    a=q.get()
    raspi.set_gpio(a)
    thread1=thread_one(i)
    th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)
    q.put(raspi.logger())
    th.start()
  raspi.step(2)
  time.sleep(2)
  
  print(raspi.logger())