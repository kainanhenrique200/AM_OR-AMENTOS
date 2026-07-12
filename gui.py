import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class SistemaCaixaIFRN:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE GESTÃO DE ORÇAMENTOS - IFRN (MODO TERMINAL/PDV)")
        self.root.geometry("1100x650")
        self.root.configure(bg="#F5F7FA")

        # Paleta de Cores Sólidas (Estilo Caixa de Supermercado/PDV)
        self.COR_PRIMARIA = "#2563EB"    # Azul Padrão
        self.COR_SUCESSO = "#22C55E"     # Verde (Salvar/Confirmar)
        self.COR_ALERTA = "#FACC15"      # Amarelo (Editar/Aviso)
        self.COR_PERIGO = "#EF4444"      # Vermelho (Excluir/Cancelar)
        self.COR_FUNDO_PANEL = "#FFFFFF"
        self.COR_TEXTO = "#374151"

        # --- BANCO DE DADOS EM MEMÓRIA (DADOS INICIAIS PARA O CRUD) ---
        self.BD_CLIENTES = [
            {"id": 1, "nome": "Ana Beatriz Medeiros", "cpf": "111.222.333-44", "telefone": "(84) 99812-3421", "email": "ana@ifrn.br", "endereco": "Av. Salgado Filho, Natal"},
            {"id": 2, "nome": "Carlos Eduardo Silva", "cpf": "555.666.777-88", "telefone": "(84) 98711-9088", "email": "carlos@ifrn.br", "endereco": "Rua das Laranjas, Mossoró"}
        ]

        self.BD_MATERIAIS = [
            {"id": 1, "nome": "Policarbonato Alveolar", "preco": 150.00, "unidade": "m²", "categoria": "Chapas"},
            {"id": 2, "nome": "Perfil de Alumínio 6m", "preco": 85.50, "unidade": "un", "categoria": "Estruturas"}
        ]

        self.BD_METRAGENS = [
            {"id": 1, "nome": "Área Padrão Comercial", "tamanho": "50m²", "multiplicador": 1.0},
            {"id": 2, "nome": "Cobertura Residencial", "tamanho": "15m²", "multiplicador": 1.2}
        ]

        self.BD_ORCAMENTOS = [
            {"id": 1, "cliente": "Ana Beatriz Medeiros", "material": "Policarbonato Alveolar", "metragem": "Área Padrão Comercial", "total": 150.00, "data": "12/07/2026", "obs": "Entrega urgente."}
        ]

        # Variáveis de controle de IDs
        self.proximo_id_cliente = 3
        self.proximo_id_material = 3
        self.proximo_id_metragem = 3
        self.proximo_id_orcamento = 2

        # Variáveis de seleção para Edição
        self.id_cliente_selecionado = None
        self.id_material_selecionado = None
        self.id_metragem_selecionado = None

        # Estilização das tabelas nativas
        self.configurar_estilos()

        # Montagem do Layout Base
        self.criar_layout_base()

        # Inicializa exibindo o Dashboard
        self.selecionar_aba("Dashboard")

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#FFFFFF", foreground=self.COR_TEXTO, rowheight=28, fieldbackground="#FFFFFF", font=("Courier New", 11))
        style.configure("Treeview.Heading", background="#374151", foreground="#FFFFFF", font=("Courier New", 11, "bold"))
        style.map("Treeview", background=[("selected", "#2563EB")], foreground=[("selected", "#FFFFFF")])

    def criar_layout_base(self):
        # Topbar / Cabeçalho do Caixa
        topbar = tk.Frame(self.root, bg=self.COR_PRIMARIA, height=50)
        topbar.pack(fill="x", side="top")

        lbl_titulo = tk.Label(topbar, text=" [PDV V1.0] SISTEMA DE ORÇAMENTOS IFRN ", font=("Courier New", 14, "bold"), bg=self.COR_PRIMARIA, fg="#FFFFFF")
        lbl_titulo.pack(side="left", padx=10, pady=10)

        self.lbl_relogio = tk.Label(topbar, text=datetime.now().strftime("%d/%m/%Y"), font=("Courier New", 12, "bold"), bg=self.COR_PRIMARIA, fg="#FFFFFF")
        self.lbl_relogio.pack(side="right", padx=15)

        # Menu Lateral Sólido (Estilo Caixa Registradora)
        self.sidebar = tk.Frame(self.root, bg="#374151", width=180)
        self.sidebar.pack(fill="y", side="left")
        self.sidebar.pack_propagate(False)

        modulos = ["Dashboard", "Clientes", "Materiais", "Metragens", "Orçamentos"]
        self.botoes_menu = {}

        for mod in modulos:
            btn = tk.Button(self.sidebar, text=f"[F_] {mod.upper()}", font=("Courier New", 11, "bold"),
                            bg="#4B5563", fg="#FFFFFF", bd=1, relief="raised", activebackground=self.COR_PRIMARIA,
                            command=lambda m=mod: self.selecionar_aba(m))
            btn.pack(fill="x", padx=5, pady=4)
            btn.configure(height=2)
            self.botoes_menu[mod] = btn

        # Container Principal das Telas
        self.container = tk.Frame(self.root, bg="#F5F7FA")
        self.container.pack(fill="both", expand=True, side="right", padx=15, pady=15)

    def selecionar_aba(self, nome_aba):
        # Limpar tela anterior
        for widget in self.container.winfo_children():
            widget.destroy()

        # Destacar botão ativo no menu
        for nome, btn in self.botoes_menu.items():
            if nome == nome_aba:
                btn.configure(bg=self.COR_PRIMARIA, fg="#FFFFFF")
            else:
                btn.configure(bg="#4B5563", fg="#FFFFFF")

        if nome_aba == "Dashboard":
            self.tela_dashboard()
        elif nome_aba == "Clientes":
            self.tela_clientes()
        elif nome_aba == "Materiais":
            self.tela_materiais()
        elif nome_aba == "Metragens":
            self.tela_metragens()
        elif nome_aba == "Orçamentos":
            self.tela_orcamentos()

    # ==========================================
    # 1. TELA DASHBOARD (RELATÓRIO DE SINAL)
    # ==========================================
    def tela_dashboard(self):
        lbl_info = tk.Label(self.container, text="=== RESUMO GERAL DO SISTEMA (PDV) ===", font=("Courier New", 14, "bold"), bg="#F5F7FA", fg=self.COR_TEXTO)
        lbl_info.pack(anchor="w", pady=(0, 15))

        painel_cards = tk.Frame(self.container, bg="#F5F7FA")
        painel_cards.pack(fill="x", pady=10)

        dados_cards = [
            ("CLIENTES CADASTRADOS", len(self.BD_CLIENTES)),
            ("MATERIAIS DISPONÍVEIS", len(self.BD_MATERIAIS)),
            ("METRAGENS MAPEADAS", len(self.BD_METRAGENS)),
            ("ORÇAMENTOS EMITIDOS", len(self.BD_ORCAMENTOS))
        ]

        for i, (tit, val) in enumerate(dados_cards):
            card = tk.Frame(painel_cards, bg="#FFFFFF", bd=2, relief="solid", width=200, height=100)
            card.grid(row=0, column=i, padx=10)
            card.pack_propagate(False)

            lbl_tit = tk.Label(card, text=tit, font=("Courier New", 9, "bold"), bg="#FFFFFF", fg="#64748B")
            lbl_tit.pack(pady=10)
            lbl_val = tk.Label(card, text=str(val), font=("Courier New", 24, "bold"), bg="#FFFFFF", fg=self.COR_PRIMARIA)
            lbl_val.pack()

    # ==========================================
    # 2. CRUD CLIENTES (100% OPERACIONAL)
    # ==========================================
    def tela_clientes(self):
        frame_esq = tk.Frame(self.container, bg="#F5F7FA")
        frame_esq.pack(side="left", fill="both", expand=True)

        frame_dir = tk.Frame(self.container, bg="#FFFFFF", bd=1, relief="solid", width=350)
        frame_dir.pack(side="right", fill="y", padx=(10, 0))
        frame_dir.pack_propagate(False)

        tk.Label(frame_esq, text="LISTA DE CLIENTES", font=("Courier New", 12, "bold"), bg="#F5F7FA").pack(anchor="w")

        colunas = ("id", "nome", "cpf", "telefone")
        tabela = ttk.Treeview(frame_esq, columns=colunas, show="headings")
        tabela.heading("id", text="ID")
        tabela.heading("nome", text="Nome")
        tabela.heading("cpf", text="CPF")
        tabela.heading("telefone", text="Telefone")
        tabela.column("id", width=40, anchor="center")
        tabela.column("nome", width=200)
        tabela.column("cpf", width=120)
        tabela.column("telefone", width=110)
        tabela.pack(fill="both", expand=True, pady=5)

        def atualizar_tabela_clientes():
            for row in tabela.get_children():
                tabela.delete(row)
            for c in self.BD_CLIENTES:
                tabela.insert("", "end", values=(c["id"], c["nome"], c["cpf"], c["telefone"]))
        atualizar_tabela_clientes()

        tk.Label(frame_dir, text=" FORMULÁRIO CLIENTE ", font=("Courier New", 12, "bold"), bg="#374151", fg="#FFFFFF").pack(fill="x", pady=(0, 10))

        tk.Label(frame_dir, text="Nome:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_nome = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_nome.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="CPF:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_cpf = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_cpf.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Telefone:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_tel = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_tel.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="E-mail:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_email = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_email.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Endereço:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_end = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_end.pack(fill="x", padx=10, pady=2)

        def salvar_cliente():
            if not ent_nome.get() or not ent_cpf.get():
                messagebox.showwarning("Aviso", "Nome e CPF são obrigatórios!")
                return

            if self.id_cliente_selecionado is None:
                novo = {
                    "id": self.proximo_id_cliente,
                    "nome": ent_nome.get(),
                    "cpf": ent_cpf.get(),
                    "telefone": ent_tel.get(),
                    "email": ent_email.get(),
                    "endereco": ent_end.get()
                }
                self.BD_CLIENTES.append(novo)
                self.proximo_id_cliente += 1
            else:
                for c in self.BD_CLIENTES:
                    if c["id"] == self.id_cliente_selecionado:
                        c.update({
                            "nome": ent_nome.get(),
                            "cpf": ent_cpf.get(),
                            "telefone": ent_tel.get(),
                            "email": ent_email.get(),
                            "endereco": ent_end.get()
                        })
            limpar_campos()
            atualizar_tabela_clientes()

        def carregar_cliente(event):
            item = tabela.selection()
            if item:
                valores = tabela.item(item, "values")
                self.id_cliente_selecionado = int(valores[0])
                for c in self.BD_CLIENTES:
                    if c["id"] == self.id_cliente_selecionado:
                        ent_nome.delete(0, tk.END)
                        ent_nome.insert(0, c["nome"])
                        ent_cpf.delete(0, tk.END)
                        ent_cpf.insert(0, c["cpf"])
                        ent_tel.delete(0, tk.END)
                        ent_tel.insert(0, c["telefone"])
                        ent_email.delete(0, tk.END)
                        ent_email.insert(0, c["email"])
                        ent_end.delete(0, tk.END)
                        ent_end.insert(0, c["endereco"])

        def deletar_cliente():
            if self.id_cliente_selecionado:
                self.BD_CLIENTES = [c for c in self.BD_CLIENTES if c["id"] != self.id_cliente_selecionado]
                self.id_cliente_selecionado = None
                limpar_campos()
                atualizar_tabela_clientes()
            else:
                messagebox.showwarning("Aviso", "Selecione um cliente na tabela primeiro.")

        def limpar_campos():
            self.id_cliente_selecionado = None
            ent_nome.delete(0, tk.END)
            ent_cpf.delete(0, tk.END)
            ent_tel.delete(0, tk.END)
            ent_email.delete(0, tk.END)
            ent_end.delete(0, tk.END)

        tabela.bind("<<TreeviewSelect>>", carregar_cliente)

        tk.Button(frame_dir, text="[F5] SALVAR/GRAVAR", font=("Courier New", 10, "bold"), bg=self.COR_SUCESSO, fg="#FFFFFF", command=salvar_cliente).pack(fill="x", padx=10, pady=4)
        tk.Button(frame_dir, text="[F6] EXCLUIR REGISTRO", font=("Courier New", 10, "bold"), bg=self.COR_PERIGO, fg="#FFFFFF", command=deletar_cliente).pack(fill="x", padx=10, pady=4)
        tk.Button(frame_dir, text="[F7] LIMPAR TELA", font=("Courier New", 10, "bold"), bg="#9CA3AF", fg="#000000", command=limpar_campos).pack(fill="x", padx=10, pady=4)

    # ==========================================
    # 3. CRUD MATERIAIS
    # ==========================================
    def tela_materiais(self):
        frame_esq = tk.Frame(self.container, bg="#F5F7FA")
        frame_esq.pack(side="left", fill="both", expand=True)

        frame_dir = tk.Frame(self.container, bg="#FFFFFF", bd=1, relief="solid", width=350)
        frame_dir.pack(side="right", fill="y", padx=(10, 0))
        frame_dir.pack_propagate(False)

        tk.Label(frame_esq, text="LISTA DE MATERIAIS CADASTRADOS", font=("Courier New", 12, "bold"), bg="#F5F7FA").pack(anchor="w")

        colunas = ("id", "nome", "preco", "unidade")
        tabela = ttk.Treeview(frame_esq, columns=colunas, show="headings")
        tabela.heading("id", text="ID")
        tabela.heading("nome", text="Descrição Material")
        tabela.heading("preco", text="Preço Unit.")
        tabela.heading("unidade", text="Unid.")
        tabela.column("id", width=40, anchor="center")
        tabela.column("nome", width=220)
        tabela.column("preco", width=100, anchor="e")
        tabela.column("unidade", width=60, anchor="center")
        tabela.pack(fill="both", expand=True, pady=5)

        def atualizar_tabela():
            for row in tabela.get_children():
                tabela.delete(row)
            for m in self.BD_MATERIAIS:
                tabela.insert("", "end", values=(m["id"], m["nome"], f"R$ {m['preco']:.2f}", m["unidade"]))
        atualizar_tabela()

        tk.Label(frame_dir, text=" FORMULÁRIO MATERIAL ", font=("Courier New", 12, "bold"), bg="#374151", fg="#FFFFFF").pack(fill="x", pady=(0, 10))

        tk.Label(frame_dir, text="Nome do Material:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_nome = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_nome.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Preço Unitário (R$):", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_preco = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_preco.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Unidade (ex: m, un, m²):", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_un = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_un.pack(fill="x", padx=10, pady=2)

        def salvar():
            try:
                preco_val = float(ent_preco.get().replace("R$", "").strip())
                if self.id_material_selecionado is None:
                    self.BD_MATERIAIS.append({"id": self.proximo_id_material, "nome": ent_nome.get(), "preco": preco_val, "unidade": ent_un.get(), "categoria": "Geral"})
                    self.proximo_id_material += 1
                else:
                    for m in self.BD_MATERIAIS:
                        if m["id"] == self.id_material_selecionado:
                            m.update({"nome": ent_nome.get(), "preco": preco_val, "unidade": ent_un.get()})
                limpar()
                atualizar_tabela()
            except ValueError:
                messagebox.showerror("Erro", "Insira um valor numérico válido para o preço.")

        def carregar(event):
            item = tabela.selection()
            if item:
                self.id_material_selecionado = int(tabela.item(item, "values")[0])
                for m in self.BD_MATERIAIS:
                    if m["id"] == self.id_material_selecionado:
                        ent_nome.delete(0, tk.END)
                        ent_nome.insert(0, m["nome"])
                        ent_preco.delete(0, tk.END)
                        ent_preco.insert(0, str(m["preco"]))
                        ent_un.delete(0, tk.END)
                        ent_un.insert(0, m["unidade"])

        def deletar():
            if self.id_material_selecionado:
                self.BD_MATERIAIS = [m for m in self.BD_MATERIAIS if m["id"] != self.id_material_selecionado]
                self.id_material_selecionado = None
                limpar()
                atualizar_tabela()

        def limpar():
            self.id_material_selecionado = None
            ent_nome.delete(0, tk.END)
            ent_preco.delete(0, tk.END)
            ent_un.delete(0, tk.END)

        tabela.bind("<<TreeviewSelect>>", carregar)
        tk.Button(frame_dir, text="[F5] SALVAR/GRAVAR", font=("Courier New", 10, "bold"), bg=self.COR_SUCESSO, fg="#FFFFFF", command=salvar).pack(fill="x", padx=10, pady=4)
        tk.Button(frame_dir, text="[F6] EXCLUIR REGISTRO", font=("Courier New", 10, "bold"), bg=self.COR_PERIGO, fg="#FFFFFF", command=deletar).pack(fill="x", padx=10, pady=4)
        tk.Button(frame_dir, text="[F7] LIMPAR TELA", font=("Courier New", 10, "bold"), bg="#9CA3AF", fg="#000000", command=limpar).pack(fill="x", padx=10, pady=4)

    # ==========================================
    # 4. CRUD METRAGENS
    # ==========================================
    def tela_metragens(self):
        frame_esq = tk.Frame(self.container, bg="#F5F7FA")
        frame_esq.pack(side="left", fill="both", expand=True)

        frame_dir = tk.Frame(self.container, bg="#FFFFFF", bd=1, relief="solid", width=350)
        frame_dir.pack(side="right", fill="y", padx=(10, 0))
        frame_dir.pack_propagate(False)

        tk.Label(frame_esq, text="LISTA DE METRAGENS MAPEADAS", font=("Courier New", 12, "bold"), bg="#F5F7FA").pack(anchor="w")

        colunas = ("id", "nome", "tamanho", "multiplicador")
        tabela = ttk.Treeview(frame_esq, columns=colunas, show="headings")
        tabela.heading("id", text="ID")
        tabela.heading("nome", text="Descrição de Escopo")
        tabela.heading("tamanho", text="Dimensão")
        tabela.heading("multiplicador", text="Fator Mult.")
        tabela.column("id", width=40, anchor="center")
        tabela.column("nome", width=180)
        tabela.column("tamanho", width=90, anchor="center")
        tabela.column("multiplicador", width=90, anchor="center")
        tabela.pack(fill="both", expand=True, pady=5)

        def atualizar_tabela():
            for row in tabela.get_children():
                tabela.delete(row)
            for m in self.BD_METRAGENS:
                tabela.insert("", "end", values=(m["id"], m["nome"], m["tamanho"], m["multiplicador"]))
        atualizar_tabela()

        tk.Label(frame_dir, text=" FORMULÁRIO METRAGEM ", font=("Courier New", 12, "bold"), bg="#374151", fg="#FFFFFF").pack(fill="x", pady=(0, 10))

        tk.Label(frame_dir, text="Descrição / Identificação:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_nome = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_nome.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Tamanho Previsto (ex: 20m²):", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_tam = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_tam.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Fator Multiplicador de Risco:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_mult = tk.Entry(frame_dir, font=("Courier New", 11), bd=1, relief="solid")
        ent_mult.insert(0, "1.0")
        ent_mult.pack(fill="x", padx=10, pady=2)

        def salvar():
            try:
                mult_val = float(ent_mult.get())
                if self.id_metragem_selecionado is None:
                    self.BD_METRAGENS.append({"id": self.proximo_id_metragem, "nome": ent_nome.get(), "tamanho": ent_tam.get(), "multiplicador": mult_val})
                    self.proximo_id_metragem += 1
                else:
                    for m in self.BD_METRAGENS:
                        if m["id"] == self.id_metragem_selecionado:
                            m.update({"nome": ent_nome.get(), "tamanho": ent_tam.get(), "multiplicador": mult_val})
                limpar()
                atualizar_tabela()
            except ValueError:
                messagebox.showerror("Erro", "Insira um multiplicador válido (ex: 1.0 ou 1.25).")

        def carregar(event):
            item = tabela.selection()
            if item:
                self.id_metragem_selecionado = int(tabela.item(item, "values")[0])
                for m in self.BD_METRAGENS:
                    if m["id"] == self.id_metragem_selecionado:
                        ent_nome.delete(0, tk.END)
                        ent_nome.insert(0, m["nome"])
                        ent_tam.delete(0, tk.END)
                        ent_tam.insert(0, m["tamanho"])
                        ent_mult.delete(0, tk.END)
                        ent_mult.insert(0, str(m["multiplicador"]))

        def deletar():
            if self.id_metragem_selecionado:
                self.BD_METRAGENS = [m for m in self.BD_METRAGENS if m["id"] != self.id_metragem_selecionado]
                self.id_metragem_selecionado = None
                limpar()
                atualizar_tabela()

        def limpar():
            self.id_metragem_selecionado = None
            ent_nome.delete(0, tk.END)
            ent_tam.delete(0, tk.END)
            ent_mult.delete(0, tk.END)
            ent_mult.insert(0, "1.0")

        tabela.bind("<<TreeviewSelect>>", carregar)
        tk.Button(frame_dir, text="[F5] SALVAR/GRAVAR", font=("Courier New", 10, "bold"), bg=self.COR_SUCESSO, fg="#FFFFFF", command=salvar).pack(fill="x", padx=10, pady=4)
        tk.Button(frame_dir, text="[F6] EXCLUIR REGISTRO", font=("Courier New", 10, "bold"), bg=self.COR_PERIGO, fg="#FFFFFF", command=deletar).pack(fill="x", padx=10, pady=4)
        tk.Button(frame_dir, text="[F7] LIMPAR TELA", font=("Courier New", 10, "bold"), bg="#9CA3AF", fg="#000000", command=limpar).pack(fill="x", padx=10, pady=4)

    # ==========================================
    # 5. TELA DE PROCESSAMENTO: ORÇAMENTOS 
    # ==========================================
    def tela_orcamentos(self):
        frame_esq = tk.Frame(self.container, bg="#F5F7FA")
        frame_esq.pack(side="left", fill="both", expand=True)

        frame_dir = tk.Frame(self.container, bg="#FFFFFF", bd=1, relief="solid", width=380)
        frame_dir.pack(side="right", fill="y", padx=(10, 0))
        frame_dir.pack_propagate(False)

        tk.Label(frame_esq, text="HISTÓRICO DE ORÇAMENTOS EMITIDOS", font=("Courier New", 12, "bold"), bg="#F5F7FA").pack(anchor="w")

        colunas = ("id", "cliente", "material", "total")
        tabela = ttk.Treeview(frame_esq, columns=colunas, show="headings")
        tabela.heading("id", text="Nº ORC")
        tabela.heading("cliente", text="Cliente")
        tabela.heading("material", text="Material Base")
        tabela.heading("total", text="Total Faturado")
        tabela.column("id", width=60, anchor="center")
        tabela.column("cliente", width=140)
        tabela.column("material", width=140)
        tabela.column("total", width=90, anchor="e")
        tabela.pack(fill="both", expand=True, pady=5)

        def atualizar_tabela():
            for row in tabela.get_children():
                tabela.delete(row)
            for o in self.BD_ORCAMENTOS:
                tabela.insert("", "end", values=(f"{o['id']:04d}", o["cliente"], o["material"], f"R$ {o['total']:.2f}"))
        atualizar_tabela()

        tk.Label(frame_dir, text=" OPERAÇÃO DE CAIXA / CÁLCULO ", font=("Courier New", 12, "bold"), bg=self.COR_PRIMARIA, fg="#FFFFFF").pack(fill="x", pady=(0, 10))

        tk.Label(frame_dir, text="Selecione o Cliente:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        lista_clientes = [c["nome"] for c in self.BD_CLIENTES]
        cb_cliente = ttk.Combobox(frame_dir, values=lista_clientes, state="readonly", font=("Courier New", 10))
        cb_cliente.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Selecione o Material:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        lista_materiais = [m["nome"] for m in self.BD_MATERIAIS]
        cb_material = ttk.Combobox(frame_dir, values=lista_materiais, state="readonly", font=("Courier New", 10))
        cb_material.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Selecione o Escopo/Metragem:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        lista_metragens = [m["nome"] for m in self.BD_METRAGENS]
        cb_metragens = ttk.Combobox(frame_dir, values=lista_metragens, state="readonly", font=("Courier New", 10))
        cb_metragens.pack(fill="x", padx=10, pady=2)

        tk.Label(frame_dir, text="Observações adicionais:", bg="#FFFFFF", font=("Courier New", 10, "bold")).pack(anchor="w", padx=10)
        ent_obs = tk.Entry(frame_dir, font=("Courier New", 10), bd=1, relief="solid")
        ent_obs.pack(fill="x", padx=10, pady=2)

        frame_total = tk.Frame(frame_dir, bg="#000000", bd=2, relief="sunken")
        frame_total.pack(fill="x", padx=10, pady=15)

        lbl_sub_tot = tk.Label(frame_total, text="TOTAL DO ORÇAMENTO", font=("Courier New", 10, "bold"), bg="#000000", fg="#22C55E")
        lbl_sub_tot.pack(pady=(5, 0))

        lbl_valor_grande = tk.Label(frame_total, text="R$ 0,00", font=("Courier New", 26, "bold"), bg="#000000", fg="#22C55E")
        lbl_valor_grande.pack(pady=5)

        def calcular_total_caixa():
            if not cb_material.get() or not cb_metragens.get():
                lbl_valor_grande.configure(text="R$ 0,00")
                return 0.0

            preco_base = next((m["preco"] for m in self.BD_MATERIAIS if m["nome"] == cb_material.get()), 0.0)
            fator_mult = next((m["multiplicador"] for m in self.BD_METRAGENS if m["nome"] == cb_metragens.get()), 1.0)

            subtotal = preco_base * fator_mult
            lbl_valor_grande.configure(text=f"R$ {subtotal:.2f}")
            return subtotal

        cb_material.bind("<<ComboboxSelected>>", lambda e: calcular_total_caixa())
        cb_metragens.bind("<<ComboboxSelected>>", lambda e: calcular_total_caixa())

        def fechar_cupom_orcamento():
            v_total = calcular_total_caixa()
            if v_total == 0 or not cb_cliente.get():
                messagebox.showwarning("Erro de Caixa", "Preencha Cliente, Material e Metragem para faturar.")
                return

            novo_orc = {
                "id": self.proximo_id_orcamento,
                "cliente": cb_cliente.get(),
                "material": cb_material.get(),
                "metragem": cb_metragens.get(),
                "total": v_total,
                "data": datetime.now().strftime("%d/%m/%Y"),
                "obs": ent_obs.get()
            }
            self.BD_ORCAMENTOS.append(novo_orc)
            self.proximo_id_orcamento += 1

            messagebox.showinfo("CONCLUÍDO", f"Orçamento número {novo_orc['id']:04d} emitido com sucesso!")
            cb_cliente.set("")
            cb_material.set("")
            cb_metragens.set("")
            ent_obs.delete(0, tk.END)
            lbl_valor_grande.configure(text="R$ 0,00")
            atualizar_tabela()

        def estornar_orcamento():
            item = tabela.selection()
            if item:
                id_orc = int(tabela.item(item, "values")[0])
                self.BD_ORCAMENTOS = [o for o in self.BD_ORCAMENTOS if o["id"] != id_orc]
                atualizar_tabela()
            else:
                messagebox.showwarning("Aviso", "Selecione o cupom na lista para estornar.")

        tk.Button(frame_dir, text="[F5] EMITIR/FECHAR CUPOM", font=("Courier New", 11, "bold"), bg=self.COR_SUCESSO, fg="#FFFFFF", command=fechar_cupom_orcamento).pack(fill="x", padx=10, pady=4)
        tk.Button(frame_dir, text="[F6] ESTORNAR CUPOM", font=("Courier New", 11, "bold"), bg=self.COR_PERIGO, fg="#FFFFFF", command=estornar_orcamento).pack(fill="x", padx=10, pady=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaCaixaIFRN(root)
    root.mainloop()
