class gagdet():

  def __init__(self):
    self.tc=0.0
    self.ssr1=0
    
  def set_gpio(self,ssr): # GPIO on/off
      self.ssr1=ssr
      
  def step(self,n):  # change Tc by time step
    for i in range(0,n):
      if self.ssr1==1:
        self.tc=self.tc+0.05
      else:
        self.tc=self.tc-0.05
      
  def logger(self):  # values of logger
      return self.tc