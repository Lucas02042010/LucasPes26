import pickle

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

escolha = -67

while escolha != 0:
    print("Cadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir pessoa")
    print("4 - Atualizar pessoa")
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
            print("Nenhuma pessoa cadastrada.")
        else:
            for i in range(len(cadastro)):
                cadastro[i].exibir()
                cadastro[i].nome_imc()

    elif escolha == 3:
        nome = input("Nome da pessoa que deseja excluir: ")
        encontrou = False

        for i in range(len(cadastro)):
            if cadastro[i].nome == nome:
                cadastro.pop(i)
                encontrou = True
                print("Pessoa excluida")
                break

        if encontrou == False:
            print("Pessoa nao encontrada")

    elif escolha == 4:
        nome = input("Nome da pessoa que deseja atualizar: ")
        encontrou = False

        for i in range(len(cadastro)):
            if cadastro[i].nome == nome:
                cadastro[i].idade = int(input("Nova idade: "))
                cadastro[i].altura = float(input("Nova altura: "))
                cadastro[i].peso = float(input("Novo peso: "))

                encontrou = True
                print("Pessoa atualizada")
                break

        if encontrou == False:
            print("Pessoa nao encontrada")

    elif escolha == 5:
        arquivo = open("cadastro.pkl", "wb")
        pickle.dump(cadastro, arquivo)
        arquivo.close()

        print("Dados salvos com sucesso!")

    elif escolha == 6:
        try:
            arquivo = open("cadastro.pkl", "rb")
            cadastro = pickle.load(arquivo)
            arquivo.close()

            print("Dados carregados com sucesso!")

        except FileNotFoundError:
            print("Arquivo nao encontrado. Salve os dados primeiro.")

    elif escolha == 0:
        print("Saindo...")

    else:
        print("Opcao invalida!")

# a partir do picle fui eu, antes, foi o chat
