class Persona:
    def __init__(self, nombre: str, identificacion: str):
        self.nombre = nombre
        self.identificacion = identificacion

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Identificacion:", self.identificacion)


class Pasajero(Persona):
    def __init__(self, nombre: str, identificacion: str, destino: str):
        super().__init__(nombre, identificacion)
        self.destino = destino

    def mostrar_destino(self):
        print("Destino:", self.destino)


pasajero1 = Pasajero("Ana Torres", "P12345", "Lima")
pasajero2 = Pasajero("Luis Mora", "P67890", "Quito")

pasajero1.mostrar_info()
pasajero1.mostrar_destino()
pasajero2.mostrar_info()
pasajero2.mostrar_destino()
