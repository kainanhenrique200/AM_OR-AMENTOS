from models.material import Material, MaterialManager

lista_gerenciador = MaterialManager()

while True:
    print("1. Adicionar Material")
    print("2. Listar Materiais")
    print("3. Editar Material")
    print("4. Excluir Material")
    print("0. Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do material: ")
        preco = float(input("Preço por m²: "))
        lista_gerenciador.adicionar_material(nome, preco)
        print("Material cadastrado")

    elif opcao == 2:
        lista_gerenciador.listar_materiais()

    elif opcao == 3:
        id_edt = int(input("Digite o ID que deseja editar: "))
        novo_n = input("Novo nome: ")
        novo_p = float(input("Novo preco: "))
        if lista_gerenciador.editar_material(id_edt, novo_n, novo_p):
            print("Editado com sucesso!")
        else:
            print("ID não encontrado.")

    elif opcao == 4:
        id_exc = int(input("Digite o ID para excluir: "))
        if lista_gerenciador.excluir_material(id_exc):
            print("Excluído com sucesso")
        else:
            print("ID não encontrado.")

    elif opcao == 0:
        print("Sair")
        break 

    else:
        print("Opcao inválida, tente novamente.")
