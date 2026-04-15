def min(valores):
 menor = None
 for valor in valores:
  if menor is None or valor < menor:
   menor = valor
 return menor
print(min([3, 41, 12, 9, 74, 15]))