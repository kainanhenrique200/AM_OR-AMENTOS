from managers.material_manager import menu_materiais
from managers.orcamento_manager import menu_orcamentos


def menu_principal():

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Clientes")
        print("2 - Materiais")
        print("3 - Orçamentos")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("em manutenção")

        elif opcao == "2":
            menu_materiais()

        elif opcao == "3":
            menu_orcamentos()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu_principal()