print("Sistema de registro del aeropuerto")
nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre, "! Bienvenido al aeropuerto")
print("Tu vuelo sale desde la terminal principal")

cantidad_maletas = input("¿Cuántas maletas llevas? ")
print("Maletas registradas:", cantidad_maletas)

print("CONVERSIONES")
print("=== CHECK-IN AEROPUERTO ===")
cliente = input("Nombre del pasajero: ")
precio = float(input("Precio del boleto: "))
cantidad = int(input("Número de boletos: "))
total = cantidad * precio
print("Total a pagar: (round)", round(total, 2))
print(f"Total a pagar (f): ${total:.2f}")
