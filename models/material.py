class Material:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

class MaterialManager:

    def __init__(self):
        self.lista = []
        self.id = 1

    def adicionar_material(self, nome, preco):

        material = Material(self.id, nome, preco)

        self.lista.append(material)

        self.id += 1

    def listar_materiais(self):

        for material in self.lista:

            print(material.id, material.nome, material.preco)

    def editar_material(self, id, nome, preco):

        for material in self.lista:

            if material.id == id:

                material.nome = nome
                material.preco = preco

    def excluir_material(self, id):

        for material in self.lista:

            if material.id == id:

                self.lista.remove(material)

