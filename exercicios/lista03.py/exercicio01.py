idades = []

for i in range(6):
    idade = int(input("Qual a idade: "))
    idades.append(idade)

print("Maiores ou iguais a 16:")

for idade in idades:
    if idade >= 16:
        print(idade)