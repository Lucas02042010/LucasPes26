class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
        return self.quantidade > 0

    def vender(self):
        if self.esta_disponivel():
            self.quantidade -= 1
            print("Produto vendido")
        else:
            print("Produto indisponível")


produto1 = Produto("Caderno", 2)

print("Disponível?", produto1.esta_disponivel())

produto1.vender()

print("Quantidade:", produto1.quantidade)
print("Disponível?", produto1.esta_disponivel())

produto1.vender()

print("Quantidade:", produto1.quantidade)
print("Disponível?", produto1.esta_disponivel())

produto1.vender()

