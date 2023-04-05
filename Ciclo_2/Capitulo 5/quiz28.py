#quiz01
"""
En el proceso de ordenamiento por mezcla, la función ordenamiento_fusion2() se ejecuta recursivamente para dividir la lista original en sublistas más pequeñas, y luego se fusionan las sublistas ordenadas en la lista original. Cada vez que la función se ejecuta, se divide la lista por la mitad, por lo que se ejecutará log2(n) veces, donde n es la longitud de la lista. Después de la fase de división, se ejecuta la fase de combinación, que une las sublistas en una lista ordenada. Esto se hace para cada nivel de recursión, lo que significa que se ejecuta la fase de combinación para cada nivel de recursión. Por lo tanto, la función ordenamiento_fusion2() se ejecutará un total de 4 veces para la primera lista S = [6, 2, 11, 7, 5, 4, 8, 16, 10, 3] y se ejecutará un total de 4 veces también para la segunda lista S = [6, 2, 11, 7, 5, 4, 8, 16, 10, 3, 1, 12, 9]. Por lo tanto, la función ordenamiento_fusion2() se ejecutó 8 veces en total.
"""

#programacion en parejas
def merge_sorted_lists(list1, list2):
    """
    Función que mezcla dos listas ordenadas en una sola lista ordenada
    """
    i, j = 0, 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list += list1[i:]
    merged_list += list2[j:]
    return merged_list

def merge_multiple_lists(lists):
    """
    Función que mezcla múltiples listas ordenadas en una sola lista ordenada
    """
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    left = merge_multiple_lists(lists[:mid])
    right = merge_multiple_lists(lists[mid:])
    return merge_sorted_lists(left, right)
N = int(input("Ingrese el número de listas: "))
lista_de_numeros = []
for i in range(N):
    numeros = list(map(int, input("Ingrese una lista de números: ").split()))
    numeros.sort()  # aseguramos que las listas estén ordenadas
    lista_de_numeros.append(numeros)

ordenada = merge_multiple_lists(lista_de_numeros)
print("Lista fusionada: ", ordenada)
