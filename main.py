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
            menu_metragens()

        elif opcao == "4":
            menu_materiais()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu_principal()
