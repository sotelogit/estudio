# calculadora suma y resta
print('presione: 1 para suma,o 2 para resta')
opcion = float(input('ingrese una opcion: '))
 # primero habia puesto num1 y num2 arriba del primer if
 # funcionaba pero el else se ejecutaba despues de pedir los numeros.
if opcion == 1:
    num1 = float(input('ingrese un numero: '))
    num2 = float(input('ingrese otro numero: '))
    print('la suma es: ', num1 + num2)
elif opcion == 2:
    num1 = float(input('ingrese un numero: '))
    num2 = float(input('ingrese otro numero: '))
    print('la resta es: ', num1 - num2)
else:
    print('opcion no valida') 