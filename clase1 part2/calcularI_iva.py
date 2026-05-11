def calcular_iva(p):
    iva = p * 0.19
    return iva

precio_compra = float(input("Ingrese valor de compra: "))
total = precio_compra + calcular_iva(precio_compra)
print("El total con IVA es:", total)