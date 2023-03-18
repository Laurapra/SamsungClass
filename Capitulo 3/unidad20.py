#q1
# Defino la función greetings
def greetings():
    # Defino la función say_hi
    def say_hi():
        print('hello')
    
    # Llamo la función say_hi
    say_hi()

# Llamo la función greetings e imprime 'hello'
greetings()


#q2
# Defino la función calc
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a*x + b
    return mul_add

# Asigno la función calc a la variable num
num = calc()

# Llamo a num(3) y muestra el resultado
print(num(3))

#q3
# Defino la función calc con la expresión lambda
def calc():
    a = 3
    b = 5
    mul_add = lambda x: a*x + b
    return mul_add

# Asigno la función calc a la variable num
num = calc()

# Llamo a num(3) y muestra el resultado
print(num(3))

#programacion en parejas
def func1(a):
    def func2(x):
        return x % 5 == 0

    def func3(x):
        return x % 7 == 0

    result = []
    for x in a:
        if func2(x) or func3(x):
            result.append(x)
    
    return sorted(result)

lst = list(range(1, 101))
result = func1(lst)

print(result)
