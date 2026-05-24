from models.material import MaterialManager


def menu_materiais(material_manager: MaterialManager = None):
    if material_manager is None:
        material_manager = MaterialManager()

    while True:
        print("\n=== MENU - MATERIAIS ===")
        print("1 - Adicionar material")
        print("2 - Listar materiais")
        print("3 - Editar material")
        print("4 - Excluir material")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do material: ")
            try:
                preco = float(input("Preço por m²: "))
            except ValueError:
                print("Preço inválido.")
                continue

            material_manager.adicionar_material(nome, preco)
            print("Material cadastrado com sucesso!")

        elif opcao == "2":
            material_manager.listar_materiais()

        elif opcao == "3":
            material_manager.listar_materiais()
            try:
                id_material = int(input("Digite o ID do material que deseja editar: "))
                novo_nome = input("Novo nome do material: ")
                novo_preco = float(input("Novo preço por m²: "))
            except ValueError:
                print("Entrada inválida.")
                continue

            if material_manager.editar_material(id_material, novo_nome, novo_preco):
                print("Material atualizado com sucesso.")
            else:
                print("ID inválido.")

        elif opcao == "4":
            material_manager.listar_materiais()
            try:
                id_material = int(input("Digite o ID do material que deseja excluir: "))
            except ValueError:
                print("ID inválido.")
                continue

            if material_manager.excluir_material(id_material):
                print("Material excluído com sucesso.")
            else:
                print("ID inválido.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

    return material_manager
