lista = []
quantidade = 0

while True:
    print("\n1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if quantidade < 15:
            placa = input("Digite a placa: ")
            lista.append(placa)
            quantidade = quantidade + 1
            print("Placa cadastrada com sucesso!")
        else:
            print("Não há espaço disponível.")

    elif opcao == "2":
        placa = input("Digite a placa que deseja excluir: ")

        if placa in lista:
            lista.remove(placa)
            quantidade = quantidade - 1
            print("Placa excluída com sucesso!")
        else:
            print("Placa não encontrada.")

    elif opcao == "3":
        if quantidade == 0:
            print("Nenhuma placa cadastrada.")
        else:
            print("Placas cadastradas:")
            for placa in lista:
                print(placa)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")