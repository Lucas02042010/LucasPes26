

notas = []

quantidade_notas= int(input("Quantas notas vão ser digitadas? "))

for i in range(quantidade_notas):
    nota = float (input("Sua nota: "))
    notas.append(nota)

print ("Notas digitadas:")

for nota in notas:
    print(nota)