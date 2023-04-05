#quiz01
"""
El ordenamiento de burbujas compara cada elemento de la lista con el siguiente y los intercambia si no están en el orden correcto. Por lo tanto, la cantidad de intercambios es igual al número de pares de elementos que necesitan ser intercambiados para ordenar la lista.

En este caso, las operaciones de intercambio que se han ejecutado son:

1 intercambio entre 50 y 30
1 intercambio entre 40 y 10
1 intercambio entre 30 y 10
1 intercambio entre 20 y 10
En total, se han ejecutado 4 operaciones de intercambio.
"""
#quiz02
"""
En el proceso de ordenamiento por inserción se realizan las siguientes comparaciones:

Para el segundo elemento se realiza 1 comparación.
Para el tercer elemento se realizan 2 comparaciones.
Para el cuarto elemento se realizan 3 comparaciones.
Para el quinto elemento se realizan 4 comparaciones.
Por lo tanto, en total se realizan 1+2+3+4=10 comparaciones en el proceso de ordenamiento por inserción.
"""
#programacion en parejas
#quiz01
def es_anagrama(palabra1, palabra2):
    # Convertir a minúsculas y eliminar espacios
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    # Creao un diccionario vacío para almacenar la frecuencia de cada letra en la primera palabra
    frecuencias = {}

    # Recorro cada letra en la primera palabra y aumentar su frecuencia en el diccionario
    for letra in palabra1:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1

    # Recorro cada letra en la segunda palabra y disminuir su frecuencia en el diccionario
    for letra in palabra2:
        if letra in frecuencias:
            frecuencias[letra] -= 1
        else:
            return False

    # Compruebo si todas las frecuencias son cero
    for letra in frecuencias:
        if frecuencias[letra] != 0:
            return False

    return True
print(es_anagrama("ESCUCHAR", "SILENCIO"))  # True
print(es_anagrama("Tom Marvolo Riddle", "I am Lord Voldemort"))  # True
print(es_anagrama("Python", "Java"))  # False

#quiz02
def es_anagrama(palabra1, palabra2):
    # Convertir ambas palabras a minúsculas y quitar espacios en blanco
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    
    # Verificar si ambas palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False
    
    # Ordenar las letras de ambas palabras y comparar si son iguales
    return sorted(palabra1) == sorted(palabra2)
def es_anagrama(palabra1, palabra2):
    # Convertir ambas palabras a minúsculas y quitar espacios en blanco
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    
    # Verificar si ambas palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False
    
    # Ordenar las letras de ambas palabras utilizando selection_sort2()
    lista1 = list(palabra1)
    lista2 = list(palabra2)
    selection_sort2(lista1)
    selection_sort2(lista2)
    
    # Comparar si las listas ordenadas son iguales
    return lista1 == lista2
    
def selection_sort2(lista):
    n = len(lista)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
