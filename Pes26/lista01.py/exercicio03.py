
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")


if usuario == "admin":
    if senha == "12345":
        print("Login bem-sucedido")
    else:
        print("Nome de usuário ou senha incorretos")
else: 
    print("Nome de usuário e senha incorretos")


