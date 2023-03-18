#Q1
def my_greet():
    print("Bienvenido")

my_greet()
my_greet()

#Q2
def max2(m, n):
    return max(m, n)

def min2(m, n):
    return min(m, n)

max_result = max2(100, 200)
min_result = min2(100, 200)

print("El número mayor es:", max_result)
print("El número menor es:", min_result)

#Q3
def mile2km(ml):
    return ml * 1.61

for miles in range(1, 6):
    kilometers = mile2km(miles)
    print(miles, "millas son", kilometers, "kilómetros")

#Q4
def cel2fah(cel):
    return cel * (9/5) + 32

for cel in range(10, 51, 10):
    fah = cel2fah(cel)
    print(cel, "grados Celsius son", fah, "grados Fahrenheit")


#Quiz en parejas
def mean3(a, b, c):
    return (a + b + c) / 3

def max3(a, b, c):
    return max(a, b, c)

def min3(a, b, c):
    return min(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter three number: "))

average = mean3(a, b, c)
maximum = max3(a, b, c)
minimum = min3(a, b, c)

print( a, b, c)
print("The average value of 9,2,6 is: ", average)
print("The maximun value of: ", maximum)
print("The minimun value of: ", minimum)