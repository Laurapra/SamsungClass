#sesion quiz
#quiz1

def coin_change(coins, amount):
    if amount == 0:
        return 0
    if min(coins) > amount:
        return float('inf')
    min_coins = float('inf')
    for coin in coins:
        if amount >= coin:
            num_coins = coin_change(coins, amount - coin)
            if num_coins + 1 < min_coins:
                min_coins = num_coins + 1
    return min_coins

coins = [400, 100, 50, 10]
amount = 800

num_coins = coin_change(coins, amount)
print("El número mínimo de monedas necesarias para dar cambio de", amount, "wones es:", num_coins)


#programacion en parejas
#quiz1
denominations = [500, 100, 50, 10, 1] # denominaciones de las monedas disponibles
change = 710 # cantidad de cambio a distribuir

coins = [] # lista para almacenar las monedas necesarias
for d in denominations:
    while change >= d:
        coins.append(d)
        change -= d

print("Para dar un cambio de 710 won, necesitas las siguientes monedas:", coins)

#quiz2
def min_coin_change(coins, change):
    # Crear una matriz de tamaño (change+1) x (len(coins)+1)
    dp = [[float('inf')]*(len(coins)+1) for _ in range(change+1)]
    
    # Inicializar la primera columna como 0
    for i in range(change+1):
        dp[i][0] = 0
        
    # Completar la matriz
    for i in range(1, change+1):
        for j in range(1, len(coins)+1):
            if coins[j-1] <= i:
                dp[i][j] = min(dp[i][j-1], 1 + dp[i-coins[j-1]][j])
            else:
                dp[i][j] = dp[i][j-1]
    
    # Devolver la solución
    return dp[change][len(coins)]

# Ejemplo de uso
coins = [1, 5, 10, 25]
change = 48
min_coins = min_coin_change(coins, change)
print("Para dar un cambio de", change, "centavos con las monedas", coins, "necesitas al menos", min_coins, "monedas.")
