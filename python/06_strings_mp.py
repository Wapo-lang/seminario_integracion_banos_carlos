"""
Manejo de cadenas de texto en un aeropuerto
"""

pasajero = "Ana Torres"
print(f"Pasajera: {pasajero}")
print(f"Tipo de dato: {type(pasajero)}")

mensaje = "El vuelo sale desde la terminal norte"
print("Mensaje original:", mensaje)
print("En mayusculas:", mensaje.upper())
print("En minusculas:", mensaje.lower())

mensaje_vuelo = "El vuelo viajara a Lima"
mensaje_actualizado = mensaje_vuelo.replace("Lima", "Bogota")
print("Destino anterior:", mensaje_vuelo)
print("Destino actualizado:", mensaje_actualizado)
