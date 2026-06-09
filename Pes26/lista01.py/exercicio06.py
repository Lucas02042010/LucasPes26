Jogador1 = input("Você vai jogar pedra, paper ou tesoura?")
Jogador2 = input("Você vai jogar pedra, paper ou tesoura?")

if Jogador1 == "pedra" and Jogador2 == "tesoura":
    print("Jogador1 levou")
if Jogador1 == "pedra" and Jogador2 == "paper":
    print("Jogador2 levou")
if Jogador1 == "pedra" and Jogador2 == "pedra":
    print("Empate!")

if Jogador1 == "tesoura" and Jogador2 == "paper":
    print("Jogador1 levou")
if Jogador1 == "tesoura" and Jogador2 == "tesoura":
    print("Empate!")

if Jogador1 == "paper" and Jogador2 == "paper":
    print("Empate!")


if Jogador2 == "pedra" and Jogador1 == "tesoura":
    print("Jogador2 levou")
if Jogador2 == "pedra" and Jogador1 == "paper":
    print("Jogador1 levou")
if Jogador2 == "pedra" and Jogador1 == "pedra":
    print("Empate!")

if Jogador2 == "tesoura" and Jogador1 == "paper":
    print("Jogador2 levou")
if Jogador2 == "tesoura" and Jogador1 == "tesoura":
    print("Empate!")

if Jogador2 == "paper" and Jogador1 == "paper":
    print("Empate!")
