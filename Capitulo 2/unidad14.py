#codificacion en papel
#quiz01
persona_diccionario = {'Apellido': 'Doe', 'Nombre': 'John', 'Teléfono': '555-555-1212', 'Correo electrónico': 'johndoe@email.com'}

for clave, valor in persona_diccionario.items():
    print(clave + ": " + valor)
#quiz02
items = {"Café": 7, "Lápiz": 3, "Vaso de papel": 2, "Leche": 1, "Coca-Cola": 4, "Libro": 5}

def consultar_inventario(artículo):
    if artículo in items:
        return "El inventario de " + artículo + " es de " + str(items[artículo])
    else:
        return "El artículo no se encuentra en el inventario."

artículo = input("Ingrese el nombre del artículo: ")
print(consultar_inventario(artículo))
#quiz en parejas
items = {"Café": 7, "Puma": 3, "Vaso de papel": 2, "Leche": 1, "Coca-Cola": 4, "Libro": 5}

while True:
    print("Seleccione el menú 1)Comprobar existencias 2)Almacenamiento 3)Liberación 4)Salir: ", end="")
    opcion = int(input().strip())

    if opcion == 1:
        print("[Comprobar existencias] Introduzca el artículo: ", end="")
        producto = input().strip()
        if producto in items:
            print("Existencias: ", items[producto])
        else:
            print("Artículo no encontrado")
    elif opcion == 2:
        print("[Almacenamiento] Introduzca el artículo y la cantidad: ", end="")
        entrada = input().strip().split()
        producto = entrada[0]
        cantidad = int(entrada[1])
        items[producto] = cantidad
    elif opcion == 3:
        print("[Liberación] Introduzca el artículo y la cantidad: ", end="")
        entrada = input().strip().split()
        producto = entrada[0]
        cantidad = int(entrada[1])
        if producto in items:
            items[producto] -= cantidad
        else:
            print("Artículo no encontrado")
    elif opcion == 4:
        break
    else:
        print("Opción inválida")

print("Ha salido del programa.")
