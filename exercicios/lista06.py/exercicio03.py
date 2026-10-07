class contabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        valor = int(input("Digite o valor: "))
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        print (self.saldo)


contabancaria1 = contabancaria("Zanzan", "100")

contabancaria1.depositar()
contabancaria1.sacar()





