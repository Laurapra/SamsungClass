#QUIZ 01 UNIDAD 07 BLOQUE 01:
"""
letra=input("Enter the alphabet: ")
if letra =="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print(f" {letra} is a vowel")
else:
    print(f"{letra} is a consonant")
"""
#QUIZ 02 UNIDAD 07 BLOQUE 01:
"""
a,b=input("Ingrese el valor de a y b: ").split()
a=int(a)
b=int(b)
if a%b==0:
    print(f"{a} es multiplo de {b}")
else:
    print(f"{a} no es multiplo de {b}")
"""
#QUIZ 01 UNIDAD 07 BLOQUE 02:
print("Con este programa harás operaciones matemáticas\n Elige 1 para sumar\n elige 2 para restar\n elige 3 para dividir\n elige 4 para multiplicar")
eleccion= input("Selecciona tu opción (1,2,3,4): ")
if eleccion =="1":
    print ("Elegiste sumar")
elif eleccion =="2":
    print("Elegiste restar")
elif eleccion =="3":
    print("Elegiste dividir")
elif eleccion=="4":
    print("Elegiste multiplicar")
else:
    print("Elegiste una opción incorrecta")

a=int(input("Digita tu primer valor: "))
b=int(input("Digita tu segundo valor: "))
sumar= a+b
restar= a-b
dividir= a/b
multiplicar= a*b
if eleccion =="1": sumar: print(f"El resultado de sumar {a} y {b} es {sumar}")
elif eleccion=="2": restar: print(f"El resultado de {a} y {b} es {restar}")
elif eleccion=="3": dividir: print(f"El resultado de {a} y {b} es {dividir}")
elif eleccion=="4": multiplicar: print(f"El resultado de {a} y {b} es {multiplicar}")