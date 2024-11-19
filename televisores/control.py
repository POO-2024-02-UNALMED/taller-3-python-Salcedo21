
class Control:
  def __init__(self, tv=None):
    self._tv = tv
  
  def getTv(self):
    return self._tv
  
  def setTv(self, tv):
    self._tv = tv

  def turnOn(self):
    if self.tv.estado :
      self._tv.turnOn()
  
  def turnOff(self):
   if self.tv.estado :
    self._tv.turnOff()
  
  def canalUp(self):
   if self.tv.estado :
    self._tv.canalUp()
  
  def canalDown(self):
   if self.tv.estado :
    self._tv.canalDown()
  
  def volumenUp(self):
    if self.tv.estado :
     self._tv.volumenUp()
  
  def volumenDown(self):
   if self.tv.estado :
    self._tv.volumenDown()
  
  def setCanal(self):
   if self.tv.estado :
    self._tv.setCanal()
  
  def setVolumen(self):
    if self.tv.estado :
     self._tv.setVolumen()

  def enlazar(self,tv):
    self.tv = tv
    self.tv.setControl(self)
