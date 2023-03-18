#repaso de clase
#q1
def sum_recursive(n):
  if n == 1:
    return 1
  else:
    return n + sum_recursive(n-1)

#q2
def power_recursive(x, n):
  if n == 0:
    return 1
  else:
    return x * power_recursive(x, n-1)
result = power_recursive(2, 10)
print(result)

#programacion en parejas
def euler(n):
    if n == 0:
        return 1
    else:
        return euler(n-1) + 1/factorial(n)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = euler(20)
print(round(result, 5))
