"""
storage.py

Motor genérico de persistência em JSON.

Responsável por:
- Salvar dados em arquivos JSON (salvar_json)
- Carregar dados de arquivos JSON (carregar_json)
- Detectar e tratar arquivos corrompidos (tratar_arquivo_corrompido)
- Manter backups automáticos antes de cada gravação

Este módulo não conhece as classes do projeto (Cliente, Material, etc).
Ele trabalha apenas com estruturas simples (listas e dicionários), para
poder ser reaproveitado por qualquer parte do sistema.
"""

import json 
import os 
import shutil 
from datetime import datetime 


PASTA_BACKUPS ="backups"

QUANTIDADE_BACKUPS_MANTIDOS =5 


def _garantir_pasta_do_arquivo (caminho ):
    """Cria a pasta do arquivo (se houver) e a pasta de backups."""
    pasta =os .path .dirname (caminho )
    if pasta :
        os .makedirs (pasta ,exist_ok =True )
    os .makedirs (PASTA_BACKUPS ,exist_ok =True )


def _caminho_completo (nome_arquivo ):
    """
    Cada parte do sistema já tem sua própria pasta no projeto
    (ex: 'materiais/materiais.json', 'orcamentos/orcamentos.json').
    Essa função apenas repassa o caminho recebido, garantindo que
    a pasta de destino exista.
    """
    _garantir_pasta_do_arquivo (nome_arquivo )
    return nome_arquivo 


def _nome_backup_base (caminho ):
    """
    Gera um identificador de backup a partir do caminho do arquivo,
    trocando separadores de pasta por '_' (ex: 'materiais/materiais.json'
    vira 'materiais_materiais.json'), já que todos os backups ficam
    juntos numa única pasta 'backups/' na raiz do projeto.
    """
    return caminho .replace (os .sep ,"_").replace ("/","_")


def criar_backup (caminho ):
    """
    Cria uma cópia de segurança (backup) do arquivo informado,
    com data e hora no nome, antes que ele seja sobrescrito.

    Retorna o caminho do backup criado, ou None se não havia
    arquivo para copiar ou se algo deu errado.
    """
    if not os .path .exists (caminho ):
        return None 

    _garantir_pasta_do_arquivo (caminho )

    nome_base =_nome_backup_base (caminho )
    agora =datetime .now ().strftime ("%Y%m%d_%H%M%S")
    nome_backup =f"{nome_base }.{agora }.bak"
    caminho_backup =os .path .join (PASTA_BACKUPS ,nome_backup )

    try :
        shutil .copy2 (caminho ,caminho_backup )
        _limpar_backups_antigos (nome_base )
        return caminho_backup 

    except OSError as erro :
        print (f"Aviso: não foi possível criar backup de '{caminho }': {erro }")
        return None 


def _limpar_backups_antigos (nome_base ,manter =QUANTIDADE_BACKUPS_MANTIDOS ):
    """Mantém apenas os backups mais recentes de um arquivo, apagando o resto."""
    try :
        backups =[
        nome for nome in os .listdir (PASTA_BACKUPS )
        if nome .startswith (nome_base +".")
        ]
        backups .sort (reverse =True )

        for antigo in backups [manter :]:
            os .remove (os .path .join (PASTA_BACKUPS ,antigo ))

    except OSError :
        pass 


def _backup_mais_recente (nome_base ):
    """Retorna o caminho do backup mais recente de um arquivo, se existir."""
    if not os .path .isdir (PASTA_BACKUPS ):
        return None 

    backups =[
    nome for nome in os .listdir (PASTA_BACKUPS )
    if nome .startswith (nome_base +".")and "CORROMPIDO"not in nome 
    ]

    if not backups :
        return None 

    backups .sort (reverse =True )
    return os .path .join (PASTA_BACKUPS ,backups [0 ])


def salvar_json (nome_arquivo ,dados ):
    """
    Salva 'dados' (lista ou dicionário) no arquivo JSON indicado por
    'nome_arquivo' (ex: 'materiais/materiais.json').

    Antes de sobrescrever o arquivo existente, um backup automático
    é criado. A escrita é feita em um arquivo temporário e só depois
    renomeada para o nome final, evitando que o arquivo original seja
    corrompido caso o programa seja fechado no meio da gravação.

    Retorna True em caso de sucesso e False em caso de erro.
    """
    caminho =_caminho_completo (nome_arquivo )

    criar_backup (caminho )

    caminho_temporario =caminho +".tmp"

    try :
        with open (caminho_temporario ,"w",encoding ="utf-8")as arquivo :
            json .dump (dados ,arquivo ,ensure_ascii =False ,indent =4 )

        os .replace (caminho_temporario ,caminho )
        return True 

    except (OSError ,TypeError )as erro :
        print (f"Erro ao salvar '{caminho }': {erro }")

        if os .path .exists (caminho_temporario ):
            os .remove (caminho_temporario )

        return False 


def carregar_json (nome_arquivo ,valor_padrao =None ):
    """
    Carrega os dados de um arquivo JSON.

    - Se o arquivo não existir, retorna 'valor_padrao' (sistema "novo").
    - Se o arquivo existir mas estiver corrompido, aciona
      tratar_arquivo_corrompido() para tentar recuperar os dados.
    """
    if valor_padrao is None :
        valor_padrao =[]

    caminho =_caminho_completo (nome_arquivo )

    if not os .path .exists (caminho ):
        return valor_padrao 

    try :
        with open (caminho ,"r",encoding ="utf-8")as arquivo :
            return json .load (arquivo )

    except json .JSONDecodeError :
        print (f"Arquivo '{caminho }' está corrompido. Tentando recuperar...")
        return tratar_arquivo_corrompido (caminho ,valor_padrao )

    except OSError as erro :
        print (f"Erro ao acessar '{caminho }': {erro }")
        return valor_padrao 


def tratar_arquivo_corrompido (caminho ,valor_padrao =None ):
    """
    Trata um arquivo JSON corrompido, na seguinte ordem:

    1. Guarda uma cópia do arquivo corrompido (para possível análise depois).
    2. Tenta restaurar o backup automático mais recente e válido.
    3. Se nenhum backup puder ser lido, devolve 'valor_padrao' e o sistema
       recomeça com os dados vazios em vez de travar.
    """
    if valor_padrao is None :
        valor_padrao =[]

    _garantir_pasta_do_arquivo (caminho )

    nome_base =_nome_backup_base (caminho )
    agora =datetime .now ().strftime ("%Y%m%d_%H%M%S")
    caminho_corrompido =os .path .join (
    PASTA_BACKUPS ,f"{nome_base }.CORROMPIDO.{agora }"
    )

    try :
        if os .path .exists (caminho ):
            shutil .copy2 (caminho ,caminho_corrompido )
            print (f"Cópia do arquivo corrompido guardada em: {caminho_corrompido }")
    except OSError :
        pass 

    caminho_backup =_backup_mais_recente (nome_base )

    if caminho_backup :
        try :
            with open (caminho_backup ,"r",encoding ="utf-8")as arquivo :
                dados_recuperados =json .load (arquivo )

            shutil .copy2 (caminho_backup ,caminho )
            print (f"Dados restaurados a partir do backup: {caminho_backup }")
            return dados_recuperados 

        except (OSError ,json .JSONDecodeError ):
            print ("O backup mais recente também está corrompido.")

    print ("Nenhum backup válido encontrado. Iniciando com dados vazios.")
    return valor_padrao 
