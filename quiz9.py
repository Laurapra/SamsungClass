#QUIZ 02 UNIDAD 09 BLOQUE 01
"""
a=0
e=0
while(a<=10):
    a+=1
    for e in range(1,10,1):
        print('{} * {} ={:2d}'.format(a,e,a*e))"""
#QUIZ 02 UNIDAD 09 BLOQUE 02
import random
numero_oculto= random.randint(1,100)
num_adiv= -1

while numero_oculto != num_adiv:
    num_adiv=int(input("Guess a number between 1 to 100: "))
    if numero_oculto>num_adiv:
        print("Lower!")
    else:
        print("Higher!")
print(f"Congratulations. Total try:{num_adiv}")