from models.material import Material, MaterialManager
from models.orcamento import Orcamento, SistemaOrcamentos


def menu_orcamentos(manager: MaterialManager = None):

    if manager is None:
        manager = MaterialManager()
        manager.adicionar_material("Granito Preto", 850)
        manager.adicionar_material("Mármore Branco", 1200)
        manager.adicionar_material("Quartzo", 1500)

    sistema = SistemaOrcamentos()

    while True:

        print("\nMENU - ORÇAMENTOS")

        print("1 - Criar orçamento")
        print("2 - Listar orçamentos")
        print("3 - Editar orçamento")
        print("4 - Salvar orçamento")
        print("0 - Voltar")

        opcao = int(input("\nOpção: "))

        if opcao == 1:

            cliente = input("Cliente: ")

            descricao = input("Descrição: ")

            print("\nMATERIAIS DISPONÍVEIS")

            manager.listar_materiais()

            id_material = int(input("\nEscolha o ID do material: "))

            material_escolhido = manager.buscar_por_id(id_material)

            if material_escolhido is None:

                print("Material inválido!")

                continue

            quantidade = int(input("Quantidade: "))

            area = float(input("Área m²: "))

            montagem = float(input("Valor montagem: "))

            taxa_cartao = float(input("Taxa cartão (%): "))

            observacao = input("Observação: ")

            novo_orcamento = Orcamento(

                cliente,
                descricao,
                material_escolhido,
                quantidade,
                area,
                montagem,
                taxa_cartao,
                observacao
            )

            sistema.criar_orcamento(novo_orcamento)

            print("\nOrçamento criado com sucesso!")

        elif opcao == 2:

            sistema.listar_orcamentos()

        elif opcao == 3:

            numero = int(input("Número do orçamento: "))

            nova_descricao = input("Nova descrição: ")

            sistema.editar_orcamento(numero, nova_descricao)

        elif opcao == 4:

            sistema.salvar_orcamento()

        elif opcao == 0:

            print("\nVoltando ao menu principal...")

            break


if __name__ == "__main__":
    menu_orcamentos()