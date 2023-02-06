#codificacion en papel
#quiz01
estudiante_tup = (1, "Juan", 1234567890)

# Creación del diccionario
diccionario_estudiante = {estudiante_tup[0]: [estudiante_tup[1], estudiante_tup[2]]}

# Imprimir el diccionario
print(diccionario_estudiante)

#quiz02
estudiante_tup = (1001, "Juan", 123456789)

# Creación del diccionario a partir de la tupla
diccionario_estudiante = {estudiante_tup[0]: [estudiante_tup[1], estudiante_tup[2]]}

# Entrada del número de identificación del estudiante
num_id = int(input("Ingrese el número de identificación del estudiante: "))

# Verificación de existencia del estudiante
if num_id in diccionario_estudiante:
  nombre = diccionario_estudiante[num_id][0]
  telefono = diccionario_estudiante[num_id][1]
  print("Nombre:", nombre)
  print("Número de teléfono:", telefono)
else:
  print("El estudiante no se encuentra en el registro.")

#codificacion en parejas
estudiante_tupla = [('211101', 'David Doe', '010-123-1111'), ('211102', 'John Smith', '010-123-2222'), ('211103', 'Jane Carter', '010-123-3333')]
diccionario = {identificacion:nombre for identificacion, nombre, telefono in estudiante_tupla}
print(diccionario)
id_estudiante = input("Introduce el número de identificación del estudiante: ")
if id_estudiante in diccionario:
    nombre = diccionario[id_estudiante]
    for identificacion, nombre_estudiante, telefono in estudiante_tupla:
        if identificacion == id_estudiante:
            print(f"Número de identificación: {identificacion}\nNombre: {nombre}\nTeléfono: {telefono}")
            break
else:
    print("El número de identificación no se encuentra en la lista.")
