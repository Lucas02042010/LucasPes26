notas = []

escolha = -67

while escolha != 0:

    print("""
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
0 - Sair
""")

    escolha = int(input("Opção: "))

    if escolha == 1:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        print("A nota foi cadastrada!")

    elif escolha == 2:
        if len(notas) == 0:
            print("A lista de notas está vazia!")
        else:
            for i in range(len(notas)):
                print(i, "-", notas[i])

            indice = int(input("Digite o índice da nota que deseja excluir: "))

            if indice >= 0 and indice < len(notas):
                notas.pop(indice)
                print("A nota foi excluída!")
            else:
                print("Índice inválido!")

    elif escolha == 3:
        if len(notas) == 0:
            print("A lista de notas está vazia!")
        else:
            print("Notas cadastradas:")

            for nota in notas:
                print(nota)

    elif escolha == 4:
        if len(notas)==0:
            print("A lista de notas está vazia")
        else:
            media = sum(notas) / len(notas)

            print("Média:", media)

            if media >= 6:
                print("Aprovado!")
            else:
                print("Reprovado!")

    elif escolha == 0:
        print("Programa acabou!")

    else:
        print("Opção inválida!")