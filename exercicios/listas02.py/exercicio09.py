deposito = float(input("Digite o deposito: "))

grana = 0
mes = 1

while mes <= 24:
    grana = grana * 1.005
    grana = grana + deposito
    print("mes", mes, ":", grana, "reais")
    mes += 1