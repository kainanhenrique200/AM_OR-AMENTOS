from models.material import Material, MaterialManager


def menu_materiais():

    manager = MaterialManager()

    while True:
        print("CADASTRO DE MATERIAIS")
        print("\n1 - Adicionar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Voltar")

        opcao = int(input("Opção: "))

        if opcao == 1:
            print("Nome do Material: ")
            nome = input("Nome: ")
            print("Valor do m²: ")
            preco = float(input("Preço: "))

            manager.adicionar_material(nome, preco)

        elif opcao == 2:

            manager.listar_materiais()

        elif opcao == 3:

            id = int(input("ID: "))

            nome = input("Novo nome: ")

            preco = float(input("Novo preço: "))

            manager.editar_material(id, nome, preco)

        elif opcao == 4:

            id = int(input("ID: "))

            manager.excluir_material(id)

        elif opcao == 0:

            break


if __name__ == "__main__":
    menu_materiais()
