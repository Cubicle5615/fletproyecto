class Personaje:
  def __init__(self, faccion, arma, cartaDeHabilidad, cartaDeBoosteo, armaSecundaria, skin):
    self.faccion = faccion
    self.arma = arma
    self.cartaDeHabilidad = cartaDeHabilidad
    self.cartaDeBoosteo = cartaDeBoosteo
    self.armaSecundaria = armaSecundaria
    self._skin = skin

  def getSkin(self):
    return self._skin

  def setSkin(self, skin):
    self._skin = skin

  def usarHabilidad(self, personaje):
    pass

  def usarBoost(self, personaje):
    pass