#QUIZ 01 UNIDAD 08 BLOQUE 01
"""
bts=["V", "J-Hope", "RM", "Jungkook", "Jin", "Jimin", "Suga"]
for i in bts:
    print(i)
"""
#QUIZ 02 UNIDAD 08 BLOQUE 01
"""
suma=0
for i in range(1,101):
    suma=suma+i
print(f"Sum of integers from 1 to 100: {suma}")"""
#QUIZ 03 UNIDAD 08 BLOQUE 01
"""
suma=0
for i in range (0,101,2):
    suma=suma+i
print(f"Sum of even numbers from 1 to 100: {suma}")"""
#QUIZ 01 UNIDAD 08 BLOQUE 02
n=int(input("Ingrese el valor de n: "))
for i in range(1,n*n+1,n):
    if int(((i-1)/n))%2==0:
        for j in range(i,i+n):
            print(j, end=' ')
    else:
        for j in range(i+n-1,i-1,-1):
            print(j,end=' ')
    print(' ')