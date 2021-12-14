def encerrada(FILA, COLUMNA, TABLERO):
    if FILA == 0 and TABLERO[FILA + 1][COLUMNA] != ' ':
        error = True
    elif FILA == 2 and TABLERO[FILA - 1][COLUMNA] != ' ':
        error = True
    else:
        error = False
    return error

def movimiento(FILA, COLUMNA, TABLERO):
    if FILA == 0:
        TABLERO[1][COLUMNA] = TABLERO[0][COLUMNA]
        TABLERO[0][COLUMNA] = ' '
    elif FILA == 1:
        if TABLERO[2][COLUMNA] == ' ':
            TABLERO[2][COLUMNA] = TABLERO[1][COLUMNA]
            TABLERO[1][COLUMNA] = ' '
        else:
            TABLERO[0][COLUMNA] = TABLERO[1][COLUMNA]
            TABLERO[1][COLUMNA] = ' '
    elif FILA == 2:
        TABLERO[1][COLUMNA] = TABLERO[2][COLUMNA]
        TABLERO[2][COLUMNA] = ' '