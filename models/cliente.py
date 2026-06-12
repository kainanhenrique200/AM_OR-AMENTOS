class Cliente:
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.arquivado = False

    def exibir_dados(self):
        status = "Arquivado" if self.arquivado else "Ativo"

        print(f"\nID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print(f"Status: {status}")
        print("-" * 30)