#quiz02
ventas = [100, 90, 95, 85, 80, 75, 70, 60, 55, 50]
reducciones = 0

for i in range(1, len(ventas)):
    if ventas[i] < ventas[i-1]:
        reducciones += 1

print("El número de días con reducciones en ventas es:", reducciones)

#quizes en parejas
#quiz01
tupla = (1, 2, 5, 4, 3, 2, 1, 9, 9, 3, 7, 3, 9)

dic = {}
for i in tupla:
    dic[i] = dic.get(i, 0) + 1

valor_maximo = max(dic.values())
elementos_frecuentes = [k for k, v in dic.items() if v == valor_maximo]

if len(elementos_frecuentes) == 1:
    resultado = elementos_frecuentes[0]
else:
    resultado = max(elementos_frecuentes)

print("Elemento con el máximo número de ocurrencias:", resultado)


#quiz02
lista = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
lista_limpia = [i for i in lista if i and i != () and i != [] and i != '']
print("Lista obtenida:", lista_limpia)
