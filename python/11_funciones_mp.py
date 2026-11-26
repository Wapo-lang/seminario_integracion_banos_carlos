print("Sistema sencillo de vuelos del aeropuerto")


def anunciar_embarque(vuelo):
    print("Atencion: inicia el embarque del vuelo", vuelo)


anunciar_embarque("AV101")
anunciar_embarque("AV202")


def saludar_pasajero(nombre):
    print("Bienvenido al aeropuerto,", nombre)


saludar_pasajero("Carlos")


def calcular_precio(total_billetes, precio_billete):
    return total_billetes * precio_billete


total = calcular_precio(2, 150.50)
print("Total de los billetes:", round(total, 2))


def verificar_equipaje(pasajero, maletas):
    if maletas <= 2:
        print(f"{pasajero} puede pasar con {maletas} maletas")
    else:
        print(f"{pasajero} debe pagar equipaje adicional")


verificar_equipaje("Ana", 1)
verificar_equipaje("Luis", 3)
