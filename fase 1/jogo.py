def verificar(celula, qtdV):
  if celula == "0":
    if qtdV == 3: 
      return "1"
    else:
      return "0"
  elif celula == "1":
    if qtdV > 3:
      return "0"
    elif qtdV < 2:
      return "0"
    else:
      return "1"

N, Q = map(int, input().split())
matriz = []

for _ in range(N):
  linha = input()
  matriz.append(linha)

vetorNovo = ""
for _ in range(Q):
  for i in range(N):
    res = ""
    for j in range(N):
      cont = 0
      if i == 0: 
        if j == 0: 
          if matriz[i][j+1] == "1": 
            cont += 1
          if matriz[i+1][j] == "1": 
            cont += 1
          if matriz[i+1][j+1] == "1": 
            cont += 1
          
          res += verificar(matriz[i][j], cont)
        elif j == N-1: 
          if matriz[i][j-1] == "1": 
            cont += 1
          if matriz[i+1][j] == "1": 
            cont += 1
          if matriz[i+1][j-1] == "1": 
            cont += 1
          
          res += verificar(matriz[i][j], cont)
        else:
          if matriz[i][j+1] == "1": 
            cont += 1
          if matriz[i][j-1] == "1": 
            cont += 1
          if matriz[i+1][j] == "1": 
            cont += 1
          if matriz[i+1][j+1] == "1": 
            cont += 1
          if matriz[i+1][j-1] == "1": 
            cont += 1
          
          res += verificar(matriz[i][j], cont)
      elif i == N-1:
        if j == 0:
          if matriz[i][j+1] == "1": 
            cont += 1
          if matriz[i-1][j] == "1": 
            cont += 1
          if matriz[i-1][j+1] == "1": 
            cont += 1

          res += verificar(matriz[i][j], cont)
        elif j == N-1:
          if matriz[i][j-1] == "1": 
            cont += 1
          if matriz[i-1][j] == "1": 
            cont += 1
          if matriz[i-1][j-1] == "1": 
            cont += 1

          res += verificar(matriz[i][j], cont)
        else:
          if matriz[i][j+1] == "1": 
            cont += 1
          if matriz[i][j-1] == "1": 
            cont += 1
          if matriz[i-1][j] == "1": 
            cont += 1
          if matriz[i-1][j+1] == "1": 
            cont += 1
          if matriz[i-1][j-1] == "1": 
            cont += 1
          
          res += verificar(matriz[i][j], cont)
      else:
        if j == 0:
          if matriz[i-1][j] == "1": 
            cont += 1
          if matriz[i][j+1] == "1": 
            cont += 1
          if matriz[i+1][j] == "1": 
            cont += 1
          if matriz[i+1][j+1] == "1": 
            cont += 1
          if matriz[i-1][j+1] == "1": 
            cont += 1
        
          res += verificar(matriz[i][j], cont)
        elif j == N-1:
          if matriz[i+1][j] == "1": 
            cont += 1
          if matriz[i-1][j] == "1": 
            cont += 1
          if matriz[i][j-1] == "1": 
            cont += 1
          if matriz[i-1][j-1] == "1": 
            cont += 1
          if matriz[i+1][j-1] == "1": 
            cont += 1
        
          res += verificar(matriz[i][j], cont)
        else:
          if matriz[i][j-1] == "1": 
            cont += 1
          if matriz[i][j+1] == "1": 
            cont += 1
          if matriz[i-1][j] == "1": 
            cont += 1
          if matriz[i-1][j+1] == "1": 
            cont += 1
          if matriz[i-1][j-1] == "1": 
            cont += 1
          if matriz[i+1][j] == "1": 
            cont += 1
          if matriz[i+1][j+1] == "1": 
            cont += 1
          if matriz[i+1][j-1] == "1": 
            cont += 1

          res += verificar(matriz[i][j], cont)
    matriz[i] = res

for linha in matriz:
  print(linha)