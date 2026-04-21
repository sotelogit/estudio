menor = None
for valor in [3, 41, 12, 9, 74, 15,2]:
  if menor is None or valor < menor:
     menor = valor
print('El menor es:', menor)