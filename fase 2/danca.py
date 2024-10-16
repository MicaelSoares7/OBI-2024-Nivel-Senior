# 100%

def resolver_danca_de_formatura(N, M, P, operacoes):

    linha_map = list(range(N))
    coluna_map = list(range(M))

    for op in operacoes:
        tipo, a, b = op
        a -= 1 
        b -= 1  
        if tipo == 'L':
            linha_map[a], linha_map[b] = linha_map[b], linha_map[a]
        elif tipo == 'C':
            coluna_map[a], coluna_map[b] = coluna_map[b], coluna_map[a]

    pista_final = []
    for i in range(N):
        linha_atual = []
        for j in range(M):
            aluno_num = linha_map[i] * M + coluna_map[j] + 1
            linha_atual.append(aluno_num)
        pista_final.append(linha_atual)

    return pista_final

N, M, P = map(int, input().split())
operacoes = []
for _ in range(P):
    entrada = input().split()
    tipo = entrada[0]
    a, b = int(entrada[1]), int(entrada[2])
    operacoes.append((tipo, a, b))

resultado = resolver_danca_de_formatura(N, M, P, operacoes)


for linha in resultado:
    print(" ".join(map(str, linha)))
