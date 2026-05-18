def min(valores):
 menor = None
 for valor in valores:
  if menor is None or valor < menor:
   menor = valor
 return menor
numeros = [5, 2, 9, 1, 5, 6]
resultado = min(numeros)
print("El valor mínimo es:", resultado)