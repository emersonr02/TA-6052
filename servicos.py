# -*- coding: utf-8 -*-
# servicos.py
from datetime import datetime
import dados

# --- Autenticacao ---
def loginAdmin():
    print("\n--- Login Administrador ---")
    username = input("Usuario: ")
    password = input("Senha: ")
    return username == "admin" and password == "admin"

def loginUtilizador():
    print("\n--- Login Utilizador ---")
    nib = input("Digite seu NIB: ")
    if nib not in dados.clientes or not dados.clientes[nib]["Ativo"]:
        print("NIB inexistente ou conta desativada.")
        return None
    
    password = input("Digite sua senha: ")
    if password == dados.clientes[nib]["senha"]:
        print(f"Bem-vindo, {dados.clientes[nib]['nome']}!")
        return nib
    print("Senha incorreta.")
    return None

# --- Sistema de Registo ---
def registrarMovimentacao(nib, tipo, valor, destino=None):
    id_formatado = f"M{dados.contadorMovimentos:03d}"
    
    novo_movimento = {
        "tipo": tipo,
        "valor": valor,
        "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "remetente": nib,
        "destinatario": destino if destino else "N/A"
    }
    
    dados.regtransferencias[id_formatado] = novo_movimento
    dados.clientes[nib]["Movimentos"].append(id_formatado)
    
    if destino and destino in dados.clientes:
        dados.clientes[destino]["Movimentos"].append(id_formatado)
        
    dados.contadorMovimentos += 1

# --- Operacoes de Conta ---
def consultarSaldo(meuNIB):
    print(f"\nSaldo atual de {dados.clientes[meuNIB]['nome']}: {dados.clientes[meuNIB]['saldo']:.2f}EUR")

def realizarLevantamento(meuNIB):
    try:
        valor = float(input("Valor a levantar: "))
        if 0 < valor <= dados.clientes[meuNIB]["saldo"]:
            dados.clientes[meuNIB]["saldo"] -= valor
            registrarMovimentacao(meuNIB, "Levantamento", valor)
            print("Levantamento concluido!")
        else:
            print("Saldo insuficiente ou valor invalido.")
    except ValueError:
        print("Erro: Digite um numero valido.")

def realizarDeposito(meuNIB):
    print("\n--- Realizar Deposito Automatico ---")
    try:
        valor = int(input("Digite o valor total a depositar (notas de 5, 10, 20, 50): "))
        
        if valor <= 0 or valor % 5 != 0:
            print("Erro: O valor deve ser positivo e multiplo de 5EUR (notas disponiveis).")
            return

        valor_restante = valor
        notas_processadas = {}
        denominacoes = [50, 20, 10, 5]

        for nota in denominacoes:
            quantidade_notas = valor_restante // nota
            if quantidade_notas > 0:
                notas_processadas[str(nota)] = quantidade_notas
                valor_restante %= nota

        dados.clientes[meuNIB]["saldo"] += valor
        
        for nota_str, qtd in notas_processadas.items():
            dados.stock_notas[nota_str] += qtd
        
        registrarMovimentacao(meuNIB, "Deposito", valor)

        print(f"\nSucesso! Deposito de {valor}EUR processado.")
        print("Notas detectadas e guardadas no cofre:")
        for n, q in notas_processadas.items():
            print(f"- {q} nota(s) de {n}EUR")
        
        print(f"Novo saldo: {dados.clientes[meuNIB]['saldo']:.2f}EUR")

    except ValueError:
        print("Erro: Insira um valor numerico inteiro.")

def realizarTransferencia(meuNIB):
    destinatario = input("NIB do destinatario: ")
    if destinatario not in dados.clientes or not dados.clientes[destinatario]["Ativo"]:
        print("Destinatario invalido ou inativo.")
        return
    
    if destinatario == meuNIB:
        print("Nao pode transferir para si mesmo.")
        return

    else:

        try:
            valor = float(input("Valor a transferir: "))
            if 0 < valor <= dados.clientes[meuNIB]["saldo"]:
                dados.clientes[meuNIB]["saldo"] -= valor
                dados.clientes[destinatario]["saldo"] += valor
                registrarMovimentacao(meuNIB, "Transferencia", valor, destino=destinatario)
                print("Transferencia enviada com sucesso!")
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Erro: Digite um numero valido.")

def consultarMovimentos(meuNIB):
    print(f"\n--- Extrato de Conta: {meuNIB} ---")
    if not dados.clientes[meuNIB]["Movimentos"]:
        print("Nao existem movimentos registados.")
        return
    
    for id_mov in dados.clientes[meuNIB]["Movimentos"]:
        m = dados.regtransferencias.get(id_mov)
        if m:
            # Removido acento de 'destinatario' aqui tambem
            print(f"[{m['data']}] {m['tipo']:<15} | {m['valor']:>7.2f}EUR | Dest: {m['destinatario']}")

# --- Operacoes Administrativas ---
def criarCliente():
    nome = input("Nome do cliente: ")
    senha = input("Senha: ")
    novo_nib = f"PT{dados.contadorNIB}"
    dados.clientes[novo_nib] = {
        "nome": nome, 
        "senha": senha, 
        "saldo": 1000.0, 
        "Movimentos": [], 
        "Ativo": True
    }
    print(f"Cliente criado com sucesso! NIB: {novo_nib}")
    dados.contadorNIB += 1

def listarClientes():
    print("\n--- Listagem de Clientes ---")
    for nib, info in dados.clientes.items():
        status = "ATIVO" if info["Ativo"] else "INATIVO"
        print(f"NIB: {nib} | Nome: {info['nome']:<10} | Saldo: {info['saldo']:>8.2f}EUR | {status}")

def pesquisarMovimentacao():
    id_m = input("Digite o ID da movimentacao (ex: M001): ").upper()
    m = dados.regtransferencias.get(id_m)
    if m:
        print(f"\nDetalhes da Movimentacao {id_m}:")
        for chave, valor in m.items():
            print(f"{chave.capitalize()}: {valor}")
    else:
        print("Movimentacao nao encontrada.")

def apagarCliente():
    nib = input("Digite o NIB do cliente a desativar: ")
    if nib in dados.clientes and dados.clientes[nib]["Ativo"]:
        confirmar = input(f"Tem certeza que deseja desativar {dados.clientes[nib]['nome']}? (s/n): ")
        if confirmar.lower() == 's':
            dados.clientes[nib]["Ativo"] = False
            print("Conta desativada com sucesso.")
    else:
        print("Cliente nao encontrado ou ja esta inativo.")

def verEstatisticas():
    ativos = [c for c in dados.clientes.values() if c["Ativo"]]
    total_dinheiro = sum(c["saldo"] for c in ativos)
    
    print("\n=== ESTATISTICAS DO BANCO ===")
    print(f"Total de Clientes Ativos: {len(ativos)}")
    print(f"Volume Total de Depositos: {total_dinheiro:.2f}EUR")
    
    print("\n--- Stock de Notas no ATM ---")
    caixa_total = 0
    for nota, qtd in dados.stock_notas.items():
        subtotal = int(nota) * qtd
        caixa_total += subtotal
        print(f"Notas de {nota:^2}EUR: {qtd:^3} unidades | Total: {subtotal:>5}EUR")
    print(f"Total fisico em caixa: {caixa_total}EUR")