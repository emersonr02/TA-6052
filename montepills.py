clientes = {
    "PT5000": {"nome": "Emerson", "senha": "1234", "saldo": 1000, "Movimentos": [00001]},
    "PT5001": {"nome": "João", "senha": "5678", "saldo": 500, "Movimentos": [00001]}
    }
contadorNIB = "02"
regtransferencias = {
    00001: {"tipo": "transferência", "remetente": "PT5000", "destinatário": "PT5001", "valor": 100, "data": "2024-06-01"}
    }
def loginUtilizador():
    print("Bem-vindo ao sistema de login!")
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    # Simulação de verificação de credenciais
    if username == "admin" and password == "senha123":
        print("Login bem-sucedido! Bem-vindo, admin.")
    else:
        print("Credenciais inválidas. Tente novamente.")

def menuUtilizador():
    print("\n--- Menu do Usuário ---")
    print("1. Consultar Saldo")
    print("2. Realizar levantamento")
    print("3. Realizar depósito")
    print("4. Realizar transferência")
    print("5. Consultar movimentações")
    print("6. Sair")
    op = input("Escolha uma opção: ")
    return op

def menuAdmin():
    print("\n--- Menu do Administrador ---")
    print("1. Criar Cliente")
    print("2. Listar Clientes")
    print("3. Listar/pesquisar movimentações")
    print("4. Apagar cliente")
    print("5. Estatísticas")
    print("6. Sair")
    op = input("Escolha uma opção: ")
    return op

def consultarSaldo():
    print("\n--- Consultar Saldo ---")
    NIB = input("Digite o NIB do cliente: ")
    try :
        NIB = int(NIB)
        for i in clientes
            if i == NIB
            saldo = clientes[NIB]["saldo"]
            print(f"O saldo do cliente {clientes[NIB]['nome']} é: {saldo} euros.")
            else:
                print("NIB não encontrado. Tente novamente.")
    except ValueError:
        print("NIB inválido. Tente novamente.")
