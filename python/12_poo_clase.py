class Guerrero:
    nombre: str
    raza: str

    def __init__(self, nombre:str, raza:str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Raza ", self.raza)

goku = Guerrero("Goku", "Sayajin")
vegeta = Guerrero("Vegeta", "Sayajin")
piccolo = Guerrero("Piccolo", "Namkiano")
carlos = Guerrero("Carlos", "Humano")

goku.mostrar_info()
vegeta.mostrar_info()
piccolo.mostrar_info()
carlos.mostrar_info()