"""
Manejo de Cadena de Caracteres
"""
nombre1 = "Qui-Gon Jinn"
print(f"Jedi 1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")
nombre2 = "Obiwan Kenobi"
print(f"Jedi 2: {type(nombre2)}")

print("Convertir Mayusculas y minusculas")
mensaje = "La federación invade el Planeta Naboo"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print("Mensaje Original", mensaje)
print("Mensaje en Mayuscula", mensaje_mayuscula)
print("Mensaje en Minuscula", mensaje_minuscula)

print("Reemplazo de substring")
mensaje = "La nave viajará a Tatooine"
nuevo_mensaje = mensaje.replace("Tatooine", "Coruscant")
print("Mensaje Original", mensaje)
print("Mensaje Reemplazado", nuevo_mensaje)
