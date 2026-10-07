class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
    def exibir(self):
        print(self.nome, self.idade, self.altura, self.altura)
    
    def imc(self):
        imcc = self.peso/(self.altura*self.altura)
        print(imcc)
    
    def imc_nome(self):
        imccc = self.peso/(self.altura*self.altura)
        print(self.nome, imccc)

Maloka1 = Pessoa("Zii", 17, 1.8, 56)
Maloka2 = Pessoa("Negox", 18, 1.6, 98)
Maloka3 = Pessoa("zanzan", 16, 1.5, 120)

Malokas= [Maloka1, Maloka2, Maloka3]

for bosta in Malokas:
    bosta.exibir()
    bosta.imc()
    bosta.imc_nome()

