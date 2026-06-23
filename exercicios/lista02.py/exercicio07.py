quantidade_notas = int(input("Digite a quantidade de notas:  "))
contador = 0
notas = 0

while contador < quantidade_notas:
    nota = int(input("Digite a sua nota: "))
    notas = notas + nota
    contador += 1

media = notas/quantidade_notas
print("Sua média é: ", media)

if media < 6.0:
    print ("Reprovado")
else:
    print ("Aprovado")
