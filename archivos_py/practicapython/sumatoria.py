def suma_comun(limite):
    total = 0  # Acá se guarda la suma
    for i in range(1, limite + 1):# base del sigma
      print(i,end=" ") 
      total = total + i # formula aplicada centro del sigma
    return total

print(suma_comun(5)) # ultimo valor del sigma