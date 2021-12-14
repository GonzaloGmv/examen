vocales ='aeiou'
while True:
    palabra = input("Escriba una palabra: ")
    letras = palabra.split()
    if len(letras) == 1:
        break
    else:
        print("Eso no es solo una palabra")
        pass
