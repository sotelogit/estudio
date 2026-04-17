def cuenta_regresiva(numero):
    if numero <= 0:
        print("fin")
    else:
        print(numero, end=" ")
        cuenta_regresiva(numero - 1)
cuenta_regresiva(10)