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

