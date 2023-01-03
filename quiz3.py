#QUIZ1 DEL FINAL: n! se define como n (n-1) (n-2) (n-3) ... 2 1. Encuentre 5! y 10! usando enteros y el operador * e imprimalos como sigue.
"""
Ejemplo de resultado
Calcule el factorial.
5! = 120
Calcule el factorial.
10! = 3628800
"""
"""
n=int(input("N:"))
factorial=1
if n!=0:
    for i in range(1, n+1):
        factorial=factorial*i
print(f"El factorial de {n} es {factorial}")
"""
print("Calcule el factorial:")
factorial_5=5*(5-1)*(5-2)*(5-3)*(5-4)
factorial_10=10*(10-1)*(10-2)*(10-3)*(10-4)*(10-5)*(10-6)*(10-7)*(10-8)*(10-9)
print("5!= ",factorial_5)
print("Calcule el factorial: ")
print("10!= ",factorial_10,)

#QUIZ 01 UNIDAD 03
numero="50"
numero2=50
valor1=int(numero)+numero2
valor2=numero+str(numero2)
print(valor1)
print(valor2)