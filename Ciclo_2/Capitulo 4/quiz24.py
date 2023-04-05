#programacion en parejas
def word_count(S, x):
    count = 0
    for word in S:
        if word == x:
            count += 1
    return count

s = list(input('Ingrese una oración: ').split())
x = input('Ingrese la palabra a buscar: ')
count = word_count(s, x)
print(f'En la lista S, la palabra "{x}" aparece {count} veces.')
