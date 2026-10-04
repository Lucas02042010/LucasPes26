def data_por_extenso(data):

    meses = [
        "janeiro", "fevereiro", "março", "abril",
        "maio", "junho", "julho", "agosto",
        "setembro", "outubro", "novembro", "dezembro"
    ]

    partes = data.split("/")

    dia = int(partes[0])
    mes = int(partes[1])
    ano = partes[2]

    return str(dia) + " de " + meses[mes - 1] + " de " + ano


data = input("Digite uma data (DD/MM/AAAA): ")

print(data_por_extenso(data))