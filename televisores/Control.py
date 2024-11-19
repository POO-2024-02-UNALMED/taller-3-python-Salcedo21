from tv import TV
class control:
  def __init__(self, tv):
    self._tv = tv
  
  def getTv(self):
    return self._tv
  
  def setTv(self, tv):
    self._tv = tv

  def turnOn(self):
    self._tv.turnOn()
  
  def turnOff(self):
    self._tv.turnOff()
  
  def canalUp(self):
    self._tv.canalUp()
  
  def canalDown(self):
    self._tv.canalDown()
  
  def volumenUp(self):
    self._tv.volumenUp()
  
  def volumenDown(self):
    self._tv.volumenDown()
  
  def setCanal(self):
    self._tv.setCanal()
  
  def setVolumen(self):
    self._tv.setVolumen()

  def enlazar(self,tv):
    self.tv = tv
    self.tv.setControl
