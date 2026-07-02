from models.material import Material

materiais = []

def adicionar_material():
    nome = input("Digite o nome do material: ")
    preco = float(input("Digite o preço por m2: "))

    material = Material(nome, preco)
    materiais.append(material)

    print("Material cadastrado com sucesso")


def listar_materiais():
    if len(materiais) == 0:
        print("Nenhum material cadastrado.\n")
        return

    for i, material in enumerate(materiais):
        print(f"{i} - {material}")

    print()


def editar_material():
    listar_materiais()

    if len(materiais) == 0:
        return

    indice = int(input("Digite o indice do material que deseja editar: "))

    if 0 <= indice < len(materiais):
        novo_nome = input("Novo nome do material: ")
        novo_preco = float(input("Novo preço por m2: "))

        materiais[indice].nome = novo_nome
        materiais[indice].preco_m2 = novo_preco

        print("Material atualizado com sucesso")

    else:
        print("Indice invalido")

def excluir_material():
    listar_materiais()

    if len(materiais) == 0:
        return

    indice = int(input("Digite o indice do material que deseja excluir: "))

    if 0 <= indice < len(materiais):
        materiais.pop(indice)

        print("Material excluido com sucesso")

    else:
        print("Indice invalido")

def main():
    while True:
        print("1...Adicionar material")
        print("2...Listar materiais")
        print("3...Editar material")
        print("4...Excluir material")
        print("0...Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            adicionar_material()

        elif opcao == "2":
            listar_materiais()

        elif opcao == "3":
            editar_material()

        elif opcao == "4":
            excluir_material()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    main()
