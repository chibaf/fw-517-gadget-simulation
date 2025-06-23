class gagdet():

  def __init__(self):
    self.tc=0.0
    self.ssr1=0
    
  def set_gpio(self,ssr):
      self.ssr1=ssr
      if self.ssr1==1:
        self.tc=self.tc+1
      return self.tc
      
  def logger(self):
      rtuen self.tc