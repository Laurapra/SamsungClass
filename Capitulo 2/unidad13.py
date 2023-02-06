#quizz en papel 
#quiz01
lista_matriz = [[10, 20], [30, 40], [50, 60]]
valor = lista_matriz[1][0]
print(valor)

#quiz02
lista_2d = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for fila in lista_2d:
    for elemento in fila:
        print(elemento, end=" ")
    print()
#quiz en parejas
#quiz01
def cuadros(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if (i + j) % 2 == 0:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

n = int(input("Ingrese la dimensión de la matriz: "))
resultado = cuadros(n)
for fila in resultado:
    print(*fila)
