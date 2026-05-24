class Material:
    def __init__(self, nome, preco_m2):
        self.nome = nome
        self.preco_m2 = preco_m2

    def __str__(self):
        return f"Material: {self.nome} | Preço por m2: R$ {self.preco_m2:.2f}"


class MaterialManager:
    def __init__(self):
        self.lista_materiais = []
        self.contador_id = 1

    def adicionar_material(self, nome, preco):
        novo = Material(self.contador_id, nome, preco)
        self.lista_materiais.append(novo)
        self.contador_id += 1

    def listar_materiais(self):
        if not self.lista_materiais:
            print("\n Lista Vazia ")
        else:
            for mat in self.lista_materiais:
                print(f"ID: {mat.id} | Nome: {mat.nome} | R$/m²: {mat.preco_m2}")

    def editar_material(self, id_busca, novo_nome, novo_preco):
        for mat in self.lista_materiais:
            if mat.id == id_busca:
                mat.nome = novo_nome
                mat.preco = novo_preco
                return True
        return False

    def excluir_material(self, id_busca):
        for mat in self.lista_materiais:
            if mat.id == id_busca:
                self.lista_materiais.remove(mat)
                return True
        return False

