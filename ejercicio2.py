import random, ejr2_func

blancas = chr(0x2656)
negras = chr(0x265C)

while True:

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

    errorb1 = ejr2_func.encerrada(blanca1, 0, tablero)
    errorb2 = ejr2_func.encerrada(blanca2, 1, tablero)
    errorb3 = ejr2_func.encerrada(blanca3, 2, tablero)
    errorn1 = ejr2_func.encerrada(negra1, 0, tablero)
    errorn2 = ejr2_func.encerrada(negra2, 1, tablero)
    errorn3 = ejr2_func.encerrada(negra3, 2, tablero)

    if errorb1 == True and errorb2 == True and errorb3 == True:
        pass
    elif errorn1 == True and errorn2 == True and errorn3 == True:
        pass
    else:
        break

for i in range(3):
    print(tablero[i])
