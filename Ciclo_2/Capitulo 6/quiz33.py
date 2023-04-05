#programacion en parejas
def maze_solver(maze):
    n = len(maze)
    visited = [[False]*n for _ in range(n)]
    
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        if maze[x][y] == 1 or visited[x][y]:
            return False
        visited[x][y] = True
        if x == n-1 and y == n-1:
            return True
        if dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1):
            return True
        return False
    
    if dfs(0, 0):
        print("Se encontró un camino desde (0, 0) hasta (N-1, N-1)")
    else:
        print("No se encontró un camino válido")

# ejemplo de uso
maze = [
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 0]
]
maze_solver(maze)
