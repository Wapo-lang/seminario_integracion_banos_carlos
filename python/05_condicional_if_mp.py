print("Control de embarque del aeropuerto")

vuelo = "A-204"
maletas = 3

if maletas <= 1:
    print("Puedes llevar tu equipaje a mano.")
elif maletas == 2:
    print("Tienes dos maletas. Puedes pasar por facturación.")
else:
    print("Tienes varias maletas. Debes ir al mostrador de equipaje.")

hora_salida = 18
if hora_salida < 12:
    print("Tu vuelo sale en la mañana.")
elif hora_salida <= 18:
    print("Tu vuelo sale por la tarde.")
else:
    print("Tu vuelo sale por la noche.")

pasajero = "Laura"
if pasajero == "Laura":
    print(f"{pasajero}, tu vuelo {vuelo} está en la puerta 7.")
else:
    print("Tu vuelo está programado correctamente.")
