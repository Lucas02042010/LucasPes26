amigos_proximos  = []

escolha =-67

while escolha != 0:
    print("""
Amigos Próximos
---------------
1 - Cadastrar
2 - Excluir
3 - Listar
0 - Sair
""")
    
    escolha= int(input("Escolha uma opção: "))
    
    if escolha == 1:
        nome = input("Nome da conta? ")
        amigos_proximos.append(nome)
        print ("A conta foi cadastrada na lista de Amigos Próximos!")

    elif escolha == 2:
        if len(amigos_proximos) == 0:
            print ("Sua lista de Amigos Próximos está vazia! ")
        else:
            nome = input("Nome da conta que você deseja excluir da lista de Amigos Próximos: ")
        if nome in amigos_proximos:
            amigos_proximos.remove(nome)
            print ("A conta foi excluída! ")
        else:
            print("A conta não foi encontrada ")

    elif escolha == 3:
        if len(amigos_proximos) == 0:
            print("A lista de Amigos Próximos está vazia!")
        else:
            print("Amigos Próximos:")
            for amigo in amigos_proximos:
                print(amigo)

    elif escolha == 0:
        print("Programa cabou ")