numero_tabuada = int(input("Digite um numero pra mostrar a tabuada: "))

contador = 1

print("Tabuada do número ", numero_tabuada)

while contador <= 10:
    print(numero_tabuada, "x", contador, "=", numero_tabuada * contador)
    contador += 1
    