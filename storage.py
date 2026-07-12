import json
import os
import shutil
from datetime import datetime

PASTA_BACKUPS = "backups"
QUANTIDADE_BACKUPS_MANTIDOS = 5

def _garantir_pasta_do_arquivo(caminho):
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    os.makedirs(PASTA_BACKUPS, exist_ok=True)

def _caminho_completo(nome_arquivo):
    _garantir_pasta_do_arquivo(nome_arquivo)
    return nome_arquivo

def _nome_backup_base(caminho):
    return caminho.replace(os.sep, "_").replace("/", "_")

def criar_backup(caminho):
    if not os.path.exists(caminho):
        return None
    _garantir_pasta_do_arquivo(caminho)
    nome_base = _nome_backup_base(caminho)
    agora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_backup = f"{nome_base}.{agora}.bak"
    caminho_backup = os.path.join(PASTA_BACKUPS, nome_backup)
    try:
        shutil.copy2(caminho, caminho_backup)
        _limpar_backups_antigos(nome_base)
        return caminho_backup
    except OSError:
        return None

def _limpar_backups_antigos(nome_base, manter=QUANTIDADE_BACKUPS_MANTIDOS):
    try:
        backups = [
            nome for nome in os.listdir(PASTA_BACKUPS)
            if nome.startswith(nome_base + ".")
        ]
        backups.sort(reverse=True)
        for antigo in backups[manter:]:
            os.remove(os.path.join(PASTA_BACKUPS, antigo))
    except OSError:
        pass

def _backup_mais_recente(nome_base):
    if not os.path.isdir(PASTA_BACKUPS):
        return None
    backups = [
        nome for nome in os.listdir(PASTA_BACKUPS)
        if nome.startswith(nome_base + ".") and "CORROMPIDO" not in nome
    ]
    if not backups:
        return None
    backups.sort(reverse=True)
    return os.path.join(PASTA_BACKUPS, backups[0])

def salvar_json(nome_arquivo, dados):
    caminho = _caminho_completo(nome_arquivo)
    criar_backup(caminho)
    caminho_temporario = caminho + ".tmp"
    try:
        with open(caminho_temporario, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        os.replace(caminho_temporario, caminho)
        return True
    except (OSError, TypeError):
        if os.path.exists(caminho_temporario):
            os.remove(caminho_temporario)
        return False

def carregar_json(nome_arquivo, valor_padrao=None):
    if valor_padrao is None:
        valor_padrao = []
    caminho = _caminho_completo(nome_arquivo)
    if not os.path.exists(caminho):
        return valor_padrao
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return tratar_arquivo_corrompido(caminho, valor_padrao)
    except OSError:
        return valor_padrao

def tratar_arquivo_corrompido(caminho, valor_padrao=None):
    if valor_padrao is None:
        valor_padrao = []
    _garantir_pasta_do_arquivo(caminho)
    nome_base = _nome_backup_base(caminho)
    agora = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho_corrompido = os.path.join(PASTA_BACKUPS, f"{nome_base}.CORROMPIDO.{agora}")
    try:
        if os.path.exists(caminho):
            shutil.copy2(caminho, caminho_corrompido)
    except OSError:
        pass
    caminho_backup = _backup_mais_recente(nome_base)
    if caminho_backup:
        try:
            with open(caminho_backup, "r", encoding="utf-8") as arquivo:
                dados_recuperados = json.load(arquivo)
            shutil.copy2(caminho_backup, caminho)
            return dados_recuperados
        except (OSError, json.JSONDecodeError):
            pass
    return valor_padrao
