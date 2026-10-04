professores = {
    "001": "Prof Thiago Paes",
    "002": "Prof Schalata",
    "003": "Prof Ignácio",
    "004": "Prof Ryan",
    "005": "Prof André",
    "006": "Profª Fabiana",
    "007": "Prof Alberto",
    "008": "Prof Juliano",
    "009": "Prof Thiago Waltrik",
    "010": "Prof João Eduardo"
}

acessos = {
    "Lab102": ["003", "001", "004", "005", "006"],
    "Lab103": ["007"],
    "Lab104": ["004", "008", "002", "005"],
    "Lab105": ["003", "007", "009", "001"],
    "Lab106": ["002", "003", "009", "001"],
    "Lab107": ["005", "002", "009", "001", "010"]
}


def listar_professores():
    print("\n--- PROFESSORES ---")

    for codigo, nome in professores.items():
        print(codigo, "-", nome)


def listar_acessos():
    print("\n--- ACESSOS ---")

    for laboratorio, lista in acessos.items():
        print("\n", laboratorio)

        for codigo in lista:
            print("-", professores[codigo])


def adicionar_professor():
    codigo = input("Digite o código do professor: ")
    nome = input("Digite o nome do professor: ")

    professores[codigo] = nome

    print("Professor cadastrado!")


def alterar_professor():
    codigo = input("Digite o código do professor: ")

    if codigo in professores:
        nome = input("Digite o novo nome: ")
        professores[codigo] = nome
        print("Professor alterado!")
    else:
        print("Professor não encontrado.")


def excluir_professor():
    codigo = input("Digite o código do professor: ")

    if codigo in professores:
        del professores[codigo]

        for laboratorio in acessos:
            if codigo in acessos[laboratorio]:
                acessos[laboratorio].remove(codigo)

        print("Professor excluído!")
    else:
        print("Professor não encontrado.")


def adicionar_acesso():
    laboratorio = input("Digite o laboratório: ")
    codigo = input("Digite o código do professor: ")

    if laboratorio not in acessos:
        print("Laboratório inválido.")
    elif codigo not in professores:
        print("Professor não encontrado.")
    else:
        if codigo not in acessos[laboratorio]:
            acessos[laboratorio].append(codigo)
            print("Acesso cadastrado!")
        else:
            print("Esse professor já possui acesso.")


def alterar_acesso():
    laboratorio = input("Digite o laboratório: ")
    codigo_antigo = input("Código antigo do professor: ")
    codigo_novo = input("Novo código do professor: ")

    if laboratorio in acessos and codigo_antigo in acessos[laboratorio]:
        acessos[laboratorio].remove(codigo_antigo)
        acessos[laboratorio].append(codigo_novo)
        print("Acesso alterado!")
    else:
        print("Acesso não encontrado.")


def excluir_acesso():
    laboratorio = input("Digite o laboratório: ")
    codigo = input("Digite o código do professor: ")

    if laboratorio in acessos and codigo in acessos[laboratorio]:
        acessos[laboratorio].remove(codigo)
        print("Acesso excluído!")
    else:
        print("Acesso não encontrado.")


def testar_acesso():
    laboratorio = input("Digite o laboratório: ")
    codigo = input("Digite o código do professor: ")

    if laboratorio in acessos and codigo in acessos[laboratorio]:
        print("ACESSO PERMITIDO!")
    else:
        print("ACESSO NEGADO!")


while True:
    print("\n===== SISTEMA DE ACESSO =====")
    print("1 - Listar professores")
    print("2 - Adicionar professor")
    print("3 - Alterar professor")
    print("4 - Excluir professor")
    print("5 - Listar acessos")
    print("6 - Adicionar acesso")
    print("7 - Alterar acesso")
    print("8 - Excluir acesso")
    print("9 - Testar acesso")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_professores()

    elif opcao == "2":
        adicionar_professor()

    elif opcao == "3":
        alterar_professor()

    elif opcao == "4":
        excluir_professor()

    elif opcao == "5":
        listar_acessos()

    elif opcao == "6":
        adicionar_acesso()

    elif opcao == "7":
        alterar_acesso()

    elif opcao == "8":
        excluir_acesso()

    elif opcao == "9":
        testar_acesso()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")