# servicos.py
from datetime import datetime
import dados

def loginAdmin():
    print("\n--- Login Administrador ---")
    username = input("Usuário: ")
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

def registrarMovimentacao(nib, tipo, valor, destino=None):
    id_formatado = f"M{dados.contadorMovimentos:03d}"
    
    novo_movimento = {
        "tipo": tipo,
        "valor": valor,
        "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "remetente": nib,
        "destinatário": destino if destino else "N/A"
    }
    
    dados.regtransferencias[id_formatado] = novo_movimento
    dados.clientes[nib]["Movimentos"].append(id_formatado)
    
    if destino and destino in dados.clientes:
        dados.clientes[destino]["Movimentos"].append(id_formatado)
        
    dados.contadorMovimentos += 1

def realizarLevantamento(meuNIB):
    try:
        valor = float(input("Valor a levantar: "))
        if 0 < valor <= dados.clientes[meuNIB]["saldo"]:
            dados.clientes[meuNIB]["saldo"] -= valor
            registrarMovimentacao(meuNIB, "Levantamento", valor)
            print("Levantamento concluído!")
        else:
            print("Saldo insuficiente ou valor inválido.")
    except ValueError:
        print("Erro: Digite um número.")

def realizarTransferencia(meuNIB):
    destinatario = input("NIB do destinatário: ")
    if destinatario not in dados.clientes or not dados.clientes[destinatario]["Ativo"]:
        print("Destinatário inválido.")
        return
    try:
        valor = float(input("Valor a transferir: "))
        if 0 < valor <= dados.clientes[meuNIB]["saldo"]:
            dados.clientes[meuNIB]["saldo"] -= valor
            dados.clientes[destinatario]["saldo"] += valor
            registrarMovimentacao(meuNIB, "Transferência", valor, destino=destinatario)
            print("Transferência enviada!")
        else:
            print("Saldo insuficiente.")
    except ValueError:
        print("Erro: Digite um número.")

def criarCliente():
    nome = input("Nome do cliente: ")
    senha = input("Senha: ")
    novo_nib = f"PT{dados.contadorNIB}"
    dados.clientes[novo_nib] = {"nome": nome, "senha": senha, "saldo": 1000.0, "Movimentos": [], "Ativo": True}
    print(f"Cliente criado! NIB: {novo_nib}")
    dados.contadorNIB += 1