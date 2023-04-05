#seccion quiz 
#quiz1
def find_heavy_coin(coins):
    # Divide las monedas en tres grupos de igual tamaño
    group_size = len(coins) // 3
    group_a, group_b, group_c = coins[:group_size], coins[group_size:2*group_size], coins[2*group_size:]
    
    # Pesa los grupos A y B en la balanza
    weight_a, weight_b = sum(group_a), sum(group_b)
    
    # Si los dos grupos tienen el mismo peso, entonces la moneda más pesada debe estar en el grupo C
    if weight_a == weight_b:
        return group_c[0]
    # Si no, divide el grupo más pesado en tres grupos de igual tamaño
    elif weight_a > weight_b:
        group_d, group_e, group_f = group_a[:group_size], group_a[group_size:2*group_size], group_a[2*group_size:]
    else:
        group_d, group_e, group_f = group_b[:group_size], group_b[group_size:2*group_size], group_b[2*group_size:]
    
    # Pesa los grupos D y E en la balanza
    weight_d, weight_e = sum(group_d), sum(group_e)
    
    # Si los dos grupos tienen el mismo peso, entonces la moneda más pesada debe estar en el grupo F
    if weight_d == weight_e:
        return group_f[0]
    # Si no, pese dos de las monedas del grupo más pesado
    elif weight_d > weight_e:
        weight = coins.index(group_d[0])
        return group_d[0] if weight_d - weight == 2 else group_d[1]
    else:
        weight = coins.index(group_e[0])
        return group_e[0] if weight_e - weight == 2 else group_e[1]
coins = [1, 2, 3, 4, 5, 6, 7, 8]
heavy_coin = find_heavy_coin(coins)
print("La moneda más pesada es la número:", heavy_coin)

#quiz2
def find_heavy_coin(coins):
    # Dividimos las monedas en tres grupos de tres monedas cada uno
    group1 = coins[:3]
    group2 = coins[3:6]
    group3 = coins[6:]
    
    # Pesamos dos de los grupos en la balanza
    if sum(group1) > sum(group2):
        # La moneda pesada debe estar en el grupo 1
        if group1[0] > group1[1]:
            return 1
        elif group1[1] > group1[2]:
            return 2
        else:
            return 3
    elif sum(group1) < sum(group2):
        # La moneda pesada debe estar en el grupo 2
        if group2[0] > group2[1]:
            return 4
        elif group2[1] > group2[2]:
            return 5
        else:
            return 6
    else:
        # La moneda pesada debe estar en el grupo 3
        if group3[0] > group3[1]:
            return 7
        else:
            return 8
#PROGRAMACION EN PAREJAS
def tromino(board, n, x_missing, y_missing, x_start, y_start):
    if n == 1:
        return
    
    x_center = x_start + n//2
    y_center = y_start + n//2
    
    # Determine in which quadrant the missing square is located
    if x_missing < x_center and y_missing < y_center:
        quadrant = 1
    elif x_missing < x_center and y_missing >= y_center:
        quadrant = 2
    elif x_missing >= x_center and y_missing < y_center:
        quadrant = 3
    else:
        quadrant = 4
    
    # Place the L-shaped tromino in the corresponding quadrant
    for i in range(x_start, x_start + n):
        for j in range(y_start, y_start + n):
            if i == x_center and j == y_center:
                continue
            if quadrant == 1 and i == x_center-1 and j == y_center:
                continue
            if quadrant == 2 and i == x_center and j == y_center:
                continue
            if quadrant == 3 and i == x_center and j == y_center-1:
                continue
            if quadrant == 4 and i == x_center-1 and j == y_center-1:
                continue
            
            board[i][j] = 1
    
    # Recursively solve for each sub-quadrant
    tromino(board, n//2, x_center-1, y_center, x_start, y_start)
    tromino(board, n//2, x_center, y_center, x_start, y_center)
    tromino(board, n//2, x_center, y_center-1, x_start + n//2, y_start)
    tromino(board, n//2, x_center-1, y_center-1, x_start + n//2, y_start + n//2)


# Ejemplo de uso
n = 4
x_missing = 2
y_missing = 2

# Inicializar el tablero
board = [[0]*n for _ in range(n)]
board[x_missing][y_missing] = "X"

# Resolver el problema del Tromino
tromino(board, n, x_missing, y_missing, 0, 0)

# Imprimir el tablero resultante
for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()
