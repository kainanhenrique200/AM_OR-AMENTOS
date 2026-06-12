from models.orcamento import Orcamento
from managers.material_manager import materiais

orcamentos = []


def criar_orcamento():

    if len(materiais) == 0:
        print("Nenhum material cadastrado.")
        return

    cliente = input("Digite o nome do cliente: ")
    descricao = input("Digite a descrição do orçamento: ")

    print("\nMateriais disponíveis:")

    contador = 0
    for material in materiais:
        print(f"{contador} - {material.nome}")
        contador += 1

    indice = int(input("Escolha o material: "))

    quantidade = int(input("Digite a quantidade de peças: "))
    area = float(input("Digite a área em m²: "))
    montagem = float(input("Digite o valor da montagem: "))
    taxa_cartao = float(input("Digite a taxa do cartão (%): "))
    observacao = input("Digite uma observação: ")

    orcamento = Orcamento(
        cliente,
        descricao,
        materiais[indice],
        quantidade,
        area,
        montagem,
        taxa_cartao,
        observacao
    )

    orcamentos.append(orcamento)

    print("Orçamento cadastrado com sucesso")


def listar_orcamentos():

    if len(orcamentos) == 0:
        print("Nenhum orçamento cadastrado.\n")
        return

    contador = 0

    for orcamento in orcamentos:
        print(f"{contador} - {orcamento}")
        contador += 1

    print()


def editar_orcamento():

    listar_orcamentos()

    if len(orcamentos) == 0:
        return

    indice = int(input("Digite o índice do orçamento que deseja editar: "))

    if 0 <= indice < len(orcamentos):

        nova_descricao = input("Nova descrição: ")
        orcamentos[indice].descricao = nova_descricao

        print("Orçamento atualizado com sucesso")

    else:
        print("Índice inválido")


def excluir_orcamento():

    listar_orcamentos()

    if len(orcamentos) == 0:
        return

    indice = int(input("Digite o índice do orçamento que deseja excluir: "))

    if 0 <= indice < len(orcamentos):

        orcamentos.pop(indice)

        print("Orçamento excluído com sucesso")

    else:
        print("Índice inválido")


def calcular_total_orcamento():

    listar_orcamentos()

    if len(orcamentos) == 0:
        return

    indice = int(input("Digite o índice do orçamento: "))

    if 0 <= indice < len(orcamentos):

        orcamento = orcamentos[indice]

        valor_material = orcamento.material.preco_m2 * orcamento.area

        subtotal = valor_material + orcamento.montagem

        taxa = subtotal * (orcamento.taxa_cartao / 100)

        valor_final = subtotal + taxa

        print("\nRESULTADO")
        print(f"Cliente: {orcamento.cliente}")
        print(f"Descrição: {orcamento.descricao}")
        print(f"Material: {orcamento.material.nome}")
        print(f"Quantidade: {orcamento.quantidade}")
        print(f"Área: {orcamento.area} m²")
        print(f"Montagem: R$ {orcamento.montagem:.2f}")
        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Taxa do cartão: R$ {taxa:.2f}")
        print(f"Valor Final: R$ {valor_final:.2f}")

    else:
        print("Índice inválido")


def menu_orcamentos():

    while True:

        print("\n1...Adicionar orçamento")
        print("2...Listar orçamentos")
        print("3...Editar orçamento")
        print("4...Excluir orçamento")
        print("5...Calcular orçamento")
        print("0...Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_orcamento()

        elif opcao == "2":
            listar_orcamentos()

        elif opcao == "3":
            editar_orcamento()

        elif opcao == "4":
            excluir_orcamento()

        elif opcao == "5":
            calcular_total_orcamento()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_orcamentos()