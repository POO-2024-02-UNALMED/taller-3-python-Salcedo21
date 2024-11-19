
class Control:
  def __init__(self, tv=None):
    self._tv = tv
  
  def getTv(self):
    return self._tv
  
  def setTv(self, tv):
    self._tv = tv

  def turnOn(self):
    if self._tv._estado :
      self._tv.turnOn()
  
  def turnOff(self):
   if self._tv._estado :
    self._tv.turnOff()
  
  def canalUp(self):
   if self._tv._estado :
    self._tv.canalUp()
  
  def canalDown(self):
   if self._tv._estado :
    self._tv.canalDown()
  
  def volumenUp(self):
    if self._tv._estado :
     self._tv.volumenUp()
  
  def volumenDown(self):
   if self._tv._estado :
    self._tv.volumenDown()
  
  def setCanal(self,canal):
   if self._tv._estado :
    self._tv.setCanal(canal)
  
  def setVolumen(self,canal):
    if self._tv._estado :
     self._tv.setVolumen(canal)

  def enlazar(self,tv):
    self._tv = tv
    self._tv.setControl(self)
