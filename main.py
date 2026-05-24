import sys
import os

# 1. Adiciona a pasta 'models' ao path para que o import 'from material import Material' funcione no material_manager
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

# 2. Importa o módulo material e injeta a classe MaterialManager dinâmica
import models.material

class MaterialManagerShim:
    def __init__(self):
        self.lista = []
        self.id = 1

    def adicionar_material(self, nome, preco):
        material = models.material.Material(nome, preco)
        material.id = self.id
        self.lista.append(material)
        self.id += 1

    def listar_materiais(self):
        if len(self.lista) == 0:
            print("\nNenhum material cadastrado.")
            return

        print("\nMateriais disponíveis:")
        for material in self.lista:
            print(f"ID: {material.id} | {material.nome} | R$ {material.preco_m2:.2f}/m²")

    def buscar_por_id(self, id_material):
        for material in self.lista:
            if material.id == id_material:
                return material
        return None

models.material.MaterialManager = MaterialManagerShim

# 3. Importa os managers de forma segura agora que as credenciais e classes estão injetadas
from managers.cliente_manager import ClienteManager
from managers.orcamento_manager import menu_orcamentos
from managers.segmento_manager import menu_metragens
from managers.material_manager import main as menu_materiais


def menu_principal():
    cliente_manager = ClienteManager()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Clientes")
        print("2 - Orçamentos")
        print("3 - Metragens")
        print("4 - Materiais")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cliente_manager.menu()

        elif opcao == "2":
            menu_orcamentos()

        elif opcao == "3":
            menu_metragens(cliente_manager)

        elif opcao == "4":
            menu_materiais()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu_principal()
