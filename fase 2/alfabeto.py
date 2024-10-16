# 100%

K, N = map(int, input().split())

alfabeto_alienigena = set(input().strip())
mensagem = input().strip()

if all(c in alfabeto_alienigena for c in mensagem):
    print('S')
else:
    print('N')