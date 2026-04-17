mayor = None # None es un valor especial que se utiliza para indicar que no hay ningún valor asignado a una variable. En este caso, se utiliza para indicar que aún no se ha encontrado un valor mayor en la lista de números.
print('Antes:', mayor)
for valor in [3, 41, 12, 9, 74, 15, 85]:
  if mayor is None or valor > mayor :
    mayor = valor
  print("bucle:", valor, mayor)
print('Mayor:', mayor)