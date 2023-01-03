#QUIZ 01 UNIDAD 04 BLOQUE 01
width, height= 30,60 #Aqui asigno valor de las variables de manera simultanea
area= width*height
print(f"El área del rectangulo es: {area}")

#QUIZ 02 UNIDAD  BLOQUE 01
base=int(input("Ingrese la base del triangulo: "))
altura=int(input("Ingrese la altura del triangulo: "))
print(f"La hipotenusa del triangulo es: {base**2+altura**2}")

#QUIZ 01 UNIDAD 04 BLOQUE 02
pi=3.141592
radio=float(input("Ingrese el número del radio: "))
circunferencia=2*pi*radio
area=pi*(radio**2)
print(f"La circunferencia del círculo es: {circunferencia}, el área del círuclo es: {area}")

#QUIZ 02 UNIDAD 04 BLOQUE 02
a= n= 2
print("--"*15)
print(f"  a    n    a**n ")
print("--"*15)
print(f"   {a}   {n}    {a**n}")
a+= 1
print(f"   {a}   {n}    {a**n}")
a+= 1
print(f"   {a}   {n}    {a**n}")
a+= 1
print(f"   {a}   {n}    {a**n}")
a+= 1
print(f"   {a}   {n}    {a**n}")