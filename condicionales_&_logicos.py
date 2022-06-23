numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))

if numero1 >= 0 and numero2 >= 0:
    print("Ambos numeros son positivos")

elif numero1 == 0:
    print("El primer numero es cero")

else:
    if numero1 < 0 and numero2 < 0:
        print("Ambos numeros son negativos")
