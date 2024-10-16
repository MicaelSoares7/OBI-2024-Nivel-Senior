N, K = map(int, input().split())
lista = list(map(int, input().split()))

lista.sort()
C = lista[N-K]

print(C)