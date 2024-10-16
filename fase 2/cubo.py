# 100%

N = int(input())

if N > 2:
    zero_faces = (N-2)**3
else:
    zero_faces = 0

if N > 2:
    uma_face = 6 * (N-2)**2
else:
    uma_face = 0


if N > 2:
    duas_faces = 12 * (N-2)
else:
    duas_faces = 0

tres_faces = 8

print(zero_faces)
print(uma_face)
print(duas_faces)
print(tres_faces)
