def sumarec(numero):
# caso base     
    if numero == 1:
        return 1
    else:
        return numero + sumarec(numero - 1)
print(sumarec(5))    