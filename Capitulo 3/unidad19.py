#quiz1
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []

for i in filter(lambda x: x % 2 == 0, n_list):
    even_list.append(i)
print(even_list)


#q2
n_list = [1,2,3,4,5,6,7,8,9,10]
even_list = list(filter(lambda x: x % 2 == 0, n_list))
print(even_list)

#q3
a_list = ['a', 'b', 'c', 'd']

def to_upper(char):
    return char.upper()

upper_a_list = list(map(to_upper, a_list))

print(upper_a_list) # ['A', 'B', 'C', 'D']

#Q4
from functools import reduce

# Uso reduce() y una expresión lambda para calcular la suma de enteros de 1 a 100
suma = reduce(lambda x, y: x + y, range(1, 101))

# Imprimo el resultado
print("La suma de 1 a 100 es", suma)

#programacion en parejas
# Definir la lista de puntajes de los estudiantes
scores = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]

# Obtener el número total de estudiantes
num_estudiantes = len(scores) // 3

# Crear una lista de sublistas que representen los puntajes de cada estudiante
estudiantes = [scores[i:i+3] for i in range(0, len(scores), 3)]

# Filtrar la lista de estudiantes para encontrar aquellos con puntajes válidos
estudiantes_validos = list(filter(lambda estudiante: all(score != 0 for score in estudiante), estudiantes))

# Obtener el número de estudiantes con puntajes válidos
num_estudiantes_validos = len(estudiantes_validos)

# Imprimir los resultados
print(f"el numero total de estudiantes es {num_estudiantes}")
print(f"el numero total de estudiantes validos es {num_estudiantes_validos}")
print(estudiantes_validos)