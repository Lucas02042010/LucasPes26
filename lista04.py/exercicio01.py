

bairros = ("Centro")

for i in range(5):
    nome = input("Digite o nome do bairro: ")
    bairros.append(nome)

print ("Bairros cadastrados: ")

for bairro in bairros:
    print (bairro)