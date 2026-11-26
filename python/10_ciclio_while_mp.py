combustible = 2000
while combustible < 10000:
    print("Cargando combustible:", combustible, "litros")
    combustible += 2000

print("El avion tiene suficiente combustible")

asientos_disponibles = 3
while asientos_disponibles > 0:
    print("Asientos disponibles:", asientos_disponibles)
    asientos_disponibles -= 1

print("El vuelo esta completo")

print("Cuenta regresiva para el despegue")
segundos = 5
while segundos > 0:
    print(segundos)
    segundos -= 1
print("Despegue")
