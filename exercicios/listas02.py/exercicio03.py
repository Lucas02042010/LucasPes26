numero = int(input("Informe um número: "))
contador = 1

if numero >= 1:
    while contador <= numero:
        print(contador)
        contador += 1
else:
    while contador >= numero:
        print(contador)
        contador -= 1
