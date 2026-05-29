class Material:
    def __init__(self, nome, preco_m2):
        self.nome = nome
        self.preco_m2 = preco_m2

    def __str__(self):
        return f"Material: {self.nome} | Preço por m2: R$ {self.preco_m2:.2f}"
