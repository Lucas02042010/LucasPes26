def converter_hora(hora):
    partes = hora.split(":")

    horas = int(partes[0])
    minutos = partes[1]

    if horas >= 12:
        periodo = "P"
    else:
        periodo = "A"

    if horas == 0:
        horas = 12
    elif horas > 12:
        horas = horas - 12

    return str(horas) + ":" + minutos, periodo


def mostrar_hora(hora, periodo):
    print(hora, periodo + ".M.")


while True:

    hora = input("Digite a hora (HH:MM) ou 0 para sair: ")

    if hora == "0":
        break

    hora_convertida, periodo = converter_hora(hora)

    mostrar_hora(hora_convertida, periodo)