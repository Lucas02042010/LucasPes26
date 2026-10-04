class carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def pintar(self):
        corx = input("Digite a nova cor: ")
        self.cor = corx

    def  mostrar_cor(self):
        print(self.cor)


carro1 = carro("Zuh", "zih")

carro1.pintar()
carro1.mostrar_cor()