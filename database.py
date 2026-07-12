import os

import storage
from calculos import Metragem
from models.cliente import Cliente
from models.material import Material
from models.orcamento import Orcamento

ARQUIVO_CLIENTES = os.path.join("clientes", "clientes.json")
ARQUIVO_MATERIAIS = os.path.join("materiais", "materiais.json")
ARQUIVO_ORCAMENTOS = os.path.join("orcamentos", "orcamentos.json")
ARQUIVO_MEDIDAS = os.path.join("medidas", "medidas.json")

def _cliente_para_dict(cliente):
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "telefone": cliente.telefone,
        "email": cliente.email,
        "arquivado": cliente.arquivado,
    }

def _dict_para_cliente(dado):
    cliente = Cliente(dado["id"], dado["nome"], dado["telefone"], dado["email"])
    cliente.arquivado = dado.get("arquivado", False)
    return cliente

def salvar_clientes(clientes, clientes_arquivados=None):
    clientes_arquivados = clientes_arquivados or []
    dados = {
        "ativos": [_cliente_para_dict(c) for c in clientes],
        "arquivados": [_cliente_para_dict(c) for c in clientes_arquivados],
    }
    return storage.salvar_json(ARQUIVO_CLIENTES, dados)

def carregar_clientes():
    padrao = {"ativos": [], "arquivados": []}
    dados = storage.carregar_json(ARQUIVO_CLIENTES, padrao)
    ativos = [_dict_para_cliente(d) for d in dados.get("ativos", [])]
    arquivados = [_dict_para_cliente(d) for d in dados.get("arquivados", [])]
    return ativos, arquivados

def _material_para_dict(material):
    return {"nome": material.nome, "preco_m2": material.preco_m2}

def _dict_para_material(dado):
    return Material(dado["nome"], dado["preco_m2"])

def salvar_materiais(materiais):
    dados = [_material_para_dict(m) for m in materiais]
    return storage.salvar_json(ARQUIVO_MATERIAIS, dados)

def carregar_materiais():
    dados = storage.carregar_json(ARQUIVO_MATERIAIS, [])
    return [_dict_para_material(d) for d in dados]

def _orcamento_para_dict(orcamento):
    return {
        "cliente": orcamento.cliente,
        "descricao": orcamento.descricao,
        "material_nome": orcamento.material.nome,
        "quantidade": orcamento.quantidade,
        "area": orcamento.area,
        "montagem": orcamento.montagem,
        "taxa_cartao": orcamento.taxa_cartao,
        "observacao": orcamento.observacao,
    }

def _dict_para_orcamento(dado, materiais_disponiveis):
    material = next((m for m in materiais_disponiveis if m.nome == dado["material_nome"]), None)
    if material is None:
        material = Material(dado["material_nome"], 0.0)
    return Orcamento(
        dado["cliente"],
        dado["descricao"],
        material,
        dado["quantidade"],
        dado["area"],
        dado["montagem"],
        dado["taxa_cartao"],
        dado["observacao"],
    )

def salvar_orcamentos(orcamentos):
    dados = [_orcamento_para_dict(o) for o in orcamentos]
    return storage.salvar_json(ARQUIVO_ORCAMENTOS, dados)

def carregar_orcamentos(materiais_disponiveis):
    dados = storage.carregar_json(ARQUIVO_ORCAMENTOS, [])
    return [_dict_para_orcamento(d, materiais_disponiveis) for d in dados]

def _medida_para_dict(medida):
    return {
        "descricao": medida._Metragem__descricao,
        "largura": medida._Metragem__largura,
        "comprimento": medida._Metragem__comprimento,
    }

def _dict_para_medida(dado):
    return Metragem(dado["descricao"], dado["largura"], dado["comprimento"])

def salvar_medidas(medidas):
    dados = [_medida_para_dict(m) for m in medidas]
    return storage.salvar_json(ARQUIVO_MEDIDAS, dados)

def carregar_medidas():
    dados = storage.carregar_json(ARQUIVO_MEDIDAS, [])
    return [_dict_para_medida(d) for d in dados]

if __name__ == "__main__":
    m1 = Material("MDF 15mm", 120.0)
    m2 = Material("Compensado 10mm", 80.0)
    salvar_materiais([m1, m2])
    materiais_carregados = carregar_materiais()
    c1 = Cliente(1, "João Silva", "(11) 99999-0000", "joao@email.com")
    salvar_clientes([c1])
    ativos, arquivados = carregar_clientes()
    orc = Orcamento("João Silva", "Móvel sob medida", m1, 3, 2.5, 150.0, 3.5, "Entregar dia 20")
    salvar_orcamentos([orc])
    orcamentos_carregados = carregar_orcamentos(materiais_carregados)
    medida = Metragem("Prateleira sala", 1.2, 0.4)
    salvar_medidas([medida])
    medidas_carregadas = carregar_medidas()
