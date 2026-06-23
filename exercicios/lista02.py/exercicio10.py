
contador = 0
numero = 1
soma = 0


while numero > 0:
    numero = int(input("Digite um numero: "))
    soma = soma + numero
    contador += 1

media = soma/contador
print(media)
