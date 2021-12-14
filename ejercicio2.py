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

turno = random.randrange(2)
while True:
    for i in range(3):
        print(tablero[i])
    print('\n')
    if turno == 0:
        if errorb1 == False and errorn1 == False:
            ejr2_func.movimiento(blanca1, 0, tablero)
            blanca1 = ejr2_func.cambio_ficha(blanca1, 0, tablero)
            errorn1 = ejr2_func.encerrada(negra1, 0, tablero)
        elif errorb2 == False and errorn2 == False:
            ejr2_func.movimiento(blanca2, 1, tablero)
            blanca2 = ejr2_func.cambio_ficha(blanca2, 1, tablero)
            errorn2 = ejr2_func.encerrada(negra2, 1, tablero)  
        elif errorb3 == False and errorn3 == False:
            ejr2_func.movimiento(blanca3, 2, tablero)
            blanca3 = ejr2_func.cambio_ficha(blanca3, 2, tablero)
            errorn3 = ejr2_func.encerrada(negra3, 2, tablero)
        else:
            print("Las blancas estan encerradas, ganan las negras")
            break
        turno = 1
    elif turno == 1:
        if errorb1 == False and errorn1 == False:
            ejr2_func.movimiento(negra1, 0, tablero)
            negra1 = ejr2_func.cambio_ficha(negra1, 0, tablero)
            errorb1 = ejr2_func.encerrada(blanca1, 0, tablero)
        elif errorb2 == False and errorn2 == False:
            ejr2_func.movimiento(negra2, 1, tablero)
            negra2 = ejr2_func.cambio_ficha(negra2, 1, tablero)
            errorb2 = ejr2_func.encerrada(blanca2, 1, tablero) 
        elif errorb3 == False and errorn3 == False:
            ejr2_func.movimiento(negra3, 2, tablero)
            negra3 = ejr2_func.cambio_ficha(negra3, 2, tablero)
            errorb3 = ejr2_func.encerrada(blanca3, 2, tablero)
        else:
            print("Las negras estan encerradas, ganan las blancas")
            break
        turno = 0