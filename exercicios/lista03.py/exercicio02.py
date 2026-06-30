notas = []
media = 0

for i in range(4):
    nota = float(input("Qual a nota do estudante: "))
    notas.append(nota)

for nota in notas:
    media= media + nota

media = media / 4

print ("Média: ", media)

if media >= 6:
    print("Aprovado")
else:
    print ("Reprovado")