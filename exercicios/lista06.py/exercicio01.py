class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        print (self.titulo, "foi escrito por",  self.autor)

livro1 = livro("ZIiiiiii", " Zanzenzo")
livro1.descricao()