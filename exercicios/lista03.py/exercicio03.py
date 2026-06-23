
lista = [12, -1, -1, -1, 67, -1, -1, -1, -1, -1]

opcao_escolhida = -1
while opcao_escolhida != "0":
    print("""
        Menu
        ----
        1 – Cadastrar
        2 – Listar todos
        0 – Sair 
    """)
    opcao_escolhida = input("Digite sua opcão: ")

    if opcao_escolhida == "1":
        print("Criando")

        #substituir o valor se possível
        lugar_livre = 0
        for lugar in lista:
            if lugar < 0:
                break
            lugar_livre = lugar_livre + 1
 
        if lugar_livre > len(lista):
            print("Não posso cadastrar!")
        else:
            print("Tem um espaço no "+str(lugar_livre))

            lista[lugar_livre] = int(input("Digite seu codigo: "))
    elif opcao_escolhida == "2":
        print("Listar")
        for codigo in lista:
            if codigo > 0:
                print("Item com código: "+str(codigo))

