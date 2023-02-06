# codificacion en papel
# quiz01
st = ['apple', 'mango', 'banana']
s1 = set(st)
print("s1 =", s1)

# quiz02
s1 | s2(union of sets) - Resultado: {10, 20, 30, 40, 50, 60, 70}
s1 & s2(intersection of sets) - Resultado: {30, 40}
s1 - s2(difference of sets) - Resultado: {10, 20}
s1 ^ s2(symmetric difference of sets) - Resultado: {10, 20, 50, 60, 70}
s1.issubset(s2) ( is s1 a subset of s2) - Resultado: False
s1.issuperset(s2) ( is s1 a superset of s2) - Resultado: False

# qiz en parejas
mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]


def find_tuple(mylist, a, b):
    found = False
    for i, t in enumerate(mylist):
        if t == (a, b):
            print("Hay un elemento ({}, {}) en el {}º lugar".format(a, b, i + 1))
            found = True
        elif t == (b, a):
            print("No hay ({}, {}), pero sí hay ({}, {}) en el {}º lugar".format(
                a, b, b, a, i + 1))
            found = True
    if not found:
        print("No hay tal elemento")


a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
find_tuple(mylist, a, b)
