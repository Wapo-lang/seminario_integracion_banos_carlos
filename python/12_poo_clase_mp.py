class Vuelo:
    codigo: str
    destino: str

    def __init__(self, codigo: str, destino: str):
        self.codigo = codigo
        self.destino = destino

    def mostrar_info(self):
        print("Vuelo:", self.codigo)
        print("Destino:", self.destino)


vuelo1 = Vuelo("AV101", "Bogota")
vuelo2 = Vuelo("AV202", "Lima")
vuelo3 = Vuelo("AV303", "Quito")

vuelo1.mostrar_info()
vuelo2.mostrar_info()
vuelo3.mostrar_info()
