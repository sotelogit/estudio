def factorial(n):
    if type(n) is not int:
     raise ValueError("El número debe ser un entero")

    elif n < 0:
        raise ValueError("El número debe ser un entero positivo")         
    elif n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))  # Output: 120