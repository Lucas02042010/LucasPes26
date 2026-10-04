def desenhar_moldura(linhas=1, colunas=1):

    if linhas < 1:
        linhas = 1
    elif linhas > 20:
        linhas = 20

    if colunas < 1:
        colunas = 1
    elif colunas > 20:
        colunas = 20

    print("+" + "-" * colunas + "+")

    for i in range(linhas - 2):
        print("|" + " " * colunas + "|")

    if linhas > 1:
        print("+" + "-" * colunas + "+")


linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

desenhar_moldura(linhas, colunas)