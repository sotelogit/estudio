

def fib (n):
#formula de binet presiso hasta los numeros 70 80
  phi= 1.6180339
  psi= 0.61800339
  raiz_5=2.236067
  resultado=(phi**n-psi**n)/raiz_5
  if n > 50:
      print("ingrese un numero menor que 50") 
  else:
   return round(resultado)

posicion = int(input("escriba un numero del 1 al 50: "))

# 3. Llamamos a la función con ese número
resultado_final = fib(posicion)

# 4. Mostramos el resultado
print(f"El número en la posición {posicion} es: {resultado_final}")
