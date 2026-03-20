# Sistema de inventario básico
from funciones import *

# Lista para guardar los productos
inventario = []


# Menú principal
opcion = ""

while opcion != "4":
    print("\n1. Agregar producto")

    print("2. Mostrar inventario")

    print("3. Calcular estadísticas")

    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_producto(inventario)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        calcular_estadisticas(inventario)

    elif opcion == "4":
        print("Fin del programa")

    else:
        print("Opción inválida")

