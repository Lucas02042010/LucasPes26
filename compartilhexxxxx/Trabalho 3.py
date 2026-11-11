
class Cliente:
    def __init__(self, Nome_Cliente, Endereco_Cliente, Id_Cliente, Senha_Cliente):
        self.Nome_Cliente = Nome_Cliente
        self.Endereco_Cliente = Endereco_Cliente
        self.Id_Cliente = Id_Cliente
        self.senha = Senha_Cliente


class Produto:
    def __init__(self, Nome_Produto, Id_Produto, Preco_Produto, Status_Produto):
        self.Nome_Produto = Nome_Produto
        self.Id_Produto = Id_Produto
        self.Preco_Produto = Preco_Produto
        self.Status_Produto = Status_Produto


class Vendedor:
    def __init__(self, Nome_Vendedor, Telefone_Vendedor, Endereco_Vendedor, Id_Vendedor):
        self.Nome_Vendedor = Nome_Vendedor
        self.Telefone_Vendedor = Telefone_Vendedor
        self.Endereco_Vendedor = Endereco_Vendedor
        self.Id_Vendedor = Id_Vendedor


usuario_log = None
produtos = []

escolha = -1

while escolha != 0:

    print("""
    1 -- Entrar como Cliente
    2 -- Cadastrar Produto
    3 -- Login Vendedor
    4 -- LogOut Cliente
    5 -- LogOut Vendedor
    6 -- Ver os produtos Cadastrados
    0 -- Sair
    """)

    escolha = int(input("Escolha uma opção: "))

    # LOGIN CLIENTE
    if escolha == 1:
        if usuario_log == None:
            nome_usuario = input("Digite seu e-mail: ")
            if "@" in nome_usuario:
                senha_usuario = input("Digite sua senha: ")
                endereco_usuario = input("Digite seu CEP: ")
                if len(endereco_usuario) == 8:
                    Id_usuario = input("Digite seu ID: ")
                    cliente = Cliente(
                        nome_usuario,
                        endereco_usuario,
                        Id_usuario,
                        senha_usuario
                    )
                    usuario_log = "cliente"
                    print("Bem vindo cliente!")
                else:
                    print("CEP inválido! Digite um CEP com 8 dígitos.")
            else:
                print("Esse e-mail é inválido!")
        else:
            print("Você é um Vendedor")

    # CADASTRAR PRODUTO
    elif escolha == 2:

        if usuario_log == "vendedor":

            fish = input("Digite o nome do produto: ")
            ball = input("Digite o ID do produto: ")
            cat = float(input("Digite o preço do produto: "))
            chocolex = input("Digite o status do produto: ")

            Xandao = Produto(fish, ball, cat, chocolex)
            produtos.append(Xandao)
            print("Cadastro de produto feito!")

        else:
            print("Você não tem permissão para cadastrar produtos!")

    # LOGIN VENDEDOR
    elif escolha == 3:

        if usuario_log == None:

            cuxcux = input("Nome do Vendedor: ")
            zinho = input("Telefone do Vendedor: ")
            zuzu = input("Digite seu CEP: ")
            frufru = input("ID Vendedor: ")

            ZanZan = Vendedor(cuxcux, zinho, zuzu, frufru)
            usuario_log = "vendedor"

            print("Entrando como vendedor...")

        else:
            print("Você é a bostinha de um cliente!")

    # LOGOUT CLIENTE
    elif escolha == 4:

        if usuario_log == "cliente":
            usuario_log = None

            print("Você saiu da conta de cliente!")

        else:
            print("Nenhum cliente está logado!")

    # LOGOUT VENDEDOR
    elif escolha == 5:

        if usuario_log == "vendedor":
            usuario_log = None
            print("Você saiu da conta de vendedor!")

        else:
            print("Nenhum vendedor está logado!")

    # VER PRODUTOS
    elif escolha == 6:

        if len(produtos) > 0:

            for produto in produtos:

                print("----------------------")
                print("Nome:", produto.Nome_Produto)
                print("ID:", produto.Id_Produto)
                print("Preço:", produto.Preco_Produto)
                print("Status:", produto.Status_Produto)
                print("----------------------")

        else:
            print("Nenhum produto cadastrado!")

    elif escolha == 0:
        print("Saindo do sistema... Até mais!")

    else:
        print("Opção inválida!")
