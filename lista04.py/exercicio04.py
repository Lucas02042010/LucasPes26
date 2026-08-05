

cidades = []

quantidade_cidades= int(input("Quantas cidades vão ser digitadas? "))

for i in range(quantidade_cidades):
    cidade = float (input("Sua cidade: "))
    cidades.append(cidade)

print ("Cidades digitadas:")

for cidade in cidades:
    print(cidade)

del cidades[1]

print (cidades)