from datetime import datetime

caminhoes = {
    "001": "Monobloco",
    "002": "Scania 112 HW",
    "003": "Volkswagen Express 4150",
    "004": "Volkswagen Express 6160",
    "005": "Volkswagen VW 17230 Worker",
    "006": "Volkswagen Express 9170",
    "007": "Iveco Daily 40s14",
    "008": "Iveco Tectro 310E28"
}

condutores = {
    "001": "Roberto Souza",
    "002": "João Graciano",
    "003": "Karine Silva",
    "004": "Pedro Luiz",
    "005": "Maria Catarina",
    "006": "Júlio Cardoso",
    "007": "Altivo Antônio",
    "008": "Jorge Gonçalves",
    "009": "Marcos Vinícius",
    "010": "Heleno Nunes",
    "011": "Mara Cristina",
    "012": "Otávio Rocha"
}

saidas = {}


def listar_caminhoes():
    print("\n--- CAMINHÕES ---")

    for codigo, nome in caminhoes.items():
        print(codigo, "-", nome)


def listar_condutores():
    print("\n--- CONDUTORES ---")

    for codigo, nome in condutores.items():
        print(codigo, "-", nome)


def registrar_saida():
    codigo_caminhao = input("Código do caminhão: ")
    codigo_condutor = input("Código do condutor: ")

    if codigo_caminhao not in caminhoes:
        print("Caminhão não encontrado.")
        return

    if codigo_condutor not in condutores:
        print("Condutor não encontrado.")
        return

    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    saidas[codigo_caminhao] = {
        "condutor": codigo_condutor,
        "saida": data_hora,
        "chegada": None
    }

    print("Saída registrada!")


def registrar_retorno():
    codigo_caminhao = input("Código do caminhão: ")

    if codigo_caminhao in saidas:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

        saidas[codigo_caminhao]["chegada"] = data_hora

        print("Retorno registrado!")
    else:
        print("Esse caminhão não possui uma saída registrada.")


def consultar_caminhao():
    codigo = input("Digite o código do caminhão: ")

    if codigo not in saidas:
        print("Esse caminhão não saiu para uma rota.")
        return

    dados = saidas[codigo]

    print("\nCaminhão:", caminhoes[codigo])
    print("Condutor:", condutores[dados["condutor"]])
    print("Saída:", dados["saida"])

    if dados["chegada"] is None:
        print("Situação: AINDA NÃO RETORNOU")
    else:
        print("Chegada:", dados["chegada"])
        print("Situação: RETORNOU")


def listar_retorno_por_data():
    data = input("Digite a data (DD/MM/AAAA): ")

    encontrou = False

    for codigo, dados in saidas.items():

        if dados["chegada"] is not None:
            data_chegada = dados["chegada"].split()[0]

            if data_chegada == data:
                print(
                    codigo,
                    "-",
                    caminhoes[codigo],
                    "-",
                    condutores[dados["condutor"]]
                )

                encontrou = True

    if not encontrou:
        print("Nenhum caminhão retornou nessa data.")


def verificar_entregas():
    if len(saidas) == 0:
        print("Nenhuma saída foi registrada.")
        return

    todas = True

    for codigo in saidas:
        if saidas[codigo]["chegada"] is None:
            todas = False
            print("O caminhão", codigo, "ainda não retornou.")

    if todas:
        print("Todas as entregas foram realizadas!")
    else:
        print("Ainda existem entregas pendentes.")


while True:

    print("\n===== ALPHA ENTREGAS =====")
    print("1 - Listar caminhões")
    print("2 - Listar condutores")
    print("3 - Registrar saída")
    print("4 - Registrar retorno")
    print("5 - Consultar caminhão")
    print("6 - Listar retornos por data")
    print("7 - Verificar todas as entregas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_caminhoes()

    elif opcao == "2":
        listar_condutores()

    elif opcao == "3":
        registrar_saida()

    elif opcao == "4":
        registrar_retorno()

    elif opcao == "5":
        consultar_caminhao()

    elif opcao == "6":
        listar_retorno_por_data()

    elif opcao == "7":
        verificar_entregas()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")