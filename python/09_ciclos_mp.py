print("Pasajeros que abordan:")
for numero in range(1, 6):
    print("Pasajero", numero, "abordando el vuelo")

print("Tabla de asientos")
for fila in range(1, 4):
    for asiento in range(1, 5):
        print(f"Fila {fila}, asiento {asiento}")

vuelos = [
    {"codigo": "AV101", "destino": "Bogota", "estado": "A tiempo"},
    {"codigo": "AV202", "destino": "Lima", "estado": "En embarque"},
    {"codigo": "AV303", "destino": "Quito", "estado": "A tiempo"},
]

print("Lista de vuelos")
for vuelo in vuelos:
    print(f"{vuelo['codigo']} - {vuelo['destino']} - {vuelo['estado']}")

ciudades = ["Bogota", "Lima", "Quito"]
for ciudad in ciudades:
    print("Destino disponible:", ciudad)

maletas_por_pasajero = {"Ana": 1, "Luis": 3, "Sofia": 2}
for pasajero, maletas in maletas_por_pasajero.items():
    if maletas <= 2:
        print(pasajero, "puede continuar al control de seguridad")
    else:
        print(pasajero, "debe revisar el limite de equipaje")
