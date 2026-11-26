class Maleta:
    def __init__(self, propietario: str, peso: float):
        self.propietario = propietario
        self.__peso = peso

    def mostrar_info(self):
        print("Propietario:", self.propietario)
        print("Peso de la maleta:", self.__peso, "kg")

    def get_peso(self) -> float:
        return self.__peso


maleta_ana = Maleta("Ana", 18.5)
maleta_luis = Maleta("Luis", 23.0)

maleta_ana.mostrar_info()
maleta_luis.mostrar_info()
print("Peso consultado:", maleta_ana.get_peso(), "kg")
