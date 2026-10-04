def tempo_total(horas, minutos):
    return horas * 60 + minutos


horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

total = tempo_total(horas, minutos)

print("O tempo total foi de", total, "minutos.")