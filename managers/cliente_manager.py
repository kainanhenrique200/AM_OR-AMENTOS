from models.cliente import Cliente


class ClienteManager:
    def __init__(self):
        self.clientes = []
        self.clientes_arquivados = []
        self.proximo_id = 1


    def cadastrar_cliente(self):
        print("\nCadastro de Cliente")

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")

        novo_cliente = Cliente(
            self.proximo_id,
            nome,
            telefone,
            email
        )

        self.clientes.append(novo_cliente)

        print("Cliente cadastrado com sucesso!")

        self.proximo_id += 1


    def listar_clientes(self):
        print("\nLista de Clientes")

        if len(self.clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in self.clientes:
            cliente.exibir_dados()


    def editar_cliente(self):
        id_busca = int(input("Digite o ID do cliente: "))

        for cliente in self.clientes:
            if cliente.id == id_busca:
                print("Cliente encontrado!")

                cliente.nome = input("Novo nome: ")
                cliente.telefone = input("Novo telefone: ")
                cliente.email = input("Novo email: ")

                print("Cliente atualizado!")
                return

        print("Cliente não encontrado.")

  
    def excluir_cliente(self):
        id_busca = int(input("Digite o ID para excluir: "))

        for cliente in self.clientes:
            if cliente.id == id_busca:
                self.clientes.remove(cliente)
                print("Cliente excluído.")
                return

        print("Cliente não encontrado.")

    def arquivar_cliente(self):
        id_busca = int(input("Digite o ID para arquivar: "))

        for cliente in self.clientes:
            if cliente.id == id_busca:
                cliente.arquivado = True

                self.clientes.remove(cliente)
                self.clientes_arquivados.append(cliente)

                print("Cliente arquivado.")
                return

        print("Cliente não encontrado.")

    def restaurar_cliente(self):
        id_busca = int(input("Digite o ID para restaurar: "))

        for cliente in self.clientes_arquivados:
            if cliente.id == id_busca:
                cliente.arquivado = False

                self.clientes_arquivados.remove(cliente)
                self.clientes.append(cliente)

                print("Cliente restaurado.")
                return

        print("Cliente não encontrado.")


    def menu(self):
        while True:
            print("\n MENU ")
            print("1....Cadastrar cliente")
            print("2....Listar clientes")
            print("3....Editar cliente")
            print("4....Excluir cliente")
            print("5....Arquivar cliente")
            print("6....Restaurar cliente")
            print("0....Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_cliente()

            elif opcao == "2":
                self.listar_clientes()

            elif opcao == "3":
                self.editar_cliente()

            elif opcao == "4":
                self.excluir_cliente()

            elif opcao == "5":
                self.arquivar_cliente()

            elif opcao == "6":
                self.restaurar_cliente()

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")


def menu_clientes():
    sistema = ClienteManager()
    sistema.menu()


if __name__ == "__main__":
    menu_clientes()