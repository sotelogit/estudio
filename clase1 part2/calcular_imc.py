def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

# Entrada de datos
try:
    mi_peso = float(input("Introduce tu peso (en kg): "))
    mi_altura = float(input("Introduce tu altura (en metros): "))
    
    resultado = calcular_imc(mi_peso, mi_altura)
    print(f"Tu IMC es: {resultado}")

    # Clasificación automática
    if resultado < 18.5:
        print(" Bajo peso ")
    elif 18.5 <= resultado < 25:
        print(" Peso normal ")
    elif 25 <= resultado < 30:
        print(" Sobrepeso ")
    else:
        print(" Obesidad ")

except ValueError:
    print("Error: Por favor, usá puntos para los decimales (ej: 1.75) y solo números.")