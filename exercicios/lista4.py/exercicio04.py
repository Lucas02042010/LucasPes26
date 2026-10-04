

cidades = []

quantidade_cidades= int(input("Quantas cidades vão ser digitadas? "))

for i in range(quantidade_cidades):
    cidade = int(input("Sua cidade: "))
    cidades.append(cidade)

print ("Cidades digitadas:")

for cidade in cidades:
    print(cidade)


cidade_remover = input("Qual cidade você quer remover?")

if cidade_remover in cidades:
    cidade.remove(cidade_remover)
    print("Nova lista: ")
    print (cidades)
else: 
    print ("Não tem essa city")
