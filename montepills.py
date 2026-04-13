from datetime import datetime

clientes = {
    "PT5000": {"nome": "Emerson", "senha": "1234", "saldo": 1000, "Movimentos": [00001], "Ativo": True},
    "PT5001": {"nome": "João", "senha": "5678", "saldo": 500, "Movimentos": [00001] "Ativo": True}
    }
contadorNIB = 2
regtransferencias = {
    "M00001": {"tipo": "transferência", "remetente": "PT5000", "destinatário": "PT5001", "valor": 100, "data": "2024-06-01"}
    }
contadorMovimentacao = 2
def loginAdmin():
    print("Bem-vindo ao sistema de login!")
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    # Simulação de verificação de credenciais
    if username == "admin" and password == "senha123":
        print("Login bem-sucedido! Bem-vindo, admin.")
    else:
        print("Credenciais inválidas. Tente novamente.")

def loginUtilizador():
    nib = input("Digite seu NIB: ")
    if nib not in clientes:
        print("NIB não encontrado.")
        return None
    
    password = input("Digite sua senha: ")
    if password == clientes[nib]["senha"]:
        return nib
    else:
        print("Senha incorreta.")
        return None

def menuInicial():
    print("Bem-vindo ao Banco Tal!")
    print("1 - Entrar como utilizador")
    print("9958 - Entrar como Administrador")
    op = input("Escolha uma opção: ")
    return op

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

def consultarSaldo(meuNIB):
    print("\n--- Consultar Saldo ---")
    print(f"Saldo atual: {clientes[meuNIB]['saldo']}€")
    return

def realizarLevantamento(meuNIB):
    print("\n--- Realizar Levantamento ---")
    try:
        valor = float(input("Digite o valor a ser levantado: "))
        if valor <= 0:
            print("Valor deve ser maior que zero.")
            return

        if valor <= clientes[meuNIB]["saldo"]: 
            clientes[meuNIB]["saldo"] -= valor
            registrarMovimentacao(meuNIB, "Levantamento", valor)
            print("Operação realizada com sucesso!")
        else:
            print("Saldo insuficiente.")
            
        print(f"Saldo atual: {clientes[meuNIB]['saldo']}€")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

def realizarDeposito(meuNIB):
    print("\n--- Realizar Deposito ---")
    try:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor <= 0:
            print("Valor deve ser maior que zero.")
            return

        if valor <= clientes[meuNIB]["saldo"]: 
            clientes[meuNIB]["saldo"] += valor 
            registrarMovimentacao(meuNIB, "deposito", valor)
            print("Operação realizada com sucesso!")
        else:
            print("Saldo insuficiente.")
            
        print(f"Saldo atual: {clientes[meuNIB]['saldo']}€")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
    registrarMovimentacao(meuNIB, "Depósito", valor)

def registrarMovimentacao(nib, tipo, valor, destino=None):
    global contadorMovimentos
    
    # 1. Criar o registro detalhado
    novo_movimento = {
        "tipo": tipo,
        "valor": valor,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "remetente": nib,
        "destinatário": destino if destino else "N/A"
    }
    
    # 2. Guardar no histórico geral do banco
    regtransferencias[contadorMovimentos] = novo_movimento
    
    # 3. Adicionar o ID à lista de movimentos do cliente específico
    clientes[nib]["Movimentos"].append(contadorMovimentos)
    if destino != None:
        clientes[destino]["Movimentos"].append(contadorMovimentos)
    # 4. Incrementar para o próximo ID não se repetir
    contadorMovimentos += 1

def consultarMovimentos()
    print("\n--- Consultar Movimentações ---")
    for id_movimento in clientes[meuNIB]["Movimentos"]:
        movimento = regtransferencias.get(id_movimento)
        if movimento:
            print(f"ID: {id_movimento} | Tipo: {movimento['tipo']} | Valor: {movimento['valor']}€ | Data: {movimento['data']} | Remetente: {movimento['remetente']} | Destinatário: {movimento['destinatário']}")

def realizarTransferencia(meuNIB):
    print("\n--- Realizar Transferência ---")
    destinatario = input("Digite o NIB do destinatário: ")
    
    if destinatario not in clientes:
        print("NIB do destinatário não encontrado.")
        return
    
    try:
        valor = float(input("Digite o valor a ser transferido: "))
        if valor <= 0:
            print("Valor deve ser maior que zero.")
            return
        if valor <= clientes[meuNIB]["saldo"]:
            clientes[meuNIB]["saldo"] -= valor
            clientes[destinatario]["saldo"] += valor
            registrarMovimentacao(meuNIB, "Transferência", valor, destino=destinatario)
            print("Transferência realizada com sucesso!")
        else:
            print("Saldo insuficiente.")
            
        print(f"Saldo atual: {clientes[meuNIB]['saldo']}€")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

def criarCliente():
    print("\n--- Criar Cliente ---")
    nome = input("Digite o nome do cliente: ")
    senha = input("Digite a senha do cliente: ")
    saldo_inicial = 1000  # Saldo inicial padrão para novos clientes
    
    global contadorNIB
    contadorNIB = str(int(contadorNIB) + 1).zfill(4)  # Incrementa e formata o NIB
    novo_nib = "PT" + contadorNIB
    
    clientes[novo_nib] = {
        "nome": nome,
        "senha": senha,
        "saldo": saldo_inicial,
        "Movimentos": []
    }
    
    print(f"Cliente criado com sucesso! NIB: {novo_nib}")

def listarClientes():
    print("\n--- Lista de Clientes ---")
    for nib, info in clientes.items():
        print(f"NIB: {nib} | Nome: {info['nome']} | Saldo: {info['saldo']}€")

def pesquisarMovimentacao():
    print("\n --- Pesquisaq de Movimentações")
    id_movimento = int(input("Digite a movimentação que deseja procurar: "))
    if id_movimento not in regtransferencias:
        print ("movimentação não existente!")
        return
    else:
         print(f"ID: {id_movimento} | Tipo: {movimento['tipo']} | Valor: {movimento['valor']}€ | Data: {movimento['data']} | Remetente: {movimento['remetente']} | Destinatário: {movimento['destinatário']}")

def apagarCliente():
    print("\n--- Apagar Cliente ---")
    try: 
        nib = input("Digite o NIB do cliente")
        if nib in clientes && clientes[nib]["Ativo"] == True:
            op = int(input(f"Deseja apagar o cliente {clientes[nib]["nome"]} | NIB: {nib}? (1 - Sim 0 - Não)"))
            if op = 0:
                print("Operação Cancelada!")
            if op = 1:
                clientes[nib][Ativo] = False
                print("Operação Finalizada!")
            else:
                print("Opção inválida")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

def estatistica():
    

    
