lista_primos= [2,3,5,7]
print(f"El primer elemento primo de \n{lista_primos[0]}")
#quiz02
lista_primos = [2, 3, 5, 7]
print(f"Números primos: \n{lista_primos}")
lista_primos.append(11)
print(f"Números primos despues de la adición: \n{lista_primos}")
#quiz03
lista1 = [3, 5, 7]
lista2 = [2, 3, 4, 5, 6]
for x in lista1:
    for y in lista2:
        (f"{x} * {y} = {x*y}")

#quiz 01
def get_shortest_string(s_list):
  shortest = s_list[0]
  for s in s_list[1:]:
    if len(s) < len(shortest):
      shortest = s
  return shortest
#quiz02
def shortest_string(s_list):
    shortest = s_list[0]
    for s in s_list:
        if len(s) < len(shortest):
            shortest = s
    return shortest
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
print(shortest_string(s_list))  # Output: 'opq'

#programacion en parejas
#quiz01
s_lista = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

def cadena_mas_corta(s_lista):
    short_string = s_lista[0]
    for string in s_lista:
        if len(string) < len(short_string):
            short_string = string
            return short_string

result = cadena_mas_corta(s_lista)
print("La cadena más corta es:")
print(result)

#quiz02
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

def cadena_mas_larga(s_list):
    long_string = s_list[0]
    for string in s_list:
        if len(string) > len(long_string):
            long_string = string
            return long_string

result = cadena_mas_larga(s_list)
print("La cadena más larga es:")
print(result)
#quiz 03
def print_shortest_strings(s_list):
    s_list.sort(key=len) # Ordenamos la lista de cadenas por longitud
    shortest_strings = [s for s in s_list if len(s) == len(s_list[0])] # Obtenemos las cadenas más cortas
    for s in shortest_strings[:3]: # Imprimimos las tres cadenas más cortas
        print(s)

s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
print_shortest_strings(s_list)
