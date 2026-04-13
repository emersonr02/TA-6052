# interface.py

def menuInicial():
    print("\n=== BANCO TAL (Portugal) ===")
    print("1 - Entrar como utilizador")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def menuUtilizador():
    print("\n--- Menu do Usuário ---")
    print("1. Consultar Saldo | 2. Levantamento | 3. Depósito")
    print("4. Transferência   | 5. Movimentações | 6. Sair")
    return input("Opção: ")

def menuAdmin():
    print("\n--- Menu Admin ---")
    print("1. Criar Cliente | 2. Listar Clientes | 3. Pesquisar Movimento")
    print("4. Apagar Cliente | 5. Estatísticas    | 6. Sair")
    return input("Opção: ")