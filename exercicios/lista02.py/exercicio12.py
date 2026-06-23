while True:
    print("\n1-Adição  2-Subtração  3-Divisão  4-Multiplicação  0-Sair")
    op = int(input("Opção: "))

    if op == 0:
        break
    if op not in [1, 2, 3, 4]:
        print("Opção inválida!")
        continue

    a = float(input("Número 1: "))
    b = float(input("Número 2: "))

    if op == 1:
        print(a + b)
    elif op == 2:
        print(a - b)
    elif op == 3:
        print("Erro" if b == 0 else a / b)
    else:
        print(a * b)
        