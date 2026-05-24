class Material:
    def __init__(self, id_material, nome, preco):
        self.id = id_material
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"ID: {self.id} | {self.nome} | R$ {self.preco:.2f}/m²"


class MaterialManager:
    def __init__(self):
        self.lista_materiais = []
        self.proximo_id = 1

    def adicionar_material(self, nome, preco):
        material = Material(self.proximo_id, nome, preco)
        self.lista_materiais.append(material)
        self.proximo_id += 1

    def listar_materiais(self):
        if len(self.lista_materiais) == 0:
            print("\nNenhum material cadastrado.")
            return

        print("\nMateriais disponíveis:")
        for material in self.lista_materiais:
            print(material)

    def editar_material(self, id_material, novo_nome, novo_preco):
        for material in self.lista_materiais:
            if material.id == id_material:
                material.nome = novo_nome
                material.preco = novo_preco
                return True
        return False

    def excluir_material(self, id_material):
        for material in self.lista_materiais:
            if material.id == id_material:
                self.lista_materiais.remove(material)
                return True
        return False

    def buscar_por_id(self, id_material):
        for material in self.lista_materiais:
            if material.id == id_material:
                return material
        return None
