codigo = 1


while codigo > 0:
    codigo = int(input("Codigo do produto escolhido(0 para sair): "))
    quantidade = int(input("A quantidade foi de: "))

    if codigo == 1:
        preço = quantidade * 6
        print(f"Voce comprou {quantidade} Sucos, custou {preço} reais")

    elif codigo == 2:
        preço = quantidade * 3
        print(f"Voce comprou {quantidade} Pao de queijo, custou {preço} reais")

    elif codigo == 2:
        preço = quantidade * 7
        print(f"Voce comprou {quantidade} Pastel, custou {preço} reais")

    elif codigo == 4:
        preço = quantidade * 9
        print(f"Voce comprou {quantidade} Saladao de fruta, custou {preço} reais")

    elif codigo == 5:
        preço = quantidade * 3,5
        print(f"Voce comprou {quantidade} Cafe com leite, custou {preço} reais")

    elif codigo == 6:
        preço = quantidade * 4,5
        print(f"Voce comprou {quantidade} Capuccino, custou {preço} reais")

    elif codigo == 7:
        preço = quantidade * 6,5
        print(f"Voce comprou {quantidade} Yogurt, custou {preço} reais")

    elif codigo == 8:
        preço = quantidade * 2,5
        print(f"Voce comprou {quantidade} Agua, custou {preço} reais")

    else:
        print ("Codigo nao vale")