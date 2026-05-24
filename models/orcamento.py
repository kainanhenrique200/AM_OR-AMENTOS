import json
from datetime import datetime
from models.material import Material
from calculos import calcular_total_orcamento as _calc_total

class Orcamento:

    cont = 1

    def __init__(
        self,
        cliente,
        descricao,
        material,
        quantidade,
        area,
        montagem,
        taxa_cartao,
        observacao=""
    ):

        self.numero = Orcamento.cont
        Orcamento.cont += 1

        self.cliente = cliente
        self.descricao = descricao

        self.material = material.nome
        self.valor_material = material.preco

        self.quantidade = quantidade
        self.area = area

        self.montagem = montagem
        self.taxa_cartao = taxa_cartao

        self.observacao = observacao

        self.data = datetime.now().strftime("%d/%m/%Y")

        self.valor_final = self.calcular_total_orcamento()

    def calcular_total_orcamento(self):
        return _calc_total(
            self.valor_material,
            self.quantidade,
            self.montagem,
            self.taxa_cartao
        )

    def mostrar_orcamento(self):

        print(f"\nORÇAMENTO {self.numero:02}")

        print(f"Cliente: {self.cliente}")

        print(f"Descrição: {self.descricao}")

        print(f"Material: {self.material}")

        print(f"Quantidade: {self.quantidade}")

        print(f"Área: {self.area}m²")

        print(f"Valor Material: R${self.valor_material:.2f}")

        print(f"Montagem: R${self.montagem:.2f}")

        print(f"Taxa Cartão: {self.taxa_cartao}%")

        print(f"Valor Final: R${self.valor_final:.2f}")

        print(f"Observação: {self.observacao}")

        print(f"Data: {self.data}")


class SistemaOrcamentos:

    def __init__(self):

        self.orcamentos = []

    def criar_orcamento(self, orcamento):

        self.orcamentos.append(orcamento)

    def listar_orcamentos(self):

        if len(self.orcamentos) == 0:

            print("\nNenhum orçamento cadastrado.")

        else:

            for orcamento in self.orcamentos:

                orcamento.mostrar_orcamento()

    def editar_orcamento(self, numero, nova_descricao):

        for orcamento in self.orcamentos:

            if orcamento.numero == numero:

                orcamento.descricao = nova_descricao

                print("\nOrçamento editado com sucesso!")

    def salvar_orcamento(self):

        dados = []

        for o in self.orcamentos:

            dados.append({

                "numero": o.numero,
                "cliente": o.cliente,
                "descricao": o.descricao,
                "material": o.material,
                "quantidade": o.quantidade,
                "area": o.area,
                "valor_material": o.valor_material,
                "montagem": o.montagem,
                "taxa_cartao": o.taxa_cartao,
                "valor_final": o.valor_final,
                "observacao": o.observacao,
                "data": o.data
            })

        with open("orcamentos.json", "w", encoding="utf-8") as arquivo:

            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

        print("\nOrçamentos salvos com sucesso!")