import random


def embaralhar(palavra):

    palavra = palavra.lower()

    letras = list(palavra)

    random.shuffle(letras)

    return "".join(letras)


palavra = input("Digite uma palavra: ")

print("Palavra embaralhada:", embaralhar(palavra))