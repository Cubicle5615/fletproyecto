from multipledispatch import dispatch

class Personaje:
    def __init__(self, faccion, arma, carga, vida, pistola, default):
        self.faccion = faccion
        self.arma = arma
        self.carga = carga
        self.vida = vida
        self.pistola = pistola
        self.default = default

class Faccion:
    def __init__(self, nombre):
        self.nombre = nombre

    @dispatch(Personaje)
    def cambiar(self, personaje):
        personaje.faccion = self.nombre
        print(f"{personaje.nombre} ahora pertenece a la facción {self.nombre}.")

class FaccionJedi(Faccion):
    @dispatch(Personaje)
    def cambiar(self, personaje):
        super().cambiar(personaje)
        print(f"Tu {personaje.nombre} a entrenado, tu {personaje.faccion} obtiene habilidades especiales.")

revan = Personaje("Darth Revan", "Sith")
sith = Faccion("Sith")
jedi = FaccionJedi("Personaje")

sith.cambiar(revan)
jedi.cambiar(revan)