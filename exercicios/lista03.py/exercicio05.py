codigos = []
nomes = []
idades = []
alturas = []
pesos = []

opcao = -1
codigo = 1

while opcao != 0:
    print("""
1 - Cadastrar
2 - Excluir
3 - Alterar
4 - Listar
0 - Sair
""")

    opcao = int(input("Opcao: "))

    if opcao == 1:
        nomes.append(input("Digite o nome: "))
        idades.append(int(input("Digite a idade: ")))
        alturas.append(float(input("Digite a altura: ")))
        pesos.append(float(input("Digite o peso: ")))
        codigos.append(codigo)
        codigo = codigo + 1

    elif opcao == 2:
        nome = input("Escolha um para excluir da lista: ")

        if nome in nomes:
            i = nomes.index(nome)

            nomes.pop(i)
            idades.pop(i)
            alturas.pop(i)
            pesos.pop(i)
            codigos.pop(i)

            print("Cadastro excluído!")
        else:
            print("Nome não encontrado!")

    elif opcao == 3:
        nome = input("Digite o nome para alterar: ")

        if nome in nomes:
            i = nomes.index(nome)

            idades[i] = int(input("Digite a nova idade: "))
            alturas[i] = float(input("Digite a nova altura: "))
            pesos[i] = float(input("Digite o novo peso: "))

            print("Cadastro alterado!")
        else:
            print("Nome não encontrado!")

    elif opcao == 4:
        for i in range(len(nomes)):
            print("-------------------------")
            print("Código:", codigos[i])
            print("Nome:", nomes[i])
            print("Idade:", idades[i])
            print("Altura:", alturas[i])
            print("Peso:", pesos[i])

    elif opcao == 0:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")


