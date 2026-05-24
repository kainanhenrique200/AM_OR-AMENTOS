from models.segmento import SistemaMetragem
from managers.cliente_manager import ClienteManager


def menu_metragens(cliente_manager: ClienteManager):
    """
    Menu de metragens. Recebe o ClienteManager já instanciado
    pelo menu principal para que os dados sejam compartilhados.
    """

    sistema = SistemaMetragem()

    while True:

        print("\n=== MENU - METRAGENS ===")
        print("1 - Adicionar metragem")
        print("2 - Listar metragens")
        print("3 - Editar metragem")
        print("4 - Excluir metragem")
        print("0 - Voltar")

        opcao = input("\nOpção: ")

        if opcao == "1":

            # Selecionar cliente
            if len(cliente_manager.clientes) == 0:
                print("\nNenhum cliente cadastrado. Cadastre um cliente primeiro.")
                continue

            print("\n--- Clientes disponíveis ---")
            cliente_manager.listar_clientes()

            try:
                id_cliente = int(input("\nID do cliente: "))
            except ValueError:
                print("ID inválido.")
                continue

            cliente_escolhido = None
            for c in cliente_manager.clientes:
                if c.id == id_cliente:
                    cliente_escolhido = c
                    break

            if cliente_escolhido is None:
                print("Cliente não encontrado.")
                continue

            # Dimensões
            try:
                largura = float(input("Largura (m): "))
                comprimento = float(input("Comprimento (m): "))
            except ValueError:
                print("Valor inválido.")
                continue

            sistema.adicionar(cliente_escolhido, largura, comprimento)
            print("\nMetragem cadastrada com sucesso!")

        elif opcao == "2":

            sistema.listar()

        elif opcao == "3":

            try:
                id_metro = int(input("ID da metragem: "))
                largura = float(input("Nova largura (m): "))
                comprimento = float(input("Novo comprimento (m): "))
            except ValueError:
                print("Valor inválido.")
                continue

            sistema.editar(id_metro, largura, comprimento)

        elif opcao == "4":

            try:
                id_metro = int(input("ID da metragem: "))
            except ValueError:
                print("ID inválido.")
                continue

            sistema.excluir(id_metro)

        elif opcao == "0":

            print("\nVoltando ao menu principal...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    # Permite testar o módulo de forma isolada
    cm = ClienteManager()
    menu_metragens(cm)
