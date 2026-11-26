class TransporteAeropuerto:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def anunciar(self):
        print(self.nombre, "esta disponible en el aeropuerto")


class Autobus(TransporteAeropuerto):
    def anunciar(self):
        print(self.nombre, "lleva pasajeros a la terminal")


class Avion(TransporteAeropuerto):
    def anunciar(self):
        print(self.nombre, "esta listo para el embarque")


transportes = [Autobus("Autobus 5"), Avion("Vuelo AV101")]
for transporte in transportes:
    transporte.anunciar()
