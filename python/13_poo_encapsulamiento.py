class Guerrero:
    nombre: str
    __poder: int

    def __init__(self, nombre:str,poder:str):
        self.nombre= nombre
        self.__poder= poder

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Poder", self.__poder)

    def get_poder(self):
        return self.__poder

goku = Guerrero("Goku",50000000000000000)
vegeta= Guerrero("Vegetta", 450000000000000)
carlos= Guerrero("Carlos", 40)

vegeta.mostrar_info
carlos.mostrar_info
goku.mostrar_info

print(goku.nombre)
print(carlos.nombre)
print(vegeta.get_poder())class Guerrero:
    nombre: str
    __poder: int

    def __init__(self, nombre:str,poder:str):
        self.nombre= nombre
        self.__poder= poder

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Poder", self.__poder)

    def get_poder(self):
        return self.__poder

goku = Guerrero("Goku",50000000000000000)
vegeta= Guerrero("Vegetta", 450000000000000)
carlos= Guerrero("Carlos", 40)

vegeta.mostrar_info
carlos.mostrar_info
goku.mostrar_info

print(goku.nombre)
print(carlos.nombre)
print(vegeta.get_poder())