inicio = int(input("Numero de inicio pra tabuada: "))
fim = int(input("Numero do fim da tabuada: "))
numero_tabuada = int(input("Digite o teu número:"))

print("Tabuada do parceiro número", numero_tabuada)

while inicio <= fim:
    print(numero_tabuada, "x", inicio, "=", numero_tabuada * inicio)
    inicio += 1