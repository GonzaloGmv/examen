def encerrada(FILA, COLUMNA, TABLERO):
    if FILA == 0 and TABLERO[FILA + 1][COLUMNA] != ' ':
        error = True
    elif FILA == 2 and TABLERO[FILA - 1][COLUMNA] != ' ':
        error = True
    else:
        error = False
    return error