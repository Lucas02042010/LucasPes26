def impar_ou_par(valor):
    if (valor % 2) != 0:
        return ("É ímpar")
    else:
        return ("É par")
    
numero = int(input("Digite um number: "))
resultado = impar_ou_par(numero)
print(resultado)