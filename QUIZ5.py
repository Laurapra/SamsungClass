#QUIZ 01 UNIDAD 05 BLOQUE 01
numero= int(input("Enter and Integer: "))
if numero %2 ==0:
    print(f"Is the integer odd: False")
else:
    print(f"Is the integer odd: True")

#QUIZ 02 UNIDAD 05 BLOQUE 01
numero=int(input("Enter and integer: "))
if(numero>0) & (numero<100):
    if numero %2 ==0:
        print("Is the input an even integer between 0 and 100? True")
    else:
        print("Is the input an even integer between o and 100? False")
else:
    print("Is the input an even integer between 0 and 100? False")

#QUIZ 01 UNIDAD 05 BLOQUE 02
num=int(input("Enter a 3 digit integer: "))
if num>=300 and num<=399:
    print("True")
else:
    print("False")

#QUIZ 02 UNIDAD 05 BLOQUE 02
num=int(input("Enter a 3 digit interger: "))
if num//5==0:
    print("True")
else:
    print("False")