import tkinter as tk
from tkinter import ttk, messagebox


class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Orçamentos - PEOO")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        self.centralizar_janela(900, 600)
        self.criar_tela_inicial()

    def centralizar_janela(self, largura, altura):
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        pos_x = (largura_tela // 2) - (largura // 2)
        pos_y = (altura_tela // 2) - (altura // 2)

        self.root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_inicial(self):
        self.limpar_tela()

        frame = ttk.Frame(self.root, padding=30)
        frame.pack(fill="both", expand=True)

        titulo = ttk.Label(
            frame,
            text="Sistema de Orçamentos",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=20)

        subtitulo = ttk.Label(
            frame,
            text="Controle de clientes, materiais e orçamentos por m²",
            font=("Arial", 13)
        )
        subtitulo.pack(pady=5)

        ttk.Button(
            frame,
            text="Clientes",
            width=30,
            command=self.abrir_clientes
        ).pack(pady=10)

        ttk.Button(
            frame,
            text="Materiais",
            width=30,
            command=self.abrir_materiais
        ).pack(pady=10)

        ttk.Button(
            frame,
            text="Orçamentos",
            width=30,
            command=self.abrir_orcamentos
        ).pack(pady=10)

        ttk.Button(
            frame,
            text="Sair",
            width=30,
            command=self.sair
        ).pack(pady=10)

    def criar_tela_padrao(self, titulo):
        self.limpar_tela()

        frame = ttk.Frame(self.root, padding=30)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text=titulo,
            font=("Arial", 24, "bold")
        ).pack(pady=30)

        ttk.Label(
            frame,
            text="Essa tela ainda está em desenvolvimento.",
            font=("Arial", 13)
        ).pack(pady=20)

        ttk.Button(
            frame,
            text="Voltar ao Menu Principal",
            width=30,
            command=self.criar_tela_inicial
        ).pack(pady=30)

    def abrir_clientes(self):
        self.criar_tela_padrao("Tela de Clientes")

    def abrir_materiais(self):
        self.criar_tela_padrao("Tela de Materiais")

    def abrir_orcamentos(self):
        self.criar_tela_padrao("Tela de Orçamentos")

    def sair(self):
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
        if resposta:
            self.root.destroy()