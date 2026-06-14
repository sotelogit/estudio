tabla = int(input('que tebla nesecita: '))
for i in range (1, 11):
  for j in range (1, 11):   
    print(f'{tabla} x {i} = {tabla*i}', end=' ')
  print() # salto de linea despues de cada tabla  10
  