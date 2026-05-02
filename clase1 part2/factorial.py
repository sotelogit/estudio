def factorial_recursivo(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Llamada recursiva
    else:
        return n * factorial_recursivo(n - 1)

print("El factorial de 5 es", factorial_recursivo(5))