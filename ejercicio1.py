vocales ='aeiou'
while True:
    palabra = input("Escriba una palabra: ")
    letras = palabra.split()
    if len(letras) == 1:
        break
    else:
        print("Eso no es solo una palabra")
        pass

posicion = -1
puntos_kevin = 0
puntos_stuart = 0
for letras in palabra:
    if vocales.__contains__(letras):
        if palabra.count(letras) > 1:
            posicion = palabra.index(letras, posicion + 1)
            puntos_kevin = puntos_kevin + len(palabra) - palabra.index(letras, posicion)
        else:
            puntos_kevin = puntos_kevin + len(palabra) - palabra.index(letras)
    else:
        if palabra.count(letras) > 1:
            posicion = palabra.index(letras, posicion + 1)
            puntos_stuart = puntos_stuart + len(palabra) - palabra.index(letras, posicion)
        else:
            puntos_stuart = puntos_stuart + len(palabra) - palabra.index(letras)

if puntos_stuart > puntos_kevin:
    print("El ganador es Stuart, ha obtenido ", puntos_stuart, " puntos")
elif puntos_kevin > puntos_stuart:
    print("El ganador es Kevin, ha obtenido ", puntos_kevin, " puntos")
else:
    print("Draw")