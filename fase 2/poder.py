# zerei :(

def dfs(i, j, grid, dp):
    if dp[i][j] != -1:
        return dp[i][j]

    poder_maximo = grid[i][j]
    
    direcao = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for di, dj in direcao:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[i][j] >= grid[ni][nj]:
            poder_maximo = max(poder_maximo, grid[i][j] + dfs(ni, nj, grid, dp))
    
    dp[i][j] = poder_maximo
    return poder_maximo

def jogo_do_poder(N, M, grid):
    dp = [[-1] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if dp[i][j] == -1:
                dfs(i, j, grid, dp)
    
    for row in dp:
        print(" ".join(map(str, row)))

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

jogo_do_poder(N, M, grid)