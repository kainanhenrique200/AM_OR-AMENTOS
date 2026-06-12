import subprocess


def menu_principal():

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Clientes")
        print("2 - Materiais")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("em manutenção")

        if opcao == "2":

            subprocess.run(
                ["python", "-m", "managers.material_manager"]
            )

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu_principal()