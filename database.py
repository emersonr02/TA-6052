# -*- coding: utf-8 -*-
# database.py
import json
import os
import dados  

NOME_ARQUIVO = "banco.json"

def salvar_dados(sistema_completo):
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(sistema_completo, f, indent=4, ensure_ascii=False)
        print("\n[Sistema] Dados guardados.")
    except Exception as e:
        print(f"\n[Erro] Falha ao salvar: {e}")

def carregar_dados():
    if not os.path.exists(NOME_ARQUIVO):
        return None 
    
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)