texto = input("Ingrese un texto: ")
texto_invertido = texto[::-1] # El slicing con un paso de -1 invierte el texto
if texto == texto_invertido:
    print('bingo', texto, 'es un palindromo')
    
else:
    print('texto invertido:', texto_invertido)
    

