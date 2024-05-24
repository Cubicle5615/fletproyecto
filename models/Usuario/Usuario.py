class Usuario:
  def __init__(self, nombre, id, numeroDeKills, personajeFav, servidor=None):
    self.nombre = nombre
    self._id = id
    self.numeroDeKills = numeroDeKills
    self.personajeFav = personajeFav
    self.servidor = servidor

  def getId(self):
    return self._id

  def setId(self, id):
    self._id = id

  def iniciarSesion(self):
    pass

  def cerrarSesion(self):
    pass

  def cambiarContrasena(self, nuevaContrasena):
    pass
