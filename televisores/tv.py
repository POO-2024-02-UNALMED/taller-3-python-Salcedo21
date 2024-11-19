from .control import Control
from .marca import Marca
class TV:
  _numTV = 0


  def __init__(self, marca,control= None, canal=1, precio=500, estado= False, volumen=1):
    self._marca = marca
    self._canal = canal
    self._precio = precio
    self._estado = estado
    self._volumen = volumen
    self._control = control
    TV._numTV += 1
    
  def getMarca(self):
    return self._marca
  
  def setMarca(self, marca):
    self._marca = marca

  @classmethod
  def getNumTV():
    return TV._numTV
  
  @classmethod
  def setNumTV(cls, numTV):
    cls._numTV = numTV
  
  def getCanal(self):
    return self._canal
  
  def setCanal(self, canal):
    if self._estado and 1 <= canal <= 120:
     self._canal = canal

  def getPrecio(self):
    return self._precio
  
  def setPrecio(self, precio):
    self._precio = precio

  def getVolumen(self):
    return self._volumen
  
  def setVolumen(self, volumen):
    if self._estado and 1 <= volumen <= 7:
     self._volumen = volumen
  
  def getControl(self):
    return self._control
  
  def setControl(self, control):
    self._control = control
  
  def turnOn(self):
    self._estado = True
  
  def turnOff(self):
    self._estado = False

  def getEstado(self):
    return self._estado
  
  def canalUp(self):
    if self._canal < 120 and self._estado:
      self._canal += 1
  
  def canalDown(self):
    if self._canal > 1 and self._estado:
      self._canal -= 1

  def volumenUp(self):
    if self._volumen < 7 and self._estado:
      self._volumen += 1
  
  def volumenDown(self):
    if self._volumen > 1 and self._estado:
      self._volumen -= 1
