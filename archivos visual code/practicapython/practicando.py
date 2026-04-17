palabra =input('ingresa una palabra: ')
contador = 0
for letra in palabra:
    if letra == 'a':
        contador += 1
        print(contador, end=' ')