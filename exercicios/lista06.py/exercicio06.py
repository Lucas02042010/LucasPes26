
class pessoa: 
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        print(self.nome, self.idade, self.altura, self.peso)
        
    def IMC(self): 
        imcc = self.peso/(self.altura*self.altura)
        return (imcc)
    
    def sla(self):
        imccc = self.peso/(self.altura*self.altura)
        return (self.nome, imccc) 

Pessoa1 = pessoa("Arthur", 17, 1.8, 56)
Pessoa2 = pessoa("Luiz", 18, 1.6, 98)
Pessoa3 = pessoa("emmeadosde2012", 16, 1.5, 120)

Pessoa= [Pessoa1, Pessoa2, Pessoa3]

for i in Pessoa:
    i.exibir()
    i.IMC()
    i.sla()






cadastro  = []

escolha =-67

while escolha != 0:
    print("""
Amigos Próximos
---------------
1 - Cadastrar
2 - Listar
0 - Sair
""")
escolha = int(input("Opção: "))

if escolha == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura (ex: 1.75): "))
        peso = float(input("Peso (ex: 70.5): "))

        # Instancia o objeto da classe Pessoa e adiciona à lista
        nova_pessoa = Pessoa(nome, idade, altura, peso)
        cadastro.append(nova_pessoa)
        print("\nPessoa cadastrada com sucesso!")

elif escolha == 2:
        if len(cadastro) == 0:
            print("\nNenhuma pessoa cadastrada.")
        else:
            print("\n--- Pessoas Cadastradas ---")
            for p in cadastro:
                p.exibir()

elif escolha == 0:
        print("\nSaindo do programa...")

else:
        print("\nOpção inválida! Tente novamente.")