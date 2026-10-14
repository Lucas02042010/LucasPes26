class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        print(self.nome, self.idade, self.altura, self.peso)

    def imc(self):
        return self.peso / (self.altura * self.altura)

    def nome_imc(self):
        print(self.nome, self.imc())


cadastro = []

escolha = -1

while escolha != 0:
    print("Cadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")

    escolha = int(input("Opção: "))

    if escolha == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        nova_pessoa = Pessoa(nome, idade, altura, peso)
        cadastro.append(nova_pessoa)

        print("Pessoa cadastrada")

    elif escolha == 2:
        if len(cadastro) == 0:
            print("Nenhuma pessoa cadastrada")
        else:
            for i in range(len(cadastro)):
                cadastro[i].exibir()
                cadastro[i].nome_imc()

    elif escolha == 0:
        print("Saindo do programa")

    else:
        print("Opcao invalida")
