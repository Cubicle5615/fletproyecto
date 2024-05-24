class Mapa:
  def __init__(self, mapaElegido, tamanoMapa, numerojugadores, dificultadIA, activarIA):
    self.mapaElegido = mapaElegido
    self.tamanoMapa = tamanoMapa
    self.numerojugadores = numerojugadores
    self.dificultadIA = dificultadIA
    self.activarIA = activarIA

  def getnumeroDeIA(self):
    return self._numeroDeIA

  def setnumeroDeIA(self, numeroDeIA):
    self._numeroDeIA = numeroDeIA

  def cambiarMapa(self):
    pass
