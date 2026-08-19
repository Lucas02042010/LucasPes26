def soma(lista):
    return sum(lista)


a = int(input("Digite o 1 valor: "))
b = int(input("Digite o 2 valor: "))
c = int(input("Digite o 3 valor: "))
d = int(input("Digite o 4 valor: "))

numeros = (a, b, c, d)

resultado = soma(numeros)

print("Resultado:", resultado)