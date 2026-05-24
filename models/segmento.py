from models.cliente import Cliente
from calculos import calcular_area as _calc_area


class Metragem:

    def __init__(self, id, cliente, largura, comprimento):

        self.id = id

        self.cliente = cliente

        self.largura = largura

        self.comprimento = comprimento

        self.area = self.calcular_area()

    def calcular_area(self):
        return _calc_area(self.largura, self.comprimento)

    def mostrar(self):

        print(f"\nID: {self.id}")

        print(f"Cliente: {self.cliente.nome}")

        print(f"Largura: {self.largura}m")

        print(f"Comprimento: {self.comprimento}m")

        print(f"Área: {self.area:.2f}m²")


class SistemaMetragem:

    def __init__(self):

        self.lista = []

        self.id = 1

    def adicionar(self, cliente, largura, comprimento):

        metragem = Metragem(

            self.id,
            cliente,
            largura,
            comprimento
        )

        self.lista.append(metragem)

        self.id += 1

    def listar(self):

        if len(self.lista) == 0:

            print("\nNenhuma metragem cadastrada.")

        else:

            for metragem in self.lista:

                metragem.mostrar()

    def buscar_por_id(self, id):
        for metragem in self.lista:
            if metragem.id == id:
                return metragem
        return None

    def editar(self, id, largura, comprimento):

        for metragem in self.lista:

            if metragem.id == id:

                metragem.largura = largura

                metragem.comprimento = comprimento

                metragem.area = metragem.calcular_area()

                print("\nMetragem editada com sucesso!")

    def excluir(self, id):

        for metragem in self.lista:

            if metragem.id == id:

                self.lista.remove(metragem)

                print("\nMetragem excluída com sucesso!")
                return

        print("\nMetragem não encontrada.")