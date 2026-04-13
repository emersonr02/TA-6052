# -*- coding: utf-8 -*-
# interface.py

def menuInicial():
    print("\n=== BANCO TAL (Portugal) ===")
    print("1 - Entrar como utilizador")
    print("0 - Sair")
    return input("Escolha uma opcao: ")

def menuUtilizador():
    print("\n--- Menu do Usuario ---")
    print("1. Consultar Saldo | 2. Levantamento | 3. Deposito")
    print("4. Transferencia   | 5. Movimentacoes | 6. Sair")
    return input("Opcao: ")

def menuAdmin():
    print("\n--- Menu Admin ---")
    print("1. Criar Cliente | 2. Listar Clientes | 3. Pesquisar Movimento")
    print("4. Apagar Cliente | 5. Estatisticas    | 6. Sair")
    return input("Opcao: ")