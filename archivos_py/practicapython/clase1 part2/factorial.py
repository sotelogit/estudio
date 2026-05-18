def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Llamada recursiva
    else:
        return n * factorial(n - 1)
print(factorial(5))    

