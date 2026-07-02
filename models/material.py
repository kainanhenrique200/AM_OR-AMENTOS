# models/material.py
class Produto:
    def __init__(self, nome):
        self.nome = nome


class Material(Produto):
    def __init__(self, nome, preco_m2):
        super().__init__(nome)
        self.preco_m2 = preco_m2

    def __str__(self):
        return f"Material: {self.nome} | Preço por m²: R$ {self.preco_m2:.2f}"
