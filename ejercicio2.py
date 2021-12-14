import random

blancas = chr(0x2656)
negras = chr(0x265C)

tablero = []
for i in range(3):
    tablero.append([' '] * 3)

blanca1 = random.randrange(3)
blanca2 = random.randrange(3)
blanca3 = random.randrange(3)
while True:
    negra1 = random.randrange(3)
    if negra1 != blanca1:
        break
while True:
    negra2 = random.randrange(3)
    if negra2 != blanca2:
        break
while True:
    negra3 = random.randrange(3)
    if negra3 != blanca3:
        break

tablero[blanca1][0] = blancas
tablero[blanca2][1] = blancas
tablero[blanca3][2] = blancas
tablero[negra1][0] = negras
tablero[negra2][1] = negras
tablero[negra3][2] = negras

for i in range(3):
    print(tablero[i])